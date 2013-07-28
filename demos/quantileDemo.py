import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Plot between -10 and 10 with .001 steps.
range = np.arange(-3, 3, 0.001)
ax1 = plt.subplot(121)
plt.plot(range, norm.cdf(range, 0, 1))

range = np.arange(-4, 4, 0.01)
range2 = np.arange(-4, -1.96, 0.01)
range3 = np.arange(1.96, 4, 0.01)

f = norm.pdf(range, 0, 1)
f2 = norm.pdf(range2, 0, 1)
f3 = norm.pdf(range3, 0, 1)

ax2 = plt.subplot(122)
plt.plot(range, f)
ax2.fill_between(range2, 0.0, f2, facecolor = 'blue')
ax2.fill_between(range3, 0.0, f3, facecolor = 'blue')
ax2.set_ylim([0.0, 0.5])
ax2.set_xlim([-4.0, 4.0])
ax2.set_xticks([0.0])
ax2.set_yticks([])

plt.show()