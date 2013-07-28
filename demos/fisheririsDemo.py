import pylab as plt
from sklearn import datasets
import pandas as pd 


# import the dataset
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
Y = iris.target

# Use pandas to create the scatter matrix
pd.scatter_matrix(X, diagonal = 'hist', c = Y, alpha = 0.5)
plt.show()