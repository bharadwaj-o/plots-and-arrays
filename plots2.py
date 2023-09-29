import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,6,7,8,7,17,2,4,9,12,9,6])
y=np.array([4,6,7,8,4,12,2,5,7,9,12,1])
sizes=np.array([10,20,30,40,50,55,200,65,70,76,80,85])
colors=np.array(['red','green','blue','yellow','orange','black','red','green','blue','yellow','orange','black'])

plt.scatter(x,y,s=sizes,c=colors)

x= np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
xsizes=10*np.random.randint(100,size=(100))

plt.scatter(x,y,c=colors,s=xsizes, alpha=0.5, cmap='CMRmap')


x=np.array(['A','B','C','D'])
y=np.array([5,6,3,1])

plt.bar(x,y,color='red',width=0.2)


plt.barh(x,y, height = 0.2)


x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()

y=np.array([0.5,10,20,30,40,50])
x=['z','a','b','c','d','e']
exp=[0,0,0,0,0,0.2]
plt.pie(y, labels=x, startangle=90, explode=exp, shadow= True)

plt.show()











