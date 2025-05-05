class Variable:
    def __init__(self, name):
        self.name = name
        self.varUniverse = ()
        self.memberUniverse = []
        self.fuzzy_variable = None
        self.varType = None
        self.mf_type = None
        self.membership = []

    def getVarName(self):
        return self.name

    def getVarUniverse(self):
        return self.varUniverse    

    def getMemberUniverse(self):
        return self.memberUniverse

    def getVarType(self):
        return self.varType

    def getMfType(self):
        return self.mf_type

    def getMembership(self):
        return self.membership
    
 
