'''
    This project is for the purpose of demonstration and hobby use. 
    The sensors and reading values have not been calibrated, and the data 
    presented should be used as a guide only.

'''

import board
import busio
from time import sleep


# constants: see data sheet for BH1750
# device address on I2C
BH1750_ADDR = 0x23

# device mode - see datasheet, this mode is recommended,
# measure duration is roughly 1.2ms
ONE_TIME_HIGH_RES_MODE_1 = 0x20

i2c = busio.I2C(board.SCL, board.SDA)

def get_data_light():
    '''
        returns tuple:
            (formatted string with value and units, scaled safety value)
    '''
    i2c.writeto(BH1750_ADDR, bytes([ONE_TIME_HIGH_RES_MODE_1]), stop=False)
    result = bytearray(2)
    i2c.readfrom_into(BH1750_ADDR, result)
    result_lux = (result[1] + (256 * result[0])) / 1.2
    safety_value = get_light_safety_value(result_lux)
    return (f"{result_lux} lx", safety_value)


def get_light_safety_value(value_lux):
    '''
        scales the data from safe to hazardous on interval [1,8]
        where 1=safe, 8=danger

        guide:
            https://www.ohsa.com.au/services/lighting-survey/

            Lighting in the general work areas must be of a level to enable work
            to be carried out safely.

            A value of 160 lux is recommended for general work areas. Office
            environments require more lighting, for example Moderately Difficult
            Visual Tasks (such as routine office work) should have a range of
            320-400 lux.

            This level should be considered as a minimum value when designing a
            lighting system. For more complex or intricate tasks, greater levels
            may be required.
    '''
    scaled_safety_value = 8
    if value_lux is None:
        return scaled_safety_value
    elif value_lux > 700:
        scaled_safety_value = 1
    elif value_lux > 300:
        scaled_safety_value = 2
    elif value_lux > 200:
        scaled_safety_value = 3
    elif value_lux > 100:
        scaled_safety_value = 4
    elif value_lux > 500:
        scaled_safety_value = 5
    elif value_lux > 25:
        scaled_safety_value = 6
    elif value_lux > 10:
        scaled_safety_value = 7
    else:
        scaled_safety_value = 8
    return scaled_safety_value
