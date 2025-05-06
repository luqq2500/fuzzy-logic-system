import numpy as np

VARIABLES = [
    {
        'name': 'temperature',
        'variable_universe': np.arange(0, 41, 1),
        'membership_universe': {
            'low': [0, 0, 20, 25],
            'medium': [22, 26, 30, 34],
            'high': [30, 34, 40, 40]
        },
        'variable_type': 'antecedent',
        'membership_function': 'trapmf',
    },
    {
        'name': 'flood',
        'variable_universe': np.arange(0, 101, 1),
        'membership_universe': {
            'low': [0, 0, 20, 40],
            'medium': [30, 45, 55, 70],
            'high': [60, 75, 100, 100]
        },
        'variable_type': 'antecedent',
        'membership_function': 'trapmf'
    },
    {
        'name': 'population_density',
        'variable_universe': np.arange(0, 101, 1),
        'membership_universe': {
            'low': [0, 0, 20, 40],
            'medium': [30, 45, 55, 70],
            'high': [60, 75, 100, 100]
        },
        'variable_type': 'antecedent',
        'membership_function': 'trapmf'
    },
    {
        'name': 'socioeconomic_status',
        'variable_universe': np.arange(0, 101, 1),
        'membership_universe': {
            'low': [0, 0, 30, 50],
            'medium': [40, 55, 65, 80],
            'high': [70, 85, 100, 100]
        },
        'variable_type': 'antecedent',
        'membership_function': 'trapmf'
    },
    {
        'name': 'climate_risk',
        'variable_universe': np.arange(0, 101, 1),
        'membership_universe': {
            'low': [0, 0, 20, 40],
            'medium': [35, 50, 60, 75],
            'high': [70, 85, 100, 100]
        },
        'variable_type': 'consequent',
        'membership_function': 'trapmf'
    },
    {
        'name': 'social_vulnerability',
        'variable_universe': np.arange(0, 101, 1),
        'membership_universe': {
            'low': [0, 0, 25, 40],
            'medium': [35, 50, 60, 75],
            'high': [70, 85, 100, 100]
        },
        'variable_type': 'consequent',
        'membership_function': 'trapmf'
    },
    {
        'name': 'social_risk',
        'variable_universe': np.arange(0, 101, 1),
        'membership_universe': {
            'low': [0, 0, 20, 40],
            'medium': [35, 50, 60, 75],
            'high': [70, 85, 100, 100]
        },
        'variable_type': 'consequent',
        'membership_function': 'trapmf'
    }
]
