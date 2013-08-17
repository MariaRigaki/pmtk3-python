import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, t

def plotData(data, nbins):
	# Plot the histogram
	n, bins, patches = plt.hist(data, nbins, normed=1, facecolor='blue', alpha=0.9, rwidth=0.8)
	
	# Calculate mu, sigma
	mu = np.mean(data)
	std1 = np.std(data)
	sigma = std1**2
	x = np.arange(-5, 10, 0.01)

	# Plot the gaussian fit
	f1 = norm.pdf(x, mu, sigma)
	plt.plot(x, f1, 'b:', linewidth=2.0)

	# Plot student t
	dof = nbins - 1
	nu = 1
	dist = t(dof)
	f2 = dist.pdf(x)
	plt.plot(x, f2, 'r', linewidth=2.0)
	
	# Laplace distribution
	b = np.sqrt(sigma/2)
	f3 = 1/(2 * b) * np.exp(-np.abs(x - mu) / b)
	plt.plot(x, f3, 'b--', linewidth=2.0)


n = 40
np.random.seed(8)
data = np.random.randn(n, 1)
outliers = np.array([8, 8.75, 9.5])
nn = len(outliers)
nbins = 7

legend_str = ['Gauss', 'Student', 'Laplace']
ax1 = plt.subplot(121)
plotData(data, nbins)
ax1.set_ylim([0, 0.5])
ax1.set_xlim([-5, 10])
ax1.legend(legend_str)

ax2 = plt.subplot(122)
ax2.set_ylim([0, 0.5])
ax2.set_xlim([-5, 10])
outliers = np.reshape(outliers, (3,1))
outliers = np.concatenate((data, outliers), axis=0)
plotData(outliers, nbins + nn)
ax2.legend(legend_str)

plt.show()
#plotPDFs([data ; outliers])