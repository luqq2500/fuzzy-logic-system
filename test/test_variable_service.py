import pytest
from service.variable_service import VariableService
from config.configs import MEMBERSHIP_FUNCTIONS, VARIABLE_TYPE

pass_variable_param = (0, 101, 1)
pass_trimf_membership_params = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
pass_trapmf_membership_params = [[0, 2, 3, 4], [3, 4, 7, 8], [7, 8, 9, 10]]

fail_variable_type = 'sicko'
fail_variable_param = (100,50, 60.5)
fail_membership_function = 'i4u'
fail_trimf_membership_params = [[0, 1], [3, 5, 6], [9, 8]]
fail_trapmf_membership_params = [[0, 1, 2], [4, 3, 6, 7], [99, 9, 10, 11]]

@pytest.fixture
def variable_service():
    return VariableService('test')

def test_pass_createVariable(variable_service):
    for variable_type in VARIABLE_TYPE:
        variable_service.createVariable(pass_variable_param, variable_type)
    
def test_fail_createVariable(variable_service):
    for variable_type in VARIABLE_TYPE:
        with pytest.raises(ValueError):
            variable_service.createVariable(fail_variable_param, variable_type)
    
def test_pass_createMembership(variable_service):
    variable_service.createMembership(pass_trimf_membership_params, 'trimf')
    variable_service.createMembership(pass_trapmf_membership_params, 'trapmf')

def test_fail_createMembership(variable_service):
    with pytest.raises(ValueError):
        variable_service.createMembership(fail_trimf_membership_params, 'trimf')
        variable_service.createMembership(fail_trapmf_membership_params, 'trapmf')

def test_pass_getFuzzyVariable(variable_service):
    variable_service.createVariable(pass_variable_param, 'antecedent')
    variable_service.createMembership(pass_trimf_membership_params, 'trimf')
    return variable_service.getFuzzyVariable()

def test_fail_getFuzzyVariable(variable_service):
    assert variable_service.getFuzzyVariable() is None

def test_pass_setVarUniverse(variable_service):
    variable_service.setVarUniverse(pass_variable_param)

def test_fail_setVarUniverse(variable_service):
    with pytest.raises(ValueError):
        variable_service.setVarUniverse(fail_variable_param)

def test_pass_setMemberUniverse(variable_service):
    variable_service.setMfType('trimf')
    variable_service.setMemberUniverse(pass_trimf_membership_params)
    variable_service.setMfType('trapmf')
    variable_service.setMemberUniverse(pass_trapmf_membership_params)

def test_fail_setMemberUniverse(variable_service):
    with pytest.raises(ValueError):
        variable_service.setMfType('trimf')
        variable_service.setMemberUniverse(fail_trimf_membership_params)
        variable_service.setMfType('trapmf')
        variable_service.setMemberUniverse(fail_trapmf_membership_params)

def test_pass_setVarType(variable_service):
    for variable_type in VARIABLE_TYPE:
        variable_service.setVarType(variable_type)

def test_fail_setVarType(variable_service):
    with pytest.raises(ValueError):
        variable_service.setVarType(fail_variable_type)

def test_pass_setMfType(variable_service):
    for mf_type in MEMBERSHIP_FUNCTIONS:
        variable_service.setMfType(mf_type)

def test_fail_setMfType(variable_service):
    with pytest.raises(ValueError):
        variable_service.setMfType(fail_membership_function)
