from config.configs import VARIABLE_TYPE, MEMBERSHIP_FUNCTIONS

def isValidVarType(varType):
    if varType.lower() not in VARIABLE_TYPE:
        raise ValueError(f'Variable type "{varType}" is not valid. Must be one of {VARIABLE_TYPE}.')
    return True

def isValidVarParam(params):
    if not isinstance(params, (list, tuple)):
        raise TypeError(f'Variable universe must be a list or tuple of three values: [start, stop, step]. Got {type(params).__name__}: {params}')
    if len(params) != 3:
        raise ValueError(f'Variable universe {params} must contain exactly 3 values: [start, stop, step].')
    if params[0]>params[1]:
        raise ValueError(f'Variable universe start value {params[0]} must be less than stop value {params[1]}.')
    if params[2]>(params[1] - params[0]):
        raise ValueError(f'Step size {params[2]} is too large for the given range [{params[0]}, {params[1]}].')
    for param in params:
        if isinstance(param, float):
            raise ValueError(f'All variable universe parameters must be integers. Got float: {param}')
    return True

def isValidMfType(mf_type):
    if mf_type.lower() not in MEMBERSHIP_FUNCTIONS:
        raise ValueError(f'Membership function type "{mf_type}" is not supported. Use one of {MEMBERSHIP_FUNCTIONS}.')
    return True