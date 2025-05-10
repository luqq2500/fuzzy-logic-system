from service.variable_service import VariableService
from data.variables import VARIABLES

registered_variables = []
for variable in VARIABLES:
    variable_service = VariableService(variable['name'])
    variable_service.createVariable(variable['variable_universe'], variable['variable_type'])
    ordinal_values = []
    for ordinal in variable['membership_universe']:
        ordinal_values.append(variable['membership_universe'][ordinal])
    variable_service.createMembership(ordinal_values, variable['membership_function'])
    registered_variables.append(variable_service)


for variable in registered_variables:
    print(f'{variable.variable.fuzzy_variable}, '
          f'{variable.variable.name}: '
          f'{variable.variable.variable_universe}, '
          f'{variable.variable.variable_type}, '
          f'{variable.variable.membership_universe}, '
          f'{variable.variable.mf_type}')

