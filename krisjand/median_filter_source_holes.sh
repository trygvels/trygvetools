#!/bin/bash

me=/mn/stornext/u3/krisjand/quiet_svn/oslo/src/f90/map_editor/map_editor



if [ $# -ne 3 ]; then
    echo ""
    echo "Syntax: median_filter_source_holes.sh [radius string (arcmin)] [threshold string] [inmap]"
    echo ""
    echo 'e.g. ...holes "5 10 20" "5 10 15" co32_c0001_k000001_10arcmin.fits'
    echo ""
    exit
fi

if [[ $3 = *".fits"* ]]; then
    inmap=$3
else
    echo ""
    echo "Error: inmap must be a fits-file"
    echo ""
fi

arcmins=($1)
thresholds=($2)




echo ""
echo "Median filtering source holes"
echo "Infile: $inmap"
echo "Filtering radii: $1"
echo "Filtering thresholds: $2"
echo ""
echo "Starting filtering"
echo "--------------------------------------"

for ((i=0;i<${#arcmins[@]};i++)); do
    arcmin=${arcmins[$i]}
    for ((j=0;j<${#thresholds[@]};j++)); do
	threshold=${thresholds[$j]}
	outmap=${inmap/.fits/_median_filter_${arcmin}arcmin_${threshold}threshold.fits}
	
	echo "Radius: $arcmin arcmin"
	echo "Threshold: $threshold"
	echo "Outmap: $outmap"

	if [ -r $outmap ];then
	    echo "Outmap already exists, continue to next radius/threshold"
	    continue
	fi

	$me median_filter_source_holes $inmap $arcmin $threshold $outmap
	map2png $outmap ${outmap/.fits/_max2.png} -bar -min 0 -max 2
	map2png $outmap ${outmap/.fits/_max10.png} -bar -min 0 -max 10
	map2png $outmap ${outmap/.fits/_max${threshold}.png} -bar -min 0 -max ${threshold}
	map2png mask_${outmap} -bar -min 0 -max 1
	map2png apomask_${outmap} -bar -min 0 -max 1
	echo "---------------------------------------------"
    done
done

echo "Finished median filtering"
echo ""
