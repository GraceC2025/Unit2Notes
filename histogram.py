import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

# generate data
rng = np.random.default_rng(1701)
data = rng.normal(size=1000)