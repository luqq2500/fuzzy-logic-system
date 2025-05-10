import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as controller
from models.variable import Variable
from config.configs import VARIABLE_MEMBERSHIP_ORDINALS, MEMBERSHIP_FUNCTIONS, VARIABLE_TYPE, EXPECTED_MF_LENGTH
from config.validation import isValidVarType,isValidVarParam, isValidMfType


class VariableService:
    def __init__(self, name):
        self.variable = Variable(name)

    # ====== C O R E ====== #
    def createVariable(self, varParams, varType):
        self.setVarUniverse(varParams)
        self.setVarType(varType)
        if self.variable.variable_type == 'antecedent':
            self.variable.fuzzy_variable = controller.Antecedent(self.variable.variable_universe, self.variable.name)
        elif self.variable.variable_type == 'consequent':
            self.variable.fuzzy_variable = controller.Consequent(self.variable.variable_universe, self.variable.name)

    def createMembership(self, memberParams, mf_type):
        self.setMfType(mf_type)
        self.setMemberUniverse(memberParams)
        for ordinal, values in zip(VARIABLE_MEMBERSHIP_ORDINALS, self.variable.membership_universe):
            if self.variable.mf_type == 'trimf':
                self.variable.fuzzy_variable[ordinal] = fuzz.trimf(self.variable.fuzzy_variable.universe, values)
            elif self.variable.mf_type == 'trapmf':
                self.variable.fuzzy_variable[ordinal] = fuzz.trapmf(self.variable.fuzzy_variable.universe, values)
            self.variable.membership.append(self.variable.fuzzy_variable[ordinal])

    def getVariable(self):
        return self.variable

    # ====== S E T T E R ====== #
    def setVarUniverse(self, params):
        if isValidVarParam(params):
            self.variable.varUniverse = np.arange(params[0], params[1], params[2])
        else:
            raise ValueError('Variable universe is invalid.')

    def setMemberUniverse(self, params):
        if self.isValidMemberParam(params):
            self.variable.memberUniverse = params
        else:
            raise ValueError('Membership universe incomplete.')

    def setVarType(self, varType):
        if isValidVarType(varType):
            self.variable.varType = varType.lower()
        else:
            raise ValueError(f'{varType} is not valid. Please choose one from {VARIABLE_TYPE}')

    def setMfType(self, mf_type):
        if isValidMfType(mf_type):
            self.variable.mf_type = mf_type.lower()
        else:
            raise ValueError(f'Invalid membership function type. Choose one from {MEMBERSHIP_FUNCTIONS}')

    # ====== S E R V I C E  V A L I D A T I O N ======= #
    def isValidMemberParam(self, params):
        expected_length = EXPECTED_MF_LENGTH.get(self.variable.mf_type)
        if expected_length is None:
            raise ValueError(f'Membership function type {self.variable.mf_type} is not recognized.')
        if len(params) != len(VARIABLE_MEMBERSHIP_ORDINALS):
            raise ValueError(f'Number of membership params ({len(params)}) does not match expected ordinals ({len(VARIABLE_MEMBERSHIP_ORDINALS)}).')
        for i, param in enumerate(params):
            if len(param) != expected_length:
                raise ValueError(f'Membership param at index {i} is invalid. Expected {expected_length} values, got {len(param)}: {param}')
            if any(param[j] > param[j + 1] for j in range(len(param) - 1)):
                raise ValueError(f'Membership values at index {i} are not in non-decreasing order: {param}')
        return True