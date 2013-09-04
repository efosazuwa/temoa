to_administrate = (
  'Analysis',
  'Commodity',
  'Param_CapacityToActivity',
  'Param_CostFixed',
  'Param_CostVariable',
  'Param_Demand',
  'Param_DemandDefaultDistribution',
  'Param_DemandSpecificDistribution',
  'Param_Efficiency',
  'Param_EmissionActivity',
  'Param_EmissionLimit',
  'Param_GrowthRateMax',
  'Param_GrowthRateSeed',
  'Param_LifetimeTech',
  'Param_LifetimeTechLoan',
  'Param_MaxCapacity',
  'Param_MinCapacity',
  'Param_ResourceBound',
  'Param_SegFrac',
  'Param_TechInputSplit',
  'Param_TechOutputSplit',
  'Process',
  'Set_commodity_demand',
  'Set_commodity_emission',
  'Set_commodity_physical',
  'Set_commodity_output',
  'Set_tech_baseload',
  'Set_tech_storage',
  'Technology',
  'Vintage',
)

_temp = __import__(
  'process_interface.models',
  globals(),
  locals(),
  to_administrate,
  0
)

  # the above __import__ replaces this next line.
# from process_interface.models import ( ... )

from django.contrib import admin

register = admin.site.register
for cls in to_administrate:
	register( getattr( _temp, cls ))
