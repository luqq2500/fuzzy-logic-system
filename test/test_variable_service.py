import pytest
from service.variable_service import VariableService

@pytest.fixture
def variable_service():
    return VariableService()

def test_pass_initalizeFuzzyVariable(variable_service):
    name = 'pass'
    varParams = (0, 101, 1)
    memberParams = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
    varType = 'antecedent'
    mf_type = 'trimf'
    variable_service.initiateFuzzyVariable(name, varParams, memberParams, varType, mf_type)
    

def test_fail_initiateFuzzyVariable(variable_service):
    name = 'test_variable'
    varParams = (2, 5, 20)
    memberParams = [[3, 4, 5], [8, 7, 6, 9], [9, 8, 7, 6]]
    varType = 'none'
    mf_type = 'trimf'
    with pytest.raises(ValueError):
        variable_service.initiateFuzzyVariable(name, varParams, memberParams, varType, mf_type)

def test_pass_createVariable(variable_service):
    variable_service.createVariable('pass')
    
def test_pass_createFuzzyVariable(variable_service):
    variable_service.createVariable('pass')
    varParams = (0,101,1)
    varType = 'consequent'
    variable_service.createFuzzyVariable(varParams, varType)
    
def test_fail_createFuzzyVariable(variable_service):
    variable_service.createVariable('pass')
    varParams = (100, 1, 3)
    varType = 'none'
    with pytest.raises(ValueError):
        variable_service.createFuzzyVariable(varParams, varType)

def test_pass_createMembership(variable_service):
    variable_service.createVariable('test')
    variable_service.setVarType('antecedent')
    variable_service.setVarUniverse((0, 10, 1))
    variable_service.createFuzzyVariable((0, 10, 1), 'antecedent')

    trimfParams = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
    variable_service.createMembership(trimfParams, 'trimf')

    trapmfParams = [[0, 2, 3, 4], [3, 4, 7, 8], [7, 8, 9, 10]]
    variable_service.createMembership(trapmfParams, 'trapmf')

    assert len(variable_service.variable.membership) > 0

def test_fail_createMembership(variable_service):
    variable_service.createVariable('fail')
    variable_service.setVarType('antecedent')
    variable_service.setVarUniverse((0, 10, 1))
    variable_service.createFuzzyVariable((0, 10, 1), 'antecedent')

    invalidParams = [[100, 1, 10], [0, 77, 71], [0, 9, 8, 7]]
    with pytest.raises(ValueError):
        variable_service.createMembership(invalidParams, 'trimf')
