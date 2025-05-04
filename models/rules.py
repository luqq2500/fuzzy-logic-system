class Rule:
    def __init__(self):
        self.antecedents = [] # [variable, ...]
        self.consequent = []
        self.rule = []
    
    def getAntecedents(self):
        return self.antecedents
    
    def getConsequent(self):
        return self.consequent
