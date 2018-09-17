# -*- coding: utf-8 -*-

''' created 9/16/18 by Brandon Molyneaux

This plots a bar in the "center" of the state by number of tornadoes (by zipcode).
Source: https://inkplant.com/code/state-latitudes-longitudes

Resultant image: 3d-basemap.png'''

import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import numpy as np

# 'State' : [# tornadoes, lat, lon]
stateCount = {'AK': [4, 61.370716, -152.404419],
 'AL': [2099, 32.806671, -86.791130],
 'AR': [1775, 34.969704, -92.373123],
 'AZ': [245, 33.729759, -111.431221],
 'CA': [430, 36.116203, -119.681564],
 'CO': [2129, 39.059811, -105.311104],
 'CT': [95, 41.597782, -72.755371],
 'DC': [2, 38.897438, -77.026817],
 'DE': [61, 39.318523, -75.507141],
 'FL': [3335, 27.766279, -81.686783],
 'GA': [1628, 33.040619, -83.643074],
 'HI': [41, 21.094318, -157.498337],
 'IA': [2501, 42.011539, -93.210526],
 'ID': [209, 44.240459, -114.478828],
 'IL': [2443, 40.349457, -88.986137],
 'IN': [1462, 39.849426, -86.258278],
 'KS': [4189, 38.526600, -96.726486],
 'KY': [949, 37.668140, -84.670067],
 'LA': [1969, 31.169546, -91.867805],
 'MA': [161, 42.230171, -71.530106],
 'MD': [353, 39.063946, -76.802101],
 'ME': [132, 44.693947, -69.381927],
 'MI': [1028, 43.326618, -84.536095],
 'MN': [1805, 45.694454, -93.900192],
 'MO': [2253, 38.456085, -92.288368],
 'MS': [2147, 32.741646, -89.678696],
 'MT': [413, 46.921925, -110.454353],
 'NC': [1283, 35.630066, -79.806419],
 'ND': [1537, 47.528912, -99.784012],
 'NE': [2836, 41.125370, -98.268082],
 'NH': [89, 43.452492, -71.563896],
 'NJ': [146, 40.298904, -74.521011],
 'NM': [582, 34.840515, -106.248482],
 'NV': [88, 38.313515, -117.055374],
 'NY': [436, 42.165726, -74.948051],
 'OH': [1079, 40.388783, -82.764915],
 'OK': [3800, 35.565342, -96.928917],
 'OR': [112, 44.572021, -122.070938],
 'PA': [786, 40.590752, -77.209755],
 'PR': [26, 18.200178, -66.664513],
 'RI': [10, 41.680893, -71.511780],
 'SC': [989, 33.856892, -80.945007],
 'SD': [1773, 44.299782, -99.438828],
 'TN': [1188, 35.747845, -86.692345],
 'TX': [8753, 31.054487, -97.563461],
 'UT': [128, 40.150032, -111.862434],
 'VA': [710, 37.769337, 78.169968],
 'VT': [44, 44.045876, -72.710686],
 'WA': [118, 47.400902, -121.490494],
 'WI': [1348, 44.268543, -89.616508],
 'WV': [138, 38.491226, -80.954453],
 'WY': [663, 42.755966, -107.302490]}

# make numpy arrays for plotting.
allTors = np.array([stateCount[key][0] for key in stateCount])
lats = np.array([stateCount[key][1] for key in stateCount])
lons = np.array([stateCount[key][2] for key in stateCount])

# set up plot
plt.close('all')
fig = plt.figure(figsize = (12, 8))
ax = fig.gca(projection='3d')
extent = [-127, -65, 25, 51]

# make the map and axis.
m = Basemap(llcrnrlon=extent[0], llcrnrlat=extent[2],
             urcrnrlon=extent[1], urcrnrlat=extent[3],
             projection='cyl', resolution='l', ax=ax)
ax.add_collection3d(m.drawcoastlines(linewidth=0.25))
ax.add_collection3d(m.drawcountries(linewidth=0.25))
ax.add_collection3d(m.drawstates(linewidth=0.25))
ax.view_init(azim = 285, elev = 45)
ax.set_zlabel(u'Tornadoes', labelpad = 4, size = 'small')
for t in ax.zaxis.get_major_ticks(): 
    t.label.set_fontsize(5)

# convert to map projection and plot
x, y = m(lons, lats)
ax.bar3d(x, y, np.array([0] * len(lats)), 0.5, 0.5, allTors, color = 'r', alpha = 0.5)

# more stuff with the graph
plt.title("Tornado # by state in 3D", size = 'medium')
ax.set_zlim(0., 9000)
plt.show()
