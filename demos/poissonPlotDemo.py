from scipy import stats
import pylab as plt
import numpy as np

N = 25
x = np.arange(0, N, 1)
mu = 1.0
dist = stats.poisson(mu)
ax1 = plt.subplot(121)
ax1.set_title(r'Po($\lambda$ = 1.000)')
ax1.set_xlim([0.0, 30.0])
plt.bar(x, dist.pmf(x))

mu = 10.0
dist = stats.poisson(mu)
ax2 = plt.subplot(122)
ax2.set_title(r'Po($\lambda$ = 10.000)')
ax2.set_xlim([0.0, 30.0])
plt.bar(x, dist.pmf(x))

plt.show()