import matplotlib.pyplot as plt
import numpy as np

# set style for chart
plt.style.use('seaborn-v0_8-pastel')

# create sample set of data
# remember that X is independent variable
x_vals = np.linspace(0, 10, 100)

# line plots are good to graph functions
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

# save figure as png in dictionary
plt.savefig('lineplot.png')

# alternatively set up a figure object for the plot
fig = plt.figure()
ax = plt.axes()

# plot a function on the axes object instance
ax.plot(x_vals, 2*(x_vals), color = "turquoise")
plt.savefig('lineplot2.png')