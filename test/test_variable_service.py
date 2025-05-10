import pytest
from service.variable_service import VariableService
from config.configs import MEMBERSHIP_FUNCTIONS

@pytest.fixture
def variable_service():
    return VariableService('test')

def test_pass_createVariable(variable_service):
    varParams = (0, 101, 1)
    varType = 'antecedent'
    variable_service.createVariable(varParams, varType)
    
def test_fail_createVariable(variable_service):
    varParams = (2, 5, 20)
    varType = 'none'
    with pytest.raises(ValueError):
        variable_service.createVariable(varParams,varType)
    
def test_pass_createMembership(variable_service):
    variable_service.createVariable((0, 101, 1), 'antecedent')
    memberParams = [[[0, 3, 6], [3, 6, 9], [6, 9, 10]], [[0, 2, 3, 4], [3, 4, 7, 8], [7, 8, 9, 10]]]
    for params, mf_type in zip(memberParams, MEMBERSHIP_FUNCTIONS):
        variable_service.createMembership(params, mf_type)

def test_fail_createMembership(variable_service):
    variable_service.createVariable((0, 101, 1), 'antecedent')
    invalidParams = [[100, 1, 10], [0, 77, 71], [0, 9, 8, 7]]
    with pytest.raises(ValueError):
        variable_service.createMembership(invalidParams, 'trimf')