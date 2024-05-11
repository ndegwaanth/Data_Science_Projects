from matplotlib import pyplot as plt
import numpy as np


a = np.array([20,87,4,40,53,74,56,51,11,20,40,15,79,25,27])
b = np.array([2,3,4,5,7,10,11,13,15,20,42,25,29,35,30])
plt.hist(a, bins=[0,20,40,60,80,100])
plt.hist(b, bins=[0,10,15,20,25,30])
plt.title("Histogram")
plt.show()

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()