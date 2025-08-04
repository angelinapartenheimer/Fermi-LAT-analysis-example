import numpy as np
from fermipy.gtanalysis import GTAnalysis
import matplotlib.pyplot as plt
from fermipy.plotting import SEDPlotter

sourcename = 'J0616.1-0428'

gta = GTAnalysis('config.yaml')
gta.setup()
gta.optimize()

# Free sources and fit
gta.free_source('galdiff', pars = 'norm')
gta.free_source('isodiff', pars = 'norm')
gta.free_sources(minmax_ts=[10,None],pars='norm')

#Free all parameters and fit
gta.free_sources()
fit = gta.fit()

#Show the best-fit spectral index and expected energy flux
#Note that the energy flux is printed in MeV/cm^2/s, which we convert to erg/cm^2/s
print(gta.roi[sourcename])

#SED
sed = gta.sed(sourcename, loge_bins=gta.log_energies[::4])

#Castro plot
plt.clf()
ylim = [1e-8, 1e-5]
fig = plt.figure(figsize = (8, 5))
SEDPlotter(sed).plot(showlnl=True)
plt.gca().set_ylim(ylim)
plt.savefig('sed_{}.png'.format(sourcename[:5]))
