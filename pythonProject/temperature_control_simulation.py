import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperature = np.arange(0, 101, 1)
temperature_var = ctrl.Antecedent(temperature, 'Temperature')
temperature_var['Cold'] = fuzz.trimf(temperature, [0, 0, 50])
temperature_var['Comfortable'] = fuzz.trimf(temperature, [0, 50, 100])
temperature_var['Hot'] = fuzz.trimf(temperature, [50, 100, 100])

control_action = np.arange(0, 101, 1)
control_action_var = ctrl.Consequent(control_action, 'Control Action')
control_action_var['Decrease Heating'] = fuzz.trimf(control_action, [0, 0, 50])
control_action_var['Maintain Temperature'] = fuzz.trimf(control_action, [0, 50, 100])
control_action_var['Increase Cooling'] = fuzz.trimf(control_action, [50, 100, 100])

rule1 = ctrl.Rule(temperature_var['Cold'], control_action_var['Increase Cooling'])
rule2 = ctrl.Rule(temperature_var['Comfortable'], control_action_var['Maintain Temperature'])
rule3 = ctrl.Rule(temperature_var['Hot'], control_action_var['Decrease Heating'])

fis_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fuzzy_system = ctrl.ControlSystemSimulation(fis_ctrl)

temperature_data = [20, 45, 70, 95]

for temp in temperature_data:
    fuzzy_system.input['Temperature'] = temp
    fuzzy_system.compute()
    print("Temperature:", temp, "-> Control Action:", fuzzy_system.output['Control Action'])
