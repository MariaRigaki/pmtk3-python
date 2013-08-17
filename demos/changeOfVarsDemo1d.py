import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(-1.0, 1.1, 0.1)
a = -1.0
b = 1.0

px = 1 / (b - a)* np.ones((len(xs)))
print len(px)
ys = xs**2

# Analytic
ppy = 1 / (2 * np.sqrt(xs))

# Monte Carlo
n = 1000
samples = np.random.rand(1000)*(b - a) + a
samples2 = samples**2

ax1 = plt.subplot(131)
plt.plot(xs, px)
ax2 = plt.subplot(132)
plt.plot(ys, ppy)
ax3 = plt.subplot(133)
plt.hist(samples2, 20, normed=1, facecolor='blue', alpha=0.9, rwidth=1.0)

plt.show()