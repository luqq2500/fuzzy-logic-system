from models.rule import Rule
from config.configs import OPERATORS
from skfuzzy import control as controller

class RuleService:
    def __init__(self, name):
        self.rule = Rule(name)

    def setAntecedent(self, antecedent):
        var_mem1, string_logic, var_mem2 = antecedent
        logic = OPERATORS[string_logic]
        antecedent = logic(var_mem1, var_mem2)
        self.rule.antecedent = antecedent

    def setConsequent(self, variable):
        self.rule.consequent = variable

    def createRule(self):
        self.rule.rule = controller.Rule(self.rule.antecedent, self.rule.consequent)

    def getRule(self):
        return self.rule.rule


            