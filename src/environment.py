'''
    This project is for the purpose of demonstration and hobby use. 
    The sensors and reading values have not been calibrated, and the data 
    presented should be used as a guide only.

'''

from PiicoDev_BME280 import PiicoDev_BME280

environment_sensor = PiicoDev_BME280() 


def get_data_temp():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    tempC, _, _ = environment_sensor.values() # read all data from the sensor
    safety_value = get_temp_safety_value(tempC)
    return (f"{tempC}°C", safety_value)


def get_temp_safety_value(temp):
    '''
        guide:
            wet finger in the air, based on experience and commonsense..
    '''
    scaled_safety_value = 8
    if temp is None:
        return scaled_safety_value
    elif temp > 45 or temp < 0:
        scaled_safety_value = 8
    elif temp > 40 or temp < 3:
        scaled_safety_value = 7
    elif temp > 37 or temp < 5:
        scaled_safety_value = 6
    elif temp > 35 or temp < 8:
        scaled_safety_value = 5
    elif temp > 33 or temp < 10:
        scaled_safety_value = 4
    elif temp > 30 or temp < 12:
        scaled_safety_value = 3
    elif temp > 27 or temp < 14:
        scaled_safety_value = 2
    else:
        scaled_safety_value = 1
    return scaled_safety_value


def get_data_pressure():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    _, presPa, _ = environment_sensor.values() # read all data from the sensor
    safety_value = get_pressure_safety_value(presPa)
    return (f"{presPa/100} hPa", safety_value)


def get_pressure_safety_value(pressure):
    '''
        having barometric pressure measurement was a bonus, but I have since
        discovered that it can effect health (according to the internet:
        https://www.linkedin.com/pulse/5-effects-barometric-pressure-has-humans-you-really-can-pedram-shojai/)
        so we might take a stab in the dark and ascribe some safety values to
        the pressure as well. To be really effective this should look at rates
        of change I suppose, but here we can probably just do a delta to average
        pressure?
    
        1,013.25 hPa is one atm (mean pressure at sea level:
            https://en.wikipedia.org/wiki/Atmospheric_pressure)

        1084.8 hPa is highest (adjusted-to-sea level barometric pressure)
        recorded, and
        The lowest non-tornadic atmospheric pressure ever measured was 870 hPa

        again with the wet finger in the air, below values may need to be
        adjusted, but the main point is that the value cahnges the display and
        warrants notice by user..

    '''
    scaled_safety_value = 8
    if pressure is None:
        return scaled_safety_value
    pressure = pressure / 100 # convert to hPa
    if   pressure > 1040 or pressure < 940:
        scaled_safety_value = 8
    elif pressure > 1035 or pressure < 950:
        scaled_safety_value = 7
    elif pressure > 1030 or pressure < 970:
        scaled_safety_value = 6
    elif pressure > 1025 or pressure < 975:
        scaled_safety_value = 5
    elif pressure > 1021 or pressure < 980:
        scaled_safety_value = 4
    elif pressure > 1018 or pressure < 1008:
        scaled_safety_value = 3
    elif pressure > 1015 or pressure < 1011:
        scaled_safety_value = 2
    else:
        scaled_safety_value = 1
    return scaled_safety_value


def get_data_humidity():
    '''
        returns tuple: 
            (formatted string with value and units, scaled saftey value)
    '''
    _, _, humRH = environment_sensor.values() # read all data from the sensor
    safety_value = get_humidity_safety_value(humRH)
    return (f"{humRH} rel. humidity", safety_value)


def get_humidity_safety_value(humidity):
    '''
        guide:
            https://www.nationalasthma.org.au/news/2016/indoor-humidity
            Most people find that a relative humidity between 30 to 60 percent
            is the most comfortable, with indoor humidity ideally between 30 to
            50 percent.
            low: 25
            OK: 30 - 50
            high: 60+
    '''
    scaled_safety_value = 8
    if humidity is None:
        return scaled_safety_value
    elif humidity > 80 or humidity < 25:
        scaled_safety_value = 8
    elif humidity > 70 or humidity < 27:
        scaled_safety_value = 7
    elif humidity > 60 or humidity < 30:
        scaled_safety_value = 6
    elif humidity > 55 or humidity < 32:
        scaled_safety_value = 5
    elif humidity > 50 or humidity < 34:
        scaled_safety_value = 4
    elif humidity > 45 or humidity < 36:
        scaled_safety_value = 3
    elif humidity > 40 or humidity < 38:
        scaled_safety_value = 2
    else:
        scaled_safety_value = 1
    return scaled_safety_value
