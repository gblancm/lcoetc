# Read ZP files in LCOETC format and plotting it. 
# It works onlyt as a diagnostic tool to inspec the zerop
import sys
import matplotlib.pyplot as plt
from astropy.io import ascii
from scipy.interpolate import interp1d

filein=sys.argv[1]

if len(sys.argv) > 2:
    interpolation = str(sys.argv[2])
else:
    interpolation  = 'linear'


#Specifies the kind of interpolation as a string or as an integer specifying the order of the spline interpolator to use. The string has to be one of ‘linear’, ‘nearest’, ‘nearest-up’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘previous’, or ‘next’. ‘zero’, ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of zeroth, first, second or third order; ‘previous’ and ‘next’ simply return the previous or next value of the point; ‘nearest-up’ and ‘nearest’ differ when interpolating half-integers (e.g. 0.5, 1.5) in that ‘nearest-up’ rounds up and ‘nearest’ rounds down. Default is ‘linear’.

data=ascii.read(filein, header_start=0, data_start=0)

lam=data['lambda'].data
zplam=data['zeropoint'].data

f=interp1d(lam, zplam, kind=interpolation, bounds_error=False, fill_value=0)
zp_interpolated=f(lam)

plt.plot(lam, zplam, '*', label='data')
plt.plot(lam, zp_interpolated, label=interpolation)
plt.legend(loc='best')
plt.show()


    
    
