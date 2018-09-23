#!/bin/bash                                                                                   
#Smoothing script: low res to high res maps with 20' smoothing                                
#Input is k-number from Trygve. c01 might need to be changed.                                 
dir="/mn/stornext/u3/krisjand/stornext/npipe_highres/smooth_npipe_highres_trygve/"
maps=(
"dust_Td_c0001_k"$1"_n2048.fits"
"dust_beta_c0001_k"$1"_n2048.fits"
"synch_beta_c0001_k"$1"_n2048.fits")

minvals=(
35.
3.0
-1.5)

maxvals=(
10.
0.4
-4.5)
                
for i in ${!maps[@]}; do
    #max_scalar returns the maximum value of input map and given value (i.e. sets a minimum level)
    #min_scalar returns the minimum of the two inputs (map vs. value)
    map_editor max_scalar $dir${maps[$i]} $dir${maps[$i]/.fits/_threshold.fits} ${maxvals[$i]}
    map_editor min_scalar $dir${maps[$i]/.fits/_threshold.fits} $dir${maps[$i]/.fits/_threshold.fits} ${minvals[$i]}
    ##just for checking if the input and output filenames, and nside are correct              
    #echo ${maps[$i]/.fits/_threshold.fits}
    #echo ${minvals[$i]}
    #echo ${maxvals[$i]}
done
