In order to generate the .dat files required by the ETC, follows this workflow:

1. Run the FIT_CONTINUUM_TO_ZP.ipynb notebook  to fit a continuum to the Francesco's eff files (do it for each telescope/instrument setup). 
   This will remove absorption lines and spikes from output data. Note that smoothed zero points  will be saved with a .eff2 extension.

2. Run the zp2lco.py to convert the smoothed zero points (.eff2) from Francesco's formart to ETC format. The output data will have 
   a .dat extension, following this pattern MAGELLAN1_IMACS_F2_400_18_ZP.dat.

3. Move the final data (.dat) files to the 'zeropoints' folder. 

4. You are ready to pull request them to github.
