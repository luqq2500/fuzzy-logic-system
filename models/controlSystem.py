class ControlSystem:
    def __init__(self, name):
        self.name = name
        self.variables = []
        self.rules = []
        self.controlSystem = None
        self.controlSystemSimulation = None
        self.inputs = []
        self.output = None

    def getName(self):
        return self.name

    def getRules(self):
        return self.rules

    def getControlSystem(self):
        return self.controlSystem

    def getControlSystemSimulation(self):
        return self.controlSystemSimulation

    def getInputs(self):
        return self.inputs

    def getOutput(self):
        return self.output
