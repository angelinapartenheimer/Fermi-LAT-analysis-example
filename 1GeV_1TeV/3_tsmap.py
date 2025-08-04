import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import astropy

from fermipy.gtanalysis import GTAnalysis
from fermipy.plotting import ROIPlotter

#Reload fit created in the last step of 2_fit.py
gta = GTAnalysis.create('data/fit_model.npy')

#Exclude the sub-threshold source J0616.1-0428 from the model so it is visible in the TS Map
tsmap = gta.tsmap('KM3-231203A', exclude=['J0616.1-0428'])

#Generate a TS Map
o = tsmap
plotter = ROIPlotter(o['sqrt_ts'],roi=gta.roi)
plotter.plot(vmin=0,vmax=5,levels=[3,5,7,9],subplot=111,cmap='magma', cb_kwargs = dict(orientation='vertical', shrink=1.0, pad=0.1, fraction=0.1, cb_label='sup'))

#Circles indicating containment circles of KM3NeT neutrino
plotter.draw_circle(radius = 1.5, linestyle = '-', linewidth = 2)
plotter.draw_circle(radius = 2.2, linestyle = '--', linewidth = 2)
plotter.draw_circle(radius = 3.0, linestyle = ':', linewidth = 2)

#Circle J0616.1-0428 for visibility
plotter.draw_circle(radius = 0.3, linewidth = 2, linestyle = 'solid', skydir = astropy.coordinates.SkyCoord(94.023, -4.479, unit='deg'))

#Plot labels
plt.gca().set_title(r'$\sqrt{TS}$', fontsize = 30)
plt.gca().set_xlabel('RA', fontsize = 24)
plt.gca().set_ylabel('DEC', fontsize = 24)
plt.gca().tick_params(labelsize=24)
plt.show()
