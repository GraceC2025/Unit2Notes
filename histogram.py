import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

# generate data
rng = np.random.default_rng(1701)
data = rng.normal(size=1000)

plt.hist(data)
plt.savefig('histogram.png')
plt.close()

# more customized histogram
plt.hist(data, bins=30, density=True, alpha=0.5, histtype='stepfilled', color='turquoise', edgecolor='none')
plt.savefig('histogram2.png')
plt.close()

# hexagonal binnings
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T
plt.hexbin(x, y, gridsize=50)
cb = plt.colorbar(label='count in bin')
plt.savefig('histogram3.png')
plt.close()
