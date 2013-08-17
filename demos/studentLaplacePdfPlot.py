from scipy import stats
import pylab as plt
import numpy as np


# Normal distribution
xs = np.arange(-4, 4, 0.2)
v = 1.0
mu = 0.0
f = stats.norm.pdf(xs, mu, v)

# Student t distribution
dof = 1
mu = 0.0
nu = 1
sigma = 1
dist = stats.t(dof)
f2 = dist.pdf(xs)

# Laplace distribution
b = np.sqrt(v/2)
f3 = 1/(2 * b) * np.exp(-np.abs(xs - mu) / b)


legend_str = ['Gauss', 'Student', 'Laplace']

ax1 = plt.subplot(121)
plt.plot(xs, f, 'k:', linewidth=3.0)
plt.plot(xs, f2, 'b--', linewidth=2.0)
plt.plot(xs, f3, 'r-', linewidth=2.0)
ax1.legend(legend_str)

ax2 = plt.subplot(122)
plt.plot(xs, np.log(f), 'k:', linewidth=3.0)
plt.plot(xs, np.log(f2), 'b--', linewidth=2.0)
plt.plot(xs, np.log(f3), 'r-', linewidth=2.0)
ax2.legend(legend_str)

plt.show()