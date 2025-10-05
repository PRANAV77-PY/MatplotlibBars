import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Raina','Jadeja','KL Rahul','tendulkar'])
y = np.array([3,8,1,10])

plt.barh(x,y,height = 0.2)

plt.show()