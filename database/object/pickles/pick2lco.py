# Write Pickels templates to LCO ETC format
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

flam=flam/np.median(flam)

ascii.write([lam, flam], fileout, format='commented_header', names=['Wavelength_[A]', 'F_lambda_[norm]'], formats={'Wavelength_[A]':'%.3f', 'F_lambda_[norm]':'%.5f'})


plt.plot(lam, flam)
plt.show()



