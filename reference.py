

# 1. Define variables & rules (use your VariableService)
# Assume you’ve created fuzzy vars for all of them using your service

# SYSTEM 1: temperature + flood → climate_risk
rule1 = ctrl.Rule(antecedent=(temperature['high'] & flood['high']), consequent=climate_risk['high'])
rule2 = ctrl.Rule(antecedent=(temperature['low'] & flood['low']), consequent=climate_risk['low'])
climate_ctrl = ctrl.ControlSystem([rule1, rule2])
climate_sim = ctrl.ControlSystemSimulation(climate_ctrl)

climate_sim.input['temperature'] = 36
climate_sim.input['flood'] = 80
climate_sim.compute()
climate_risk_output = climate_sim.output['climate_risk']
print("climate_risk:", climate_risk_output)


# SYSTEM 2: population_density + socioeconomic_status → social_vulnerability
rule3 = ctrl.Rule((population_density['high'] & socioeconomic_status['low']), social_vulnerability['high'])
rule4 = ctrl.Rule((population_density['low'] & socioeconomic_status['high']), social_vulnerability['low'])
social_vuln_ctrl = ctrl.ControlSystem([rule3, rule4])
social_vuln_sim = ctrl.ControlSystemSimulation(social_vuln_ctrl)

social_vuln_sim.input['population_density'] = 85
social_vuln_sim.input['socioeconomic_status'] = 30
social_vuln_sim.compute()
social_vulnerability_output = social_vuln_sim.output['social_vulnerability']
print("social_vulnerability:", social_vulnerability_output)


# SYSTEM 3: climate_risk + social_vulnerability → social_risk
rule5 = ctrl.Rule((climate_risk['high'] & social_vulnerability['high']), social_risk['high'])
rule6 = ctrl.Rule((climate_risk['low'] & social_vulnerability['low']), social_risk['low'])
social_risk_ctrl = ctrl.ControlSystem([rule5, rule6])
social_risk_sim = ctrl.ControlSystemSimulation(social_risk_ctrl)

# Chain outputs from previous systems
social_risk_sim.input['climate_risk'] = climate_risk_output
social_risk_sim.input['social_vulnerability'] = social_vulnerability_output
social_risk_sim.compute()
print("social_risk:", social_risk_sim.output['social_risk'])