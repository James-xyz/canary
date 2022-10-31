'''
    this should be the program that runs by default when device is booted.
'''

import oxygen as oxygen_sensor
import light as light_sensor
import noise as noise_sensor
import air_quality as aq_sensor
import environment as env_sensor

import os

import matrix
from time import sleep

# fireworks startup procedure
matrix.startup_fireworks()

# sensor values dict of tuples: (<data>, <safety_value>)
sensor_values = {}

i = 0
with open("test_log.txt", "w") as f:
    while True:
        print(f'{i} working...')
        i +=1 

        # # get sensor readings
        # data_oxygen, safety_value_oxygen     = oxygen_sensor.get_data_oxygen()
        # data_light, safety_value_light       = light_sensor.get_data_light()
        # data_noise, safety_value_noise       = noise_sensor.get_data_noise()
        # data_co2, safety_value_co2           = aq_sensor.get_data_co2()
        # data_temp, safety_value_temp         = env_sensor.get_data_temp()
        # data_humidity, safety_value_humidity = env_sensor.get_data_humidity()
        # data_tvoc, safety_value_tvoc         = aq_sensor.get_data_tvoc()
        # data_pressure, safety_value_pressure = env_sensor.get_data_pressure()    

        sensor_values['oxygen']   = oxygen_sensor.get_data_oxygen()
        sensor_values['light']    = light_sensor.get_data_light()
        sensor_values['noise']    = noise_sensor.get_data_noise()
        sensor_values['co2']      = aq_sensor.get_data_co2()
        sensor_values['temp']     = env_sensor.get_data_temp()
        sensor_values['humidity'] = env_sensor.get_data_humidity()
        sensor_values['tvoc']     = aq_sensor.get_data_tvoc()
        sensor_values['pressure'] = env_sensor.get_data_pressure()    

        os.system('clear')

        # output info, to led matrix, and need to add webserver rather than print here..
        for k,v in sensor_values.items():
            data, safety_value = v
            matrix.update_display((k, safety_value))
            print(f'sensor: {k}; data: {data}; safety_value: {safety_value}')
            f.write(f'{i}: sensor: {k}; data: {data}; safety_value: {safety_value}')
        sleep(0.5)

################################################################################
#
#   in the morning... write the main program: canary.py
#
#   this will require some debugging of the various modules
#
#   also, need to firm-up requirements, and docker file etc
#
#   also need to test on balena - follow instructions.
#
#   also need to think about starting write up - would be good to have this 
#   all finished by Monday PM for putting into the all-hands doc and closing out
#   residency project.
#
################################################################################