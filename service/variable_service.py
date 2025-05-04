import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as controller
from config.configs import VARIABLE_MEMBERSHIP_ORDINALS, MEMBERSHIP_FUNCTIONS, VARIABLE_TYPE

class VariableService:
    def __init__(self, variable):
        self.variable = variable
    
    def initializeVariable(self, varParams, memberParams, varType, mf_type):    
        # Set variable universe, membership universe, and variable type. 
        self.setVarUniverse(varParams)
        self.setMfType(mf_type)
        self.setMemberUniverse(memberParams)
        self.setVarType(varType)

        # Get variable universe
        # Set variable as scikit-fuzzy Antecedent or Consequent.
        varUniverse = self.variable.getVarUniverse()
        varType = self.variable.getVarType()
        name = self.variable.getVarName()

        if (varType.lower() == 'antecedent'):
            self.variable.fuzzy_variable = controller.Antecedent(varUniverse, name)
        elif (varType.lower() == 'consequent'):
            self.variable.fuzzy_variable = controller.Consequent(varUniverse, name)
    
        # Set variable membership, from given membership params.    
        for ordinal, param in zip(VARIABLE_MEMBERSHIP_ORDINALS, memberParams):
            if mf_type == 'trimf':
                self.variable.fuzzy_variable[ordinal] = fuzz.trimf(self.variable.fuzzy_variable.universe, param)
            elif mf_type == 'trapmf':
                self.variable.fuzzy_variable[ordinal] = fuzz.trapmf(self.variable.fuzzy_variable.universe, param)
        
    def getVariable(self):
        return self.variable
        
    def setVarUniverse(self, params):
        if (self.isValidVarParam(params)):
            self.variable.varUniverse = np.arange(params[0], params[1], params[2])
        else:
            raise ValueError('Variable universe is invalid.')
    
    def isValidVarParam(self, params):
        if len(params) != 3:
            return False
        if (params[0]>params[1]):
            return False
        if (params[2]>(params[1]-params[0])):
            return False
        for param in params:
            if isinstance(param, float):
                return False
        return True 

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
    
    def isValidVarType(self, varType):
        if varType.lower() not in VARIABLE_TYPE:
            return False
        return True

    def setMfType(self, mf_type):
        if (self.isValidMfType(mf_type)):
            self.variable.mf_type = mf_type.lower()
        else:
            raise ValueError(f'Invalid membership function type. Choose one from {MEMBERSHIP_FUNCTIONS}')

    def isValidMfType(self, mf_type):
        return mf_type.lower() in MEMBERSHIP_FUNCTIONS
