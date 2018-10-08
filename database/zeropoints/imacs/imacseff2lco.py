# Read efficiency (throughput) files in IMACS format and write them as ZP in LCOETC format
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import astropy
from astropy.io import ascii
from scipy.interpolate import interp1d

def elam2zp(elam, lam, neobj, ddisp, texp, atel, klam, amass): # Zero Point from System Efficiency
    # The ZP is typically given for 1 e/s/pixel
    # Convert throughput in efficiency
    h=6.6260755e-27   # Planck's constant in [erg*s]
    return 2.5*np.log10(elam*ddisp*texp*atel/(h*lam*neobj))-48.6-klam*amass


# Grism 150-11

filein='gris150-11.qe'
fileout='MAGELLAN1_IMACS_F2_150_11_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

kdata=ascii.read(klamfile)
# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})



# Grism 200-15

filein='gris200-15.qe'
fileout='MAGELLAN1_IMACS_F2_200_15_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

#datafra=ascii.read('/Users/gblancm/work/LCO/lcoetc/francesco/data/Grism200.dat')
#plt.plot(lam, zpout)
#plt.plot(datafra['col1'].data, datafra['col2'].data)
#plt.show()


# Grism 300-17

filein='gris300-17.qe'
fileout='MAGELLAN1_IMACS_F2_300_17_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

#datafra=ascii.read('/Users/gblancm/work/LCO/lcoetc/francesco/data/Grism300B.dat')
#plt.plot(lam, zpout)
#plt.plot(datafra['lambda'].data, datafra['zeropt'].data)
#plt.show()

    
# Grism 300-26

filein='gris300-26.qe'
fileout='MAGELLAN1_IMACS_F2_300_26_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

    
    
# Grating 150+3 +3.4

filein='grat150-3_3.4.qe'
fileout='MAGELLAN1_IMACS_F4_150-3_3.4_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

# Grating 300-4_6.0

filein='grat300-4_6.0.qe'
fileout='MAGELLAN1_IMACS_F4_300-4_6.0_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

# Grating 600-8_9.3

filein='grat600-8_9.3.qe'
fileout='MAGELLAN1_IMACS_F4_600-8_9.3_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

# Grating 600-13_14.0

filein='grat600-13_14.0.qe'
fileout='MAGELLAN1_IMACS_F4_600-13_14.0_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

# Grating 1200-17_19.0

filein='grat1200-17_19.0.qe'
fileout='MAGELLAN1_IMACS_F4_1200-17_19.0_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})


# Grating 1200-27_27.0

filein='grat1200-27_27.0.qe'
fileout='MAGELLAN1_IMACS_F4_1200-27_27.0_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})

# Grating 1200-27_33.5

filein='grat1200-27_33.5.qe'
fileout='MAGELLAN1_IMACS_F4_1200-27_33.5_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})


# Grating 1200-32_32.2

filein='grat1200-32_32.2.qe'
fileout='MAGELLAN1_IMACS_F4_1200-32_32.2_ZP.dat'
klamfile='/Volumes/gblanc/lcoetc/database/sky/klam.dat'
atel=306383.8

data=ascii.read(filein)
lam=data['col1'].data
elam=data['col2'].data

# trim to lrange only
lam0=kdata['col1'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
klam0=kdata['col2'][(kdata['col1'] > np.amin(lam)) * (kdata['col1'] < np.amax(lam))]
# interpolate to lam
f=interp1d(lam0, klam0, fill_value='extrapolate')
klam=f(lam)

zpout=elam2zp(elam, lam, 1.0, 1.0, 1.0, atel, klam, 1.0)
ascii.write([lam, zpout], '../'+fileout, format='commented_header', names=['lambda', 'zeropoint'], formats={'lambda':'%.3f', 'zeropoint':'%.2f'})
