import skfuzzy.control as controller
from models.controlSystem import ControlSystem

class ControlSystemService:
    def __init__(self, variable_service):
        self.variable_service = variable_service
        self.controlSystem = None

    # ============ C O R E ============== #
    def createControlSystem(self, name, variables, rules):
        self.startControlSystem(name)
        self.setVariables(variables)
        self.setControlSystemRules(rules)
        self.controlSystem.controlSystem = controller.ControlSystem(self.controlSystem.rules)
        self.controlSystem.controlSystemSimulation = controller.ControlSystemSimulation(self.controlSystem.controlSystem)
        return self.controlSystem

    def setInputControlSystem(self, simulation, tupleVariableNameValue):
        for variable_name, value in tupleVariableNameValue:
            if self.isInputVariableValid(variable_name):
                simulation.input[variable_name] = value
                self.controlSystem.inputs.append({variable_name: value})

    def compute(self):
        self.controlSystem.controlSystemSimulation.compute()

    def getComputeResult(self):
        variableName = self.controlSystem.name
        return self.controlSystem.controlSystemSimulation.output[variableName]

    def startControlSystem(self, name):
        self.controlSystem = ControlSystem(name)


    # ====== S E T T E R ====== #
    def setVariables(self, variables):
        for variable in variables:
            self.controlSystem.variables.append(variable)

    def setControlSystemRules(self, rules):
        for rule in rules:
            self.controlSystem.rules.append(rule)

    def setControlSystemSimulation(self):
        controlSystem = self.controlSystem.controlSystem
        self.controlSystem.controlSystemSimulation = controller.ControlSystemSimulation(controlSystem)


    # ====== V A L I D A T I O N ====== #
    def isInputVariableValid(self, variable_name):
        for variable in self.controlSystem.variables:
            if self.variable_service.getVariableByName(variable_name) == variable:
                return True
        return False