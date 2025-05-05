import operator
VARIABLE_MEMBERSHIP_ORDINALS = ['low','medium','high']

VARIABLE_TYPE = ['antecedent', 'consequent']

MEMBERSHIP_FUNCTIONS = ['trimf', 'trapmf']

OPERATORS = {
    '&': operator.and_,
    '|': operator.or_
}

EXPECTED_MF_LENGTH = {'trimf': 3, 'trapmf': 4}
