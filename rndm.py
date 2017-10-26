#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:51:28 2017

plot convergence map (kappa.fits) and residuals map (reshear.fits)

@author: themelis
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt


# open input fits file and observe the 1st component of the shear
#hdulist = fits.open('/local/home/themelis/Documents/Cpp/my_glimpse/example/cat_3_0.fits')
#scidata = hdulist[1].data['e1_gal  ']
#print(scidata.shape)
#plt.plot(scidata)
#plt.show()

# view the results of my_glimpse
vc0 = fits.getdata('/local/home/themelis/Documents/Cpp/my_glimpse/example/kappa.fits')
vc1 = fits.getdata('/local/home/themelis/Documents/Cpp/my_glimpse/example/jshear.fits')
plt.figure(0); plt.imshow(vc0)
plt.figure(1); plt.imshow(vc1)

print("Shear max: ", np.amax(vc1))
print("Shear min: ", np.amin(vc1))

 
