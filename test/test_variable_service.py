import pytest
import numpy as np
import skfuzzy.control as controller

from service.variable_service import VariableService
from models.variable import Variable
from config.configs import VARIABLE_MEMBERSHIP_ORDINALS, MEMBERSHIP_FUNCTIONS, VARIABLE_TYPE

@pytest.fixture
def variable_service():
    return VariableService()

def test_initiateFuzzyVariable(variable_service):
    name = "test_variable"
    varParams = [0, 10, 1]
    memberParams = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
    varType = "antecedent"
    mf_type = "trimf"

    variable = variable_service.initiateFuzzyVariable(
        name, varParams, memberParams, varType, mf_type
    )

    assert variable.getVarName() == name
    assert variable.getVarType() == varType
    assert variable.getMfType() == mf_type
    assert isinstance(variable.fuzzy_variable, controller.Antecedent)
    assert len(variable.membership) == len(VARIABLE_MEMBERSHIP_ORDINALS)

def test_createVariable(variable_service):
    variable_service.createVariable("test_variable")
    assert isinstance(variable_service.variable, Variable)
    assert variable_service.variable.getVarName() == "test_variable"

def test_createFuzzyVariable_antecedent(variable_service):
    varParams = [0, 10, 1]
    varType = "antecedent"
    variable_service.createVariable("test_variable")
    variable_service.createFuzzyVariable(varParams, varType)
    assert isinstance(variable_service.variable.fuzzy_variable, controller.Antecedent)

def test_createFuzzyVariable_consequent(variable_service):
    varParams = [0, 10, 1]
    varType = "consequent"
    variable_service.createVariable("test_variable")
    variable_service.createFuzzyVariable(varParams, varType)
    assert isinstance(variable_service.variable.fuzzy_variable, controller.Consequent)

def test_createMembership(variable_service):
    # You must set mf_type on the variable before creating membership
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")
    variable_service.createFuzzyVariable([0, 10, 1], "antecedent")

    memberParams = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
    mf_type = "trimf"
    variable_service.createMembership(memberParams, mf_type)

    assert len(variable_service.variable.membership) == len(memberParams)

def test_setVarUniverse_valid(variable_service):
    variable_service.createVariable("test_variable")
    params = [0, 10, 1]
    variable_service.setVarUniverse(params)
    np.testing.assert_array_equal(
        variable_service.variable.varUniverse,
        np.arange(0, 10, 1)
    )

def test_setVarUniverse_invalid(variable_service):
    variable_service.createVariable("test_variable")
    with pytest.raises(ValueError):
        variable_service.setVarUniverse([10, 0, 1])

def test_setMemberUniverse_valid(variable_service):
    # Must set mf_type before validating membership universe
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")

    params = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
    variable_service.setMemberUniverse(params)
    assert variable_service.variable.memberUniverse == params

def test_setMemberUniverse_invalid(variable_service):
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")
    with pytest.raises(ValueError):
        # wrong lengths vs EXPECTED_MF_LENGTH
        variable_service.setMemberUniverse([[0,1], [1,2], [2,3]])

def test_setVarType_valid(variable_service):
    variable_service.createVariable("test_variable")
    variable_service.setVarType("antecedent")
    assert variable_service.variable.varType == "antecedent"

def test_setVarType_invalid(variable_service):
    variable_service.createVariable("test_variable")
    with pytest.raises(ValueError):
        variable_service.setVarType("invalidType")

def test_setMfType_valid(variable_service):
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")
    assert variable_service.variable.mf_type == "trimf"

def test_setMfType_invalid(variable_service):
    variable_service.createVariable("test_variable")
    with pytest.raises(ValueError):
        variable_service.setMfType("invalidMf")

def test_isValidVarParam_valid(variable_service):
    assert variable_service.isValidVarParam([0, 10, 1])

def test_isValidVarParam_invalid_length(variable_service):
    with pytest.raises(ValueError):
        variable_service.isValidVarParam([0, 10])

def test_isValidVarParam_invalid_range(variable_service):
    with pytest.raises(ValueError):
        variable_service.isValidVarParam([10, 0, 1])

def test_isValidVarParam_invalid_step_size(variable_service):
    with pytest.raises(ValueError):
        variable_service.isValidVarParam([0, 10, 15])

def test_isValidMemberParam_valid(variable_service):
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")
    params = [[0, 3, 6], [3, 6, 9], [6, 9, 10]]
    assert variable_service.isValidMemberParam(params)

def test_isValidMemberParam_invalid_length(variable_service):
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")
    with pytest.raises(ValueError):
        variable_service.isValidMemberParam([[0, 3, 6], [3, 6, 9]])

def test_isValidMemberParam_invalid_order(variable_service):
    variable_service.createVariable("test_variable")
    variable_service.setMfType("trimf")
    with pytest.raises(ValueError):
        variable_service.isValidMemberParam([[0, 6, 3], [3, 6, 9], [6, 9, 10]])

def test_isValidVarType_invalid(variable_service):
    with pytest.raises(ValueError):
        variable_service.isValidVarType("invalidType")

def test_isValidMfType_invalid(variable_service):
    with pytest.raises(ValueError):
        variable_service.isValidMfType("invalidMf")
