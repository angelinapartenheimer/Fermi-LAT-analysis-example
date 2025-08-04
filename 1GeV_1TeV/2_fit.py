import numpy as np
from fermipy.gtanalysis import GTAnalysis

gta = GTAnalysis('config.yaml')
gta.setup()
gta.optimize()

# Free normalization for diffuse backgrounds and sources with TS >= 10
# Spectral indices fixed for this step; enforces 1 degree of freedom in evaluating the TS
gta.free_source('galdiff', pars = 'norm')
gta.free_source('isodiff', pars = 'norm')
gta.free_sources(minmax_ts=[10,None],pars='norm')


# The TS shown here is the TS we publish for the source
gta.print_model()


# Free all parameters, fit, and save the model
# Output of this fit used to generate TS map, light curve, and SED
gta.free_sources()
fit = gta.fit()
gta.write_roi('fit_model')
