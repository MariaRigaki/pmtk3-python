from scipy import stats
import pylab as plt
import numpy as np

x = np.arange(0.0001, 1.0, 0.0001)

H = -(x*np.log2(x) + (1-x)*np.log2(1-x))

plt.plot(x, H)
plt.xlabel('p(X = 1)')
plt.ylabel('H(X)')
plt.xticks([0.0, 0.5, 1.0])
plt.yticks([0.0, 0.5, 1.0])
plt.show()