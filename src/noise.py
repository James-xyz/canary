'''
    This project is for the purpose of demonstration and hobby use. 
    The sensors and reading values have not been calibrated, and the data 
    presented should be used as a guide only.

'''

from gpiozero import MCP3008
from random import randint


noise_sensor = MCP3008(channel=0, clock_pin=18, mosi_pin=24, miso_pin=23, select_pin=25)
# noise_sensor = MCP3008(channel=1, clock_pin=18, mosi_pin=24, miso_pin=23, select_pin=25)
# noise_sensor = MCP3008(channel=2, clock_pin=18, mosi_pin=24, miso_pin=23, select_pin=25)


def get_data_noise():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    noise = int(noise_sensor.value * 100)
    ## issues with sound detector and ADC
    safety_value = get_noise_safety_value(noise)
    return (f"{noise}", safety_value)

def get_noise_safety_value(noise_data):
    '''
        scales the data from safe to hazardous on interval [1,8] 
        where 1=safe 8=danger

        There is no reference here due to limitations with calibrating the sensor
        therefore the safety levels are simply 'wet finger in the air' values,
        guided by tasks I'd usually wear hearing protection for eg. impact driver
    '''
    # need to test and tune this too.
    return randint(0,8)
