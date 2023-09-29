import numpy as np
import matplotlib.pyplot as plt
xpoints=np.array([1,8])
ypoints=np.array([3,10])

plt.plot(xpoints,ypoints, 'o')
plt.show()

xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints, 'o')
plt.show()

ypoints=np.array([3,8,1,10,5,7])

plt.plot(ypoints)
plt.show()

plt.plot(ypoints, marker = 'o')
plt.show()

plt.plot(ypoints, marker='D')
plt.show()

plt.plot(ypoints, 'o-.k')
plt.show()

plt.plot(ypoints, 'o:g', ms =10,mec='k', mfc = 'w')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

plt.plot(ypoints, ls=':')
plt.show()

plt.plot(ypoints, linestyle= 'dashed', color='r')
plt.show()


ypoints1=np.array([3,8,1,10])
ypoints2=np.array([6,2,7,3])
ypoints3=np.array([1,3,5,7])

plt.plot(ypoints1)
plt.plot(ypoints2)
plt.plot(ypoints3)
plt.show()































































































