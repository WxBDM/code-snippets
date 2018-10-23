# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:17:33 2017
@author: bdmolyne
"""

import netCDF4, os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.colors as colors

def write_text(x, y, text, halign, valign, fontsize = 'x-small', color = 'k'):
    ax.text(x, y, text, horizontalalignment = halign, verticalalignment = valign,
            transform=ax.transAxes, fontsize = fontsize, color = color)

#initialize variables, lists, arrays, etc.
variables = []
run = -3
plt.close('all')

os.chdir('Y:/model/')
path = '2015-02-01/'
file_name = 'wrfout_d01_2015-02-01_00%3A00%3A00.nc'

#variables needed for map and calculations
nx = 49 #dimensions in x
ny = 49 #dimensions in y
Rd = 287.00
g = 9.81
lower_bound = 39.222679
upper_bound = 42.661736
left_bound = -80.826416
right_bound = -73.146973

f = netCDF4.Dataset(path + file_name, 'r')

initialization = file_name[11:27].replace('%3A', '').replace('-','').replace('_', '') + 'Z'

#gets variable names
[variables.append(v) for v in f.variables]

for i in range(0, 25):
    run += 3
    plt.close('all')
    
    #puts all info into arrays for processing
    temp_k = f.variables['T2'][i, :, :] #initial conditions
    pressure = f.variables['PSFC'][i, :, :]
    lat = f.variables['XLAT'][i, :, :]
    lon = f.variables['XLONG'][i, :, :]
    times = f.variables['Times'][:]
    w = f.variables['Q2'][i, :, :]
    pressure = f.variables['PSFC'][i, : , :]
    height = f.variables['HGT'][i, : , :]
    
    Tv = mslp = temp_c = np.zeros([nx, ny])
    
    print('   drawing basemap')
    m = Basemap(projection = 'merc', llcrnrlat = lower_bound, urcrnrlat = upper_bound,
                llcrnrlon = left_bound, urcrnrlon = right_bound, resolution = 'i')
    m.drawstates(linewidth = 1, color = 'grey', zorder = 11)
    m.drawcounties(color = 'black', zorder = 10)
    m.drawcoastlines(linewidth = 1, color = 'grey', zorder = 11)
    
    x, y = m(lon, lat)
    
    #Calculates MSLP
    #First, calculate Tv using temperature in kelvin
    Tv[0:nx, 0:ny] = temp_k[0:nx, 0:ny] * (0.61 * w[0:nx, 0:ny] + 1.)
    #Next, calculate MSLP in hPa
    mslp[0:nx, 0:ny] = (pressure[0:nx, 0:ny] * np.exp((g * height[0:nx, 0:ny])/(Rd * Tv[0:nx, 0:ny]))) / 100.0
    #Plots the MSLP.
    cs_pressure = plt.contour(x, y, mslp, colors=('k',),linestyles=('-',),linewidths=(1,))
    plt.clabel(cs_pressure, inline = True, fontsize = 6, fmt = "%0.2d")
    
    #converts Pa to hPa/mb
    pressure[0:nx, 0:ny] = np.round(pressure[0:nx, 0:ny] / 100.) #converts Pa to mb
    
    #converts k to c
    temp_c[0 : nx, 0 : ny] = temp_k[0 : nx, 0 : ny] - 273.15 #calculates kelvin to c


    time = ''
    #grabs times.
    for j in range(len(times[i])):
        time += times[i][j].decode('ascii') 
    time_title = time.replace('_', ' ')
    time_title = time_title[:-6] + 'Z: Hour [' + str(run) + ']'
    save_fig_name = time.replace('-','').replace('_', '').replace(':', '')[:-4]
    
    print('Working on hour ' + str(run))
    print('time: ' + save_fig_name)
    
    levels_temp = np.arange(-16, 17, 1)
    cs_temp = plt.contourf(x, y, temp_c, cmap = 'RdBu_r', extend = 'both', levels = levels_temp)
    cb_temp = plt.colorbar(cs_temp, extend = 'both', label = 'Temperature (C)')
    
    ax = plt.gca()
    write_text(0.002, 1, '2m Temperature & MSLP (mb)\n{}'.format(time_title), 'left', 'bottom', fontsize = 'medium')
    write_text(1, 1, 'Brandon Molyneaux', 'right', 'bottom', fontsize = 'small', color = '#A0A0A0')
    
    print('   saving\n')
    save_location = path + '2mtemp_sfcpressure/'
    plt.savefig(save_location + initialization + '-{}Z_mslp-2mtemp'.format(save_fig_name), dpi = 400, bbox_inches = 'tight')
