import skfuzzy as fuzz
import skfuzzy.control as controller
from config.configs import OPERATORS
from service.rule_service import VariableService

class RuleService:
    def __init__(self, rule):
        self.rule = rule

    # antecedentParams = [var['ordinal], logic, var['ordinal']]
    def createRule(self, antecedentParams, consequent):
        self.rule.Rule = controlller.Rule(antecedentParams, conseqent)
        return self.rule.Rule