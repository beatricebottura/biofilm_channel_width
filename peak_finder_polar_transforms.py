# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 2021

@author: Beatrice Bottura
"""


# imports
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks, peak_widths

# read in data 
df = pd.read_excel(r'filename.xlsx')

# assign values for micrometer conversion  (if using the polar transformer plugin)
num_pixels_y = 7200         # number of pixels in the y direction, as entered on the polar transformer plugin      
radius = 1100               # radial distance from the centre at which line profile was acquired (in um!)

# plot signal (by extracting data from excel sheet)
plt.plot(df.distance, df.gray, c='#0087BD')     
plt.xlabel('Distance (pixels)')
plt.ylabel('Gray level')

# find minimum and maximum of signal
max_signal = np.max(df.gray)
min_signal = np.min(df.gray)

# find peaks (returns indices of data array at which peaks occur) 
    # the values inside the find_peaks() function can be adjusted if needed
peaks, _ = find_peaks(df.gray, height=750, distance=9, prominence=0.2*(np.max(df.gray)-np.min(df.gray)))

# calculate FWHMs (in pixel units)
peaks_half = peak_widths(df.gray, peaks, rel_height=0.5)
FWHM = peaks_half[0]

# convert FWHMs to micrometer units (if using the polar transformer plugin)
FWHM_um = FWHM*2*math.pi*radius/num_pixels_y    

# plot peaks and FWHM lines
plt.plot(df.gray)
plt.plot(peaks, df.gray[peaks], "x")
plt.hlines(*peaks_half[1:], color="C2")
plt.show()



