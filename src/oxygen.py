'''
    This project is for the purpose of demonstration and hobby use. 
    The sensors and reading values have not been calibrated, and the data 
    presented should be used as a guide only.

'''

import lib.O2 as O2

O2_ADDR = 0x73

oxygen_sensor = O2.DFRobot_Oxygen_IIC(1, O2_ADDR)


def get_data_oxygen():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    oxygen_data = oxygen_sensor.get_oxygen_data(1)
    safety_value = get_oxygen_safety_value(oxygen_data)
    return (f"{oxygen_data}%", safety_value)

def get_oxygen_safety_value(oxygen_data):
    '''
        scales the data from safe to hazardous on interval [1,8] 
        where 1=safe 8=danger
        
        guide:
            https://www.cacgas.com.au/blog/bid/378107/oxygen-o2-occupational-health-exposure-standards

            Concetration of Oxygen (v/v)
            Effects                                                                                      
            20.9% 	 Oxygen concentration of Air
            19.5% 	 Minimum "Safe Level"
            17.0% 	 Impairment of judgement starts to be detected
            16.0% 	 First signs of anoxia (dizziness, light-headedness)
            16%-12%  Breathing and pulse rate increases, muscular co-ordination 
                     starts to beome impaired
            14%-10%  Consciousness continuous, abormal fatigue and distrubed 
                     respiration
            10%-6% 	 Nausea, vomiting, inability to move freely and loss of 
                     consciousness may occur
            <6% 	 Convulsive movements and gasping respiration occurs, 
                     respiration stops and a few minutes later heart action 
                     ceases.
    '''
    # default to unsafe value if sensor not working
    scaled_safety_value = 8 
    if oxygen_data is None:
        return scaled_safety_value
    elif oxygen_data > 20.8:
        scaled_safety_value = 1
    elif oxygen_data > 20:
        scaled_safety_value = 2
    elif oxygen_data > 19.5:
        scaled_safety_value = 3
    else:
        scaled_safety_value = 8
    return scaled_safety_value
