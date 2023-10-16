import matplotlib.pyplot as plt #Don't actually need to do this as it comes with Anaconda
import numpy as np

'''
#plotting two plots side by side
x = np.random.normal(0.0, 1.0, 100000) #min, max and total
plt.subplot(1, 2, 1) #row, column, position
#can swap them around to have 2 rows and 1 column etc
plt.hist(x, bins=100)

x = np.random.uniform(-4.0, 3.0, 1000)
plt.subplot(1, 2, 2) #row, column, position
plt.hist(x, bins=100)

plt.show()
'''
#scatterplots - can plot up to 4 dimensions

x1 = np.random.uniform(0.0, 10.0, 100)
x2 = np.random.uniform(0.0, 5.0, 100)
x3 = np.random.randint(0, 20, 100)
x4 = np.random.uniform(0.0, 5.0, 100)

plt.scatter(x1, x2, c=x3, s=x4)

plt.show()






