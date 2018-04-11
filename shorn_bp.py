import matplotlib.pyplot as plt
import numpy as np

bps=['100-1a', '100-1b', '100-2a', '100-2b', '100-3a', '100-3b', '100-4a', '100-4b', '217-5a', '217-5b', '217-6a', '217-6b', '217-7a', '217-7b', '217-8a', '217-8b', '353-3a', '353-3b', '353-4a', '353-4b', '353-5a', '353-5b', '353-6a', '353-6b']
name=['100-1', '100-2', '100-3', '100-4','217-5','217-6','217-7','217-8','353-3','353-4','353-5','353-6']

j = 0
for i in range(0,len(bps)-1,2):
    print bps[i], bps[i+1]
    d1 = np.loadtxt('bp_RIMO_v2.0_'+bps[i]+'.dat')
    d2 = np.loadtxt('bp_RIMO_v2.0_'+bps[i+1]+'.dat')
    a = (d1[:,1]+d2[:,1])/2
    b = np.transpose([a])
    np.savetxt('bp_RIMO_v2.0_'+name[j]+'_SHORN.dat', np.c_[d1[:,0],a], delimiter=" ")
    j+=1
    #np.c_[x,y,z]

"""
d1 = np.loadtxt('bp_RIMO_v2.0_'+bps[0]+'.dat')
d2 = np.loadtxt('bp_RIMO_v2.0_'+bps[1]+'.dat')

a = (d1[:,1]+d2[:,1])/2
plt.plot(d1[:,0],a)
plt.plot(d1[:,0],d1[:,1])
plt.plot(d2[:,0],d2[:,1])
plt.legend(['average', '100-1a', '100-1b'])
plt.xlim(50,500)
plt.show()
"""
