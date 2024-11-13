import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='ticks', palette='pastel')

# create matplotlib histogram
data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)
plt.savefig('histogram4.png', bbox_inches='tight', pad_inches=0.4)
plt.close()

# KDE gives a smooth estimate of values
sns.kdeplot(data=data, fill=True)
plt.savefig('histogram5.png', bbox_inches='tight', pad_inches=0.4)
plt.close()

# load in a built-in dataset
iris = sns.load_dataset('iris')
print(iris.head())

# pair plot to visualize multi-dimensional data
sns.pairplot(iris, hue='species', height=2.5)
plt.savefig('pairplot.png', bbox_inches='tight', pad_inches=0.4)
plt.close()