VARIABLES = {
    'temperature': {
        'name': 'temperature',
        'range': np.arange(0, 41, 1),
        'low': [0, 0, 20, 25],
        'medium': [22, 26, 30, 34],
        'high': [30, 34, 40, 40],
        'type': 'antecedent'
    },
    'flood': {
        'name': 'flood',
        'range': np.arange(0, 101, 1),
        'low': [0, 0, 20, 40],
        'medium': [30, 45, 55, 70],
        'high': [60, 75, 100, 100],
        'type': 'antecedent'
    },
    'population_density': {
        'name': 'population_density',
        'range': np.arange(0, 101, 1),
        'low': [0, 0, 20, 40],
        'medium': [30, 45, 55, 70],
        'high': [60, 75, 100, 100],
        'type': 'antecedent'
    },
    'socioeconomic_status': {
        'name': 'socioeconomic_status',
        'range': np.arange(0, 101, 1),
        'low': [0, 0, 30, 50],
        'medium': [40, 55, 65, 80],
        'high': [70, 85, 100, 100],
        'type': 'antecedent'
    },
    'climate_risk': {
        'name': 'climate_risk',
        'range': np.arange(0, 101, 1),
        'low': [0, 0, 20, 40],
        'medium': [35, 50, 60, 75],
        'high': [70, 85, 100, 100],
        'type': 'consequent'
    },
    'social_vulnerability': {
        'name': 'social_vulnerability',
        'range': np.arange(0, 101, 1),
        'low': [0, 0, 25, 40],
        'medium': [35, 50, 60, 75],
        'high': [70, 85, 100, 100],
        'type': 'consequent'
    },
    'social_risk': {
        'name': 'social_risk',
        'range': np.arange(0, 101, 1),
        'low': [0, 0, 20, 40],
        'medium': [35, 50, 60, 75],
        'high': [70, 85, 100, 100],
        'type': 'consequent'
    }
}
 