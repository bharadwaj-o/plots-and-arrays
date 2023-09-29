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





