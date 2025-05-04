import pytest
import numpy as np
from skfuzzy.control import Antecedent, Consequent
from service.variable_service import VariableService
from models.variable import Variable

# Mock Variable entity
class MockVariable:
    def __init__(self, name='Temperature'):
        self.name = name
        self.varUniverse = None
        self.memberUniverse = None
        self.varType = None
        self.mf_type = None
        self.fuzzy_variable = None

    def getMfType(self):
        return self.mf_type

    def getVarName(self):
        return self.name

    def getVarUniverse(self):
        return self.varUniverse

    def getVarType(self):
        return self.varType

# Config-like constants
VALID_VAR_PARAMS = [0, 10, 1]
VALID_MEMBER_PARAMS_TRIMF = [[0, 2, 4], [3, 5, 7], [6, 8, 10]]
VALID_MEMBER_PARAMS_TRAPMF = [[0, 1, 2, 3], [2, 3, 4, 5], [5, 6, 7, 8]]

def test_valid_var_param():
    var = MockVariable()
    vs = VariableService(var)
    assert vs.isValidVarParam(VALID_VAR_PARAMS) is True

def test_invalid_var_param_length():
    var = MockVariable()
    vs = VariableService(var)
    assert vs.isValidVarParam([0, 10]) is False

def test_invalid_var_param_range():
    var = MockVariable()
    vs = VariableService(var)
    assert vs.isValidVarParam([10, 0, 1]) is False

def test_set_var_universe_success():
    var = MockVariable()
    vs = VariableService(var)
    vs.setVarUniverse([0, 10, 2])
    assert np.array_equal(var.varUniverse, np.arange(0, 10, 2))

def test_set_var_universe_fail():
    var = MockVariable()
    vs = VariableService(var)
    with pytest.raises(ValueError):
        vs.setVarUniverse([10, 5, 1])

def test_valid_member_param_trimf():
    var = MockVariable()
    var.mf_type = 'trimf'
    vs = VariableService(var)
    assert vs.isValidMemberParam(VALID_MEMBER_PARAMS_TRIMF) is True

def test_valid_member_param_trapmf():
    var = MockVariable()
    var.mf_type = 'trapmf'
    vs = VariableService(var)
    assert vs.isValidMemberParam(VALID_MEMBER_PARAMS_TRAPMF) is True

def test_invalid_member_param_wrong_order():
    var = MockVariable()
    var.mf_type = 'trimf'
    vs = VariableService(var)
    bad_params = [[3, 2, 1], [4, 5, 6]]
    assert vs.isValidMemberParam(bad_params) is False

def test_set_var_type_valid():
    var = MockVariable()
    vs = VariableService(var)
    vs.setVarType('antecedent')
    assert var.varType == 'antecedent'

def test_set_var_type_invalid():
    var = MockVariable()
    vs = VariableService(var)
    with pytest.raises(ValueError):
        vs.setVarType('invalid_type')

def test_initialize_variable_trimf():
    var = MockVariable()
    vs = VariableService(var)
    vs.initializeVariable(
        varParams=[0, 10, 1],
        memberParams=VALID_MEMBER_PARAMS_TRIMF,
        varType='antecedent',
        mf_type='trimf'
    )
    assert isinstance(var.fuzzy_variable, Antecedent)
    assert hasattr(var.fuzzy_variable, 'universe')

def test_initialize_variable_trapmf():
    var = MockVariable()
    vs = VariableService(var)
    vs.initializeVariable(
        varParams=[0, 10, 1],
        memberParams=VALID_MEMBER_PARAMS_TRAPMF,
        varType='consequent',
        mf_type='trapmf'
    )
    assert isinstance(var.fuzzy_variable, Consequent)
    assert hasattr(var.fuzzy_variable, 'universe')
