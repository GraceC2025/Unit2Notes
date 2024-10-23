import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

# set style
plt.style.use('ggplot')

# generate data points
rng = np.random.default_rng(0)
x = rng.normal(size=100)
y = rng.normal(size=100)
colors = rng.random(100)
sizes = 1000 * rng.random(100)

# function where alpha sets opacity of points
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3)
plt.colorbar(); # shows color scale
plt.savefig('scatterplot.png')
plt.close()

# scatterplot with iris data
iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha=0.4, s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.colorbar()
plt.savefig('iris_scatter.png')

# 4 different properties:
# 1. length (x axis)
# 2. width (y axis)
# 3. petal width (size of dot)
# 4. species (color)