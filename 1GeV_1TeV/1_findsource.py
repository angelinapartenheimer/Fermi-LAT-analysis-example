import numpy as np
from fermipy.gtanalysis import GTAnalysis
from fermipy.jobs.analysis_utils import localize_sources

#First time running setup can take several hours
gta = GTAnalysis('base_config.yaml')
gta.setup()
gta.optimize()

# Free all parameters in the region
gta.free_sources()

# Identify emission peaks
model = {'Index' : 2.0, 'SpatialModel' : 'PointSource'}
findsources = gta.find_sources(model=model, sqrt_ts_threshold=3) 
gta.print_model()


# Constrain positions of new sources
loc = gta.localize('PS J0616.1-0430')
print('*****************************')
print('RA = {}, DEC = {}, UNC95 = {}, UNC68 = {}'.format(loc['ra'],loc['dec'], loc['pos_r95'], loc['pos_r68']))
print('*****************************')
