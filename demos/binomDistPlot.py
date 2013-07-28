from scipy import stats
import pylab as plt
import numpy as np

N = 10
x = np.linspace(0, N, 11)
theta = 0.25
pmf = stats.binom.pmf(x, N, theta)
ax1 = plt.subplot(121)
ax1.set_title('theta = 0.25')
plt.bar(x, pmf)

theta = 0.9
pmf = stats.binom.pmf(x, N, theta)
ax2 = plt.subplot(122)
ax2.set_title('theta = 0.9')
plt.bar(x, pmf)

plt.show()