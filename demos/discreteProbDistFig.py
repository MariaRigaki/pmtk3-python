import pylab as plt
import numpy as np 


def plotHist(locs):
	scounts = (1.0/len(locs))*np.ones((len(locs)))
	
	ax = plt.axes()
	ax.set_xticks(locs)
	ax.set_xticklabels(locs)
	ax.set_ylim([0, 1.0])
	ax.set_xlim([0, 5])
	plt.bar(locs, scounts, width = 0.8, align='center')

	plt.show()


plotHist(np.array([1, 2, 3, 4]))
plotHist(np.array([1]))


