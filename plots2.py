import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,6,7,8,7,17,2,4,9,12,9,6])
y=np.array([4,6,7,8,4,12,2,5,7,9,12,1])
sizes=np.array([10,20,30,40,50,55,200,65,70,76,80,85])
colors=np.array(['red','green','blue','yellow','orange','black','red','green','blue','yellow','orange','black'])

plt.scatter(x,y,s=sizes,c=colors)
plt.show()