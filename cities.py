import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# load CSV file into dataframe
cities = pd.read_csv('california_cities.csv')
print(cities.info())

# extract the data we're going to plot
lat = cities['latd'] # x vals
lon = cities['longd'] # y vals
pop = cities['population_total']
area = cities['area_total_sq_mi']

# scatterplot
plt.scatter(lon, lat, label=None, c=np.log10(pop), cmap='inferno', s=area, linewidth=0, alpha=0.5)

# customize and save
plt.axis('equal')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.colorbar(label='log$_{10}$(pop)')
plt.title('CA Cities: Area/Population')

# customize legend to show city's area
# plot empty lists with desired size and label
for area in [100, 300, 500]: 
    plt.scatter([],[], c='y', alpha=0.9, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1)

plt.savefig('cities.png')