from config.settings import VARIABLES, VARIABLE_TYPE, VARIABLE_MEMBERSHIP_ORDINALS

def initVariables():
    variables = {}

    for variable, data in VARIABLES:
        if data['type']:
            dd