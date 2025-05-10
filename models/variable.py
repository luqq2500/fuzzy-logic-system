class Variable:
    def __init__(self, name):
        self.name = name
        self.variable_universe = ()
        self.variable_type = None
        self.membership_universe = []
        self.mf_type = None
        self.fuzzy_variable = None
        self.membership = []

    def getVarName(self):
        return self.name

    def getVarUniverse(self):
        return self.variable_universe

    def getMemberUniverse(self):
        return self.membership_universe

    def getFuzzyVariable(self):
        return self.fuzzy_variable

    def getVarType(self):
        return self.variable_type

    def getMfType(self):
        return self.mf_type

    def getMembership(self):
        return self.membership
    
 
