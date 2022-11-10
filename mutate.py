import numpy as np 
import random
validModels= ["Model 1", "Model 2", "Model 3", "Model 4", "Model 5", "Model 6"]
validPlateNumbers = ['AAA2BBB', 'QQQ3ZZ']
validColors = ['red', 'green', 'white', 'silver', 'grey', 'beige', 'blue', 'black']
validWheathers= ['Cloudy', 'Sunny']

def data_mutate(data):
    data['GeneralSettings']['EnvironmentSettings']['Weather'] =         mutate(data['GeneralSettings']['EnvironmentSettings']['Weather'], 'Weather')
    data['GeneralSettings']['EnvironmentSettings']['Precipitation'] =   mutate(data['GeneralSettings']['EnvironmentSettings']['Precipitation'], 'float', 0 , 1)
    data['GeneralSettings']['EnvironmentSettings']['Hour'] =            mutate(data['GeneralSettings']['EnvironmentSettings']['Hour'], 'int', 8, 18)
    data['GeneralSettings']['EnvironmentSettings']['Minute'] =            mutate(data['GeneralSettings']['EnvironmentSettings']['Minute'], 'int', 0, 60)
    
    # data['GeneralSettings']['SensorSettings']['Camera']['Aperture'] =   mutate(data['GeneralSettings']['SensorSettings']['Camera']['Aperture'], 'float', 0 , 10)
    # data['GeneralSettings']['SensorSettings']['Camera']['FocalLength'] =   mutate(data['GeneralSettings']['SensorSettings']['Camera']['FocalLength'], 'float', 0 , 10)
    # data['GeneralSettings']['SensorSettings']['Camera']['Exposure'] =   mutate(data['GeneralSettings']['SensorSettings']['Camera']['Exposure'], 'float', 0 , 10)
    # data['GeneralSettings']['SensorSettings']['Camera']['ShutterSpeed'] =   mutate(data['GeneralSettings']['SensorSettings']['Camera']['ShutterSpeed'], 'float', 0 , 10)
    # data['GeneralSettings']['SensorSettings']['Camera']['Iso'] =   mutate(data['GeneralSettings']['SensorSettings']['Camera']['Iso'], 'float', 0 , 10)
    # data['GeneralSettings']['SensorSettings']['Camera']['Fov'] =   mutate(data['GeneralSettings']['SensorSettings']['Camera']['Fov'], 'float', 0 , 10)
        
    # for i in range(0,len(data['GeneralSettings']['SensorSettings']['Viewpoints'])):
        # data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Position']['X'] =   mutate(data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Position']['X'], 'float', 0 , 10)
        # data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Position']['Y'] =   mutate(data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Position']['Y'], 'float', 0 , 10)
        # data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Position']['Z'] =   mutate(data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Position']['Z'], 'float', 0 , 10)
        # data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Rotation']['Roll'] =   mutate(data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Rotation']['Roll'], 'float', 0 , 10)
        # data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Rotation']['Pitch'] =   mutate(data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Rotation']['Pitch'], 'float', 0 , 10)
        # data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Rotation']['Yaw'] =   mutate(data['GeneralSettings']['SensorSettings']['Viewpoints'][i]['Rotation']['Yaw'], 'float', 0 , 10)
    
    for i in range(0,len(data['ScenarioActors']['Navigation']['Waypoints'])):
        data['ScenarioActors']['Navigation']['Waypoints'][i]['Position']['X'] =   mutate(data['ScenarioActors']['Navigation']['Waypoints'][i]['Position']['X'], 'float', 0 , 10)
        data['ScenarioActors']['Navigation']['Waypoints'][i]['Position']['Y'] =   mutate(data['ScenarioActors']['Navigation']['Waypoints'][i]['Position']['Y'], 'float', 0 , 10)
        data['ScenarioActors']['Navigation']['Waypoints'][i]['Position']['Z'] =   mutate(data['ScenarioActors']['Navigation']['Waypoints'][i]['Position']['Z'], 'float', 0 , 10)
        data['ScenarioActors']['Navigation']['Waypoints'][i]['Rotation']['Roll'] =   mutate(data['ScenarioActors']['Navigation']['Waypoints'][i]['Rotation']['Roll'], 'float', 0 , 10)
        data['ScenarioActors']['Navigation']['Waypoints'][i]['Rotation']['Pitch'] =   mutate(data['ScenarioActors']['Navigation']['Waypoints'][i]['Rotation']['Pitch'], 'float', 0 , 10)
        data['ScenarioActors']['Navigation']['Waypoints'][i]['Rotation']['Yaw'] =   mutate(data['ScenarioActors']['Navigation']['Waypoints'][i]['Rotation']['Yaw'], 'float', 0 , 10)

    for i in range(0,len(data['ScenarioActors']['Dynamic']['Vehicles'])):    
        data['ScenarioActors']['Dynamic']['Vehicles'][i]['LicensePlate']['PlateNumber'] = mutate(data['ScenarioActors']['Dynamic']['Vehicles'][i]['LicensePlate']['PlateNumber'], 'PlateNumber')
        data['ScenarioActors']['Dynamic']['Vehicles'][i]['ClassToSpawn'] = mutate(data['ScenarioActors']['Dynamic']['Vehicles'][i]['ClassToSpawn'], 'ClassToSpawn')
        data['ScenarioActors']['Dynamic']['Vehicles'][i]['Model'] = mutate(data['ScenarioActors']['Dynamic']['Vehicles'][i]['Model'], 'Model')
        data['ScenarioActors']['Dynamic']['Vehicles'][i]['Color'] = mutate(data['ScenarioActors']['Dynamic']['Vehicles'][i]['Color'], 'Color')
        data['ScenarioActors']['Dynamic']['Vehicles'][i]['MaxSpeed'] = mutate(data['ScenarioActors']['Dynamic']['Vehicles'][i]['MaxSpeed'], 'int', 15, 20)

    for i in range(0,len(data['ScenarioActors']['Lights']['SpotLights'])):    
        data['ScenarioActors']['Lights']['SpotLights'][i]['Position']['X'] =   mutate(data['ScenarioActors']['Lights']['SpotLights'][i]['Position']['X'], 'float', 0 , 10)
        data['ScenarioActors']['Lights']['SpotLights'][i]['Position']['Y'] =   mutate(data['ScenarioActors']['Lights']['SpotLights'][i]['Position']['Y'], 'float', 0 , 10)
        data['ScenarioActors']['Lights']['SpotLights'][i]['Position']['Z'] =   mutate(data['ScenarioActors']['Lights']['SpotLights'][i]['Position']['Z'], 'float', 0 , 10)
        data['ScenarioActors']['Lights']['SpotLights'][i]['Rotation']['Roll'] =   mutate(data['ScenarioActors']['Lights']['SpotLights'][i]['Rotation']['Roll'], 'float', 0 , 10)
        data['ScenarioActors']['Lights']['SpotLights'][i]['Rotation']['Pitch'] =   mutate(data['ScenarioActors']['Lights']['SpotLights'][i]['Rotation']['Pitch'], 'float', 0 , 10)
        data['ScenarioActors']['Lights']['SpotLights'][i]['Rotation']['Yaw'] =   mutate(data['ScenarioActors']['Lights']['SpotLights'][i]['Rotation']['Yaw'], 'float', 0 , 10)
        
    return data

def mutate(value, vtype, rangemin=None, rangemax=None):
    try:
        scale = (rangemax - rangemin )/2
    except:
        scale = 1
        
    if vtype == 'float':
        return int(np.random.normal(value, int(scale)))
    if vtype == 'int':
        return random.randint(rangemin, rangemax)
    if vtype == 'Model':
        return value # random.choice(validModels)
    if vtype == 'PlateNumber':
        return random.choice(validPlateNumbers)
    if vtype == 'Color':
        return random.choice(validColors)
    return value