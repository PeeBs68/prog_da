import matplotlib.pyplot as plt #Don't actually need to do this as it comes with Anaconda
import numpy as np

'''
plt.plot([1,2,3,4])
plt.show()

plt.plot([1,2,3,4],[1,4,9,16])
plt.show()

plt.plot([1,2,3,4],[1,4,9,16],'bo')
plt.show()


x = np.arange(0.0, 10.0, 0.01) #Note: arange works with decimals. Just use 'range' for integers
y = x * 3
noise = np.random.normal(0.0, 2.0, len(x))
plt.plot(x, y, 'bo')    #b = blue and o = a dot
plt.plot(x, noise, 'g-')    #g = green and - = a line
plt.show()

plt.plot(x, y, 'bo', label='Series1')           #label here is picked up by the legend command below
plt.plot(x, noise + y, 'g-', label='Series2')   #as above for the legend

plt.title('Speed v Distance') #Just sample title
plt.xlabel('Speed (kph)')       #Important to use measurements - kph etc.
plt.ylabel('Distance (km)')
plt.legend()
'''





plt.show()