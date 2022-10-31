'''
    This project is for the purpose of demonstration and hobby use. 
    The sensors and reading values have not been calibrated, and the data 
    presented should be used as a guide only.

'''

import busio
import board
import adafruit_sgp30


i2c_bus = busio.I2C(board.SCL, board.SDA, frequency=100000)
airq_sensor_sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)


def get_data_co2():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    # measures twice, but code understandable and matches patterns.. hhmmm...
    eCO2, _ = airq_sensor_sgp30.iaq_measure()
    safety_value = get_co2_safety_value(eCO2)
    return (f"{eCO2}ppm", safety_value)


def get_co2_safety_value(eCO2):
    '''
        scales the data from safe to hazardous on interval [1,8] 
        where 1=safe 8=danger
        
        guide is.. well.. we're already at 400ppm which isn't great
        however....
        
        guide:
            https://www.fsis.usda.gov/sites/default/files/media_file/2020-08/Carbon-Dioxide.pdf

            The American Conference of Governmental Industrial Hygienists (ACGIH)
            recommends an 8- hour TWA Threshold Limit Value (TLV) of 5,000 ppm
            and a Ceiling exposure limit (not to be exceeded) of 30,000 ppm for
            a 10-minute period. A value of 40,000 is considered immediately
            dangerous to life and health (IDLH value).

            ..given the above we might fiddle with this a little, and presume
            to adjust the scale non-linearly to give the user feedback with
            immediate moves in the level, and then graduated further on..
            
    '''
    scaled_safety_value = 8
    if eCO2 is None:
        return scaled_safety_value
    elif eCO2 > 2000:
        scaled_safety_value = 8
    elif eCO2 > 1000:
        scaled_safety_value = 7
    elif eCO2 > 500:
        scaled_safety_value = 6
    elif eCO2 > 450:
        scaled_safety_value = 5
    elif eCO2 > 425:
        scaled_safety_value = 4
    elif eCO2 > 410:
        scaled_safety_value = 3
    elif eCO2 > 405:
        scaled_safety_value = 2
    else:
        scaled_safety_value = 1
    return scaled_safety_value


def get_data_tvoc():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    _, tvoc = airq_sensor_sgp30.iaq_measure()
    safety_value = get_tvoc_safety_value(tvoc)
    return (f"{tvoc}", safety_value)


def get_tvoc_safety_value(tvoc):
    '''
        scales the data from safe to hazardous on interval [1,8] 
        where 1=safe 8=danger

        guide:
            https://www.ibm.com/docs/en/mwi?topic=shields-air-quality-shield
        
            Total volatile organic compounds (TVOC), which is measured in parts
            per billion (ppb). TVOC is used to estimate the total Volatile
            Organic Compounds (VOC) that are present simultaneously in the air.
            Detecting TVOC in the 220 ppb to 660 ppb range indicate poor
            ventilation efficiency. Environment with TVOC readings in the
            2,200 ppb to 5,500 ppb range are considered unhealthy and require
            intense ventilation.
    '''
    scaled_safety_value = 8
    if tvoc is None:
        return scaled_safety_value
    elif tvoc > 2000:
        scaled_safety_value = 8
    elif tvoc > 1000:
        scaled_safety_value = 7
    elif tvoc > 500:
        scaled_safety_value = 6
    elif tvoc > 250:
        scaled_safety_value = 5
    elif tvoc > 125:
        scaled_safety_value = 4
    elif tvoc > 60:
        scaled_safety_value = 3
    elif tvoc > 30:
        scaled_safety_value = 2
    else:
        scaled_safety_value = 1
    return scaled_safety_value
