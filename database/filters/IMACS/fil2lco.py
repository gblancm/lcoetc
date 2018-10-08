# Read filter curves and write in LCO ETC format

import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import astropy
from astropy.io import ascii
from scipy.interpolate import interp1d

filein=sys.argv[1]
fileout=sys.argv[2]

data=ascii.read(filein)

lam=data['col1']
flam=data['col2']

# For IMACS curves
lam=lam*10
flam=flam/100.


ascii.write([lam, flam], fileout, format='commented_header', names=['Wavelength_[A]', 'Transmission'], formats={'Wavelength_[A]':'%.3f', 'Transmission':'%.2f'})


plt.plot(lam, flam)
plt.show()


