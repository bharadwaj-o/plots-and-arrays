import numpy as np
import matplotlib.pyplot as plt


plt.axhline(y=2, color='red')
plt.axvline(x=2, color= 'red')
plt.show()

x=np.array(['A','B','C','D'])
y=np.array([5,6,3,1])

fig, ax = plt.subplots()
z=ax.bar(x,y, 0.6)
ax.bar_label(z, label_type='center')
plt.show()


mass=np.array([10,20,30,40,50])
weight=np.array([100,200,300,400,500])

plt.plot(mass,weight, color='blue',linestyle='-')
plt.xlabel("Mass")
plt.ylabel("Weight")
plt.title("Weight and Mass on Earth")
plt.show()

x=np.array([])
y=np.array([])
with open('test.txt', 'r') as testfile:
    for i in testfile:
        x=np.append(x, int(i[0]))
        y=np.append(y, int(i[2]))
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample Graph!")
plt.show()







