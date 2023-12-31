import matplotlib.pyplot as plt #Don't actually need to do this as it comes with Anaconda
import numpy as np

x1 = np.random.uniform(0.0, 10.0, 100)
x2 = np.random.uniform(0.0, 5.0, 100)
x3 = np.random.randint(0, 20, 100)
x4 = np.random.uniform(0.0, 5.0, 100)

plt.scatter(x1, x2, c=x3, s=x4)

plt.show()