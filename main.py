from service.variable_service import VariableService
from data.variables import VARIABLES

variable_service = VariableService()

for variable in VARIABLES:
    variable_service.startVariable(variable['name'])
    variable_service.createFuzzyVariable(variable['variable_universe'], variable['variable_type'])
    membership_universe = []
    for ordinal in variable['membership_universe']:
        membership_universe.append(ordinal)
    variable_service.createMembership(membership_universe, variable['membership_function'])
    variable_service.saveVariable()

    fuzzy_variable_name = variable_service.variable.name
    print(fuzzy_variable_name)