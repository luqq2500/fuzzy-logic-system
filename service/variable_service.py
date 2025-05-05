import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as controller
from models.variable import Variable
from config.configs import VARIABLE_MEMBERSHIP_ORDINALS, MEMBERSHIP_FUNCTIONS, VARIABLE_TYPE, EXPECTED_MF_LENGTH

class VariableService:
    def __init__(self):
        self.variable = None
        self.variables = []

    ################# CORE SERVICE ####################
    def initiateFuzzyVariable(self, name, varParams, memberParams, varType, mf_type):
        self.createVariable(name)
        self.createFuzzyVariable(varParams, varType)
        self.createMembership(memberParams,mf_type)
        self.saveFuzzyVariable(self.variable)
        return self.variable

    def createVariable(self, name):
        self.variable = Variable(name)

    def createFuzzyVariable(self, varParams, varType):    
        self.setVarUniverse(varParams)
        self.setVarType(varType)

        varUniverse = self.variable.getVarUniverse()
        varType = self.variable.getVarType()
        name = self.variable.getVarName()

        if (varType.lower() == 'antecedent'):
            self.variable.fuzzy_variable = controller.Antecedent(varUniverse, name)
        elif (varType.lower() == 'consequent'):
            self.variable.fuzzy_variable = controller.Consequent(varUniverse, name)
    
    def createMembership(self, memberParams, mf_type):
        self.setMfType(mf_type)
        self.setMemberUniverse(memberParams)
        for ordinal, param in zip(VARIABLE_MEMBERSHIP_ORDINALS, memberParams):
            if self.variable.mf_type == 'trimf':
                self.variable.fuzzy_variable[ordinal] = fuzz.trimf(self.variable.fuzzy_variable.universe, param)
            elif sel.variable.mf_type == 'trapmf':
                self.variable.fuzzy_variable[ordinal] = fuzz.trapmf(self.variable.fuzzy_variable.universe, param)
            
            self.variable.membership.append(self.variable.fuzzy_variable[ordinal])

    def saveFuzzyVariable(self,variable):
        self.variables.append(variable)

    ################# SETTER SERVICE ##################
    def setVarUniverse(self, params):
        if (self.isValidVarParam(params)):
            self.variable.varUniverse = np.arange(params[0], params[1], params[2])
        else:
            raise ValueError('Variable universe is invalid.')

    def setMemberUniverse(self, params):
        if (self.isValidMemberParam(params)):
            self.variable.memberUniverse = params
        else:
            raise ValueError('Membership universe incomplete.')
    
    def setVarType(self, varType):
        if (self.isValidVarType(varType)):
            self.variable.varType = varType.lower()
        else:
            raise ValueError(f'{varType} is not valid. Please choose one from {VARIABLE_TYPE}')

    def setMfType(self, mf_type):
        if (self.isValidMfType(mf_type)):
            self.variable.mf_type = mf_type.lower()
        else:
            raise ValueError(f'Invalid membership function type. Choose one from {MEMBERSHIP_FUNCTIONS}')

    ############## VALIDATION SERVICE #################
    def isValidVarParam(self, params):
        if len(params) != 3:
            raise ValueError(f'Variable universe {params} must contain exactly 3 values: [start, stop, step].')
            return False
        if (params[0]>params[1]):
            raise ValueError(f'Variable universe start value {params[0]} must be less than stop value {params[1]}.')
            return False
        if (params[2]>(params[1]-params[0])):
            raise ValueError(f'Step size {params[2]} is too large for the given range [{params[0]}, {params[1]}].')
            return False
        for param in params:
            if isinstance(param, float):
                raise ValueError(f'All variable universe parameters must be integers. Got float: {param}')
                return False
        return True 

    def isValidMemberParam(self, params):
        mf_type = self.variable.getMfType()
        expected_length = EXPECTED_MF_LENGTH.get(mf_type)
        if expected_length is None:
            raise ValueError(f'Membership function type {mf_type} is not recognized.')

        for i, param in enumerate(params):
            if len(param) != expected_length:
                raise ValueError(f'Membership param at index {i} is invalid. Expected {expected_length} values, got {len(param)}: {param}')
            if any(param[j] > param[j + 1] for j in range(len(param) - 1)):
                raise ValueError(f'Membership values at index {i} are not in non-decreasing order: {param}')
        
        if len(params) != len(VARIABLE_MEMBERSHIP_ORDINALS):
                raise ValueError(f'Number of membership params ({len(params)}) does not match expected ordinals ({len(VARIABLE_MEMBERSHIP_ORDINALS)}).')
        
        return True

    def isValidVarType(self, varType):
        if varType.lower() not in VARIABLE_TYPE:
           raise ValueError(f'Variable type "{varType}" is not valid. Must be one of {VARIABLE_TYPE}.')
        return True

    def isValidMfType(self, mf_type):
        if mf_type.lower() not in MEMBERSHIP_FUNCTIONS:
            raise ValueError(f'Membership function type "{mf_type}" is not supported. Use one of {MEMBERSHIP_FUNCTIONS}.')
        return True
    
