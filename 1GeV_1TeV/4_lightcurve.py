import numpy as np
from fermipy.gtanalysis import GTAnalysis

gta = GTAnalysis.create('data/fit_model.npy')
sourcename = 'J0616.1-0428'

#Generate and save the light curve
#This can take awhile, so plotting is done separately in plot_lightcurve.py
lc = gta.lightcurve(sourcename, nbins = 12)
np.save('data/lc.npy', lc)
