from service.rule_service import RuleService
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

temperature = registered_variables[0]
temperature_memberships = []
for membership in temperature.variable.memberships:
    temperature_memberships.append(membership)

rule1 = RuleService('rule1')
rule1.setAntecedent([temperature_memberships[0],'&', temperature_memberships[1]])
rule1.setConsequent(registered_variables[1].variable.memberships[0])
rule1.createRule()
print(rule1.rule.rule)
