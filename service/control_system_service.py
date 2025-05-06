import skfuzzy.control as controller
from models.controlSystem import ControlSystem
from service.variable_service import VariableService

variable_service = VariableService()

class ControlSystemService:
    def __init__(self):
        self.controlSystem = None
        self.controlSystems = {}

    def startControlSystem(self, name):
        self.controlSystem = ControlSystem(name)

    # take set of variable objects: (var, var)
    def setVariable(self, variable):
        self.controlSystem.variables.append(variable)

    def setControlSystemRules(self, rules):
        for rule in rules:
            self.controlSystem.rules.append(rule)

    def setControlSystem(self):
        rules = self.controlSystem.rules
        self.controlSystem.controlSystem = controller.ControlSystem(rules)

    def setControlSystemSimulation(self):
        controlSystem = self.controlSystem.controlSystem
        self.controlSystem.controlSystemSimulation = controller.ControlSystemSimulation(controlSystem)

    # parameter: list of tuples (variable_name, int)
    def setInputControlSystem(self, variableObjectAndValueList):
        simulation = self.controlSystem.controlSystemSimulation
        for variable_name, value in variableObjectAndValueList:
            if self.isInputVariableValid(variable_name):
                simulation.input[variable_name] = value
                self.controlSystem.inputs.append({variable_name: value})

    def isInputVariableValid(self, variable_name):
        for variable in self.controlSystem.variables:
            if variable_service.getVariableByName(variable_name) == variable:
                return True
        return False

    def compute(self):
        self.controlSystem.controlSystemSimulation.compute()

    def getComputeResult(self, variableName):
        if not variable_service.getVariableByName(variableName):
            raise ValueError(f'Variable {variableName} does not exist')
        if self.controlSystem.controlSystemSimulation.output[variableName] is None:
            raise ValueError(f'Result for variable {variableName} does not exist')
        return self.controlSystem.controlSystemSimulation.output(variableName)