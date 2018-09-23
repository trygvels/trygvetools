import healpy as hp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, rc
from scipy.stats.stats import pearsonr
plt.style.use(u"trygveplot")
"""
y = '/Users/trygveleithesvalheim/Datafiles/mdata/npipe/fits/v14.2/chisq_c0001_n064.fits'
y = hp.read_map(y)
plt.plot(np.arange(len(y)),y)
plt.show()
print np.mean(y)
y1=y
y1[np.where(y1>100000)]=0
plt.plot(np.arange(len(y1)),y1)
plt.show()
print np.mean(y1)
"""
dame = 'dame64.fits'
dame = hp.read_map(dame)

npipe21 = 'co_npipe21.fits'
npipe21 = hp.read_map(npipe21)

sbgv8 = 'sbco.fits'
sbgv8 = hp.read_map(sbgv8)

dx12 = 'dx12co.fits'
dx12 = hp.read_map(dx12)

s=2

b, m = np.polyfit(dame, dx12, 1)
print "dx12 a=%.3g"%(b)
r, p = pearsonr(dame, dx12)
plt.scatter(dame, dx12, label="DX12 r=%.3g"%(r), s=s, color="C0")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, dx12, 1))(np.unique(dame)),'--', color="C0")
"""
b, m = np.polyfit(dame, sbgv8, 1)
print "old a=%.3g"%(b)
r, p = pearsonr(dame, sbgv8)
plt.scatter(dame, sbgv8, label="Early NPIPE r=%.3g"%(r),s=s, color="C2")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, sbgv8, 1))(np.unique(dame)),'--', color="C2")
"""
b, m = np.polyfit(dame, npipe21, 1)
print "new a=%.3g"%(b)
r, p = pearsonr(dame, npipe21)
plt.scatter(dame,npipe21, label="Best fit NPIPE r=%.3g"%(r),s=s, color="C1")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, npipe21, 1))(np.unique(dame)),'--', color="C1")

plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, dame, 1))(np.unique(dame)),'-',label="Dame et al.", color="C7", alpha=0.2)


plt.xlabel(r"Dame et al. CO amplitude $[\mathrm{K_{RJ}}\mathrm{km/s}]$")
plt.ylabel(r"Planck CO amplitude $[\mathrm{K_{RJ}}\mathrm{km/s}]$")
plt.legend(markerscale=5)
plt.xlim(0,170)
plt.ylim(0,200)
#plt.savefig("coscatter.pdf", bbox_inches='tight',  pad_inches=0.02)
plt.show()

#### 2-1
npipe21 = 'co21_npipe21.fits'
npipe21 = hp.read_map(npipe21)

sbgv8 = 'sbco21.fits'
sbgv8 = hp.read_map(sbgv8)
"""
b, m = np.polyfit(dame, sbgv8, 1)
print "old a=%.3g"%(b)
r, p = pearsonr(dame, sbgv8)
plt.scatter(dame, sbgv8, label="Early NPIPE r=%.3g"%(r),s=s, color="C2")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, sbgv8, 1))(np.unique(dame)),'--', color="C2")
"""
b, m = np.polyfit(dame, npipe21, 1)
print "new a=%.3g"%(b)
r, p = pearsonr(dame, npipe21)
plt.scatter(dame,npipe21, label="Best fit NPIPE r=%.3g"%(r),s=s, color="C1")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, npipe21, 1))(np.unique(dame)),'--', color="C1")

plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, dame, 1))(np.unique(dame)),'-',label="Dame et al.", color="C7", alpha=0.2)


plt.tick_params(axis='both', which='major', labelsize=16)
plt.xlabel(r"Dame et al. CO amplitude $[\mathrm{K_{RJ}}\mathrm{km/s}]$",fontsize=22)
plt.ylabel(r"Planck CO 2-1 amplitude $[\mathrm{K_{RJ}}\mathrm{km/s}]$",fontsize=22)
plt.legend(markerscale=5,fontsize=18,loc=4)
plt.xlim(0,90)
plt.ylim(0,60)
plt.savefig("co21scatter.pdf", bbox_inches='tight',  pad_inches=0.02)
plt.show()

#### 3-2
npipe21 = 'co32_npipe21.fits'
npipe21 = hp.read_map(npipe21)

sbgv8 = 'sbco32.fits'
sbgv8 = hp.read_map(sbgv8)

s=2
"""
b, m = np.polyfit(dame, sbgv8, 1)
print "old a=%.3g"%(b)
r, p = pearsonr(dame, sbgv8)
plt.scatter(dame, sbgv8, label="Early NPIPE r=%.3g"%(r),s=s, color="C2")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, sbgv8, 1))(np.unique(dame)),'--', color="C2")
"""
b, m = np.polyfit(dame, npipe21, 1)
r, p = pearsonr(dame, npipe21)
print "new a=%.3g"%(b)
plt.scatter(dame,npipe21, label="Best fit NPIPE r=%.3g"%(r),s=s, color="C1")
plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, npipe21, 1))(np.unique(dame)),'--', color="C1")

plt.plot(np.unique(dame), np.poly1d(np.polyfit(dame, dame, 1))(np.unique(dame)),'-',label="Dame et al.", color="C7", alpha=0.2)

plt.tick_params(axis='both', which='major', labelsize=16)
plt.xlabel(r"Dame et al. CO amplitude $[\mathrm{K_{RJ}}\mathrm{km/s}]$",fontsize=22)
plt.ylabel(r"Planck CO 3-2 amplitude $[\mathrm{K_{RJ}}\mathrm{km/s}]$",fontsize=22)
plt.legend(markerscale=5,fontsize=18,loc=4)
plt.xlim(0,120)
plt.ylim(0,30)
plt.savefig("co32scatter.pdf", bbox_inches='tight',  pad_inches=0.02)
plt.show()
