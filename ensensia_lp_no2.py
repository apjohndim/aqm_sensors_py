# -*- coding: utf-8 -*-
"""
           _.-'~~~~~~`-._
          /      ||      \
         /       ||       \
        |        ||        |
        | _______||_______ |
        |/ ----- \/ ----- \|
       /  (     )  (     )  \
      / \  ----- () -----  / \
     /   \      /||\      /   \
    /     \    /||||\    /     \
   /       \  /||||||\  /       \
  /_        \o========o/        _\
    `--...__|`-._  _.-'|__...--'
            |    `'    |
            

ENSENSIA Learning Packages (LP)

Foundation for Research and Technology Hellas (FORTH)
Institute of Chemical Engineering Sciences (ICE-HT)

© all rights reserved
@author: japostol

Do not distribute, reproduce, or expose this code

"""

# Import the necessary libraries
import sys
import os
import datetime
import time

import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Register the working directory
base_path = 'C:\\Users\\japostol\\Desktop\\ENSENSIA CODE LEARNING PROJECT\\'
sys.path.append(base_path)

# Load more libraries from the project
import ensensia_lp_config_file

# Request the OPTIONS variable, to handle the process
OPTIONS = ensensia_lp_config_file.get_options()


# Inform the user we are ready to start
curdate = datetime.datetime.today()
message = 'ENSENSIA starts sensing Particulate Matter'
ensensia_lp_config_file.communicate_title (message)

message = 'Datetime: {}'.format(curdate)
ensensia_lp_config_file.communicate_message (message)


# Communicate with the sensor

i2c_1 = busio.I2C(board.SCL,board.SDA)
ioerror = False
try:
    ads_no2 = ADS.ADS1015(i2c_1,address=0x48)
except Exception as e:
    if OPTIONS['verbose']:
        print(e)
        message = 'Something is wrong. ADS sensor error. Please contact the provider'
        ensensia_lp_config_file.communicate_message (message)
        ioerror = True


# read data
if not ioerror:
    
    while True:
        
        try:
            chan_1 = AnalogIn(ads_no2,ADS.P0)
            chan_2 = AnalogIn(ads_no2,ADS.P1)
            chan_3 = AnalogIn(ads_no2,ADS.P2)
            chan_4 = AnalogIn(ads_no2,ADS.P3)
            
            
            WEu = (chan_1.voltage*1000) - (chan_2.voltage*1000)
            AEu = (chan_3.voltage*1000) - (chan_4.voltage*1000) 
            
            # default temperature is 25. Integrate BME sensor for dynamic
            temperature = 25
            
            # alphasense provides this for every sensor
            sensitivity = 0.435
            alpha_factor = 1
            
            # these are provided by alphasense - update with the correct
            WE0 = 100
            AE0 = 100
            WEe = 100
            AEe = 100
            
            
            WEc = ((WEu-WEe)-(WE0-AE0)-alpha_factor*(AEu-AEe))/sensitivity
            WEc_ppb = WEc*1000
            
            print ('NO2 : {} ppb'.format(WEc_ppb))
            
            #### ADD LOGS HERE ####
            if OPTIONS['to_log_file']:
                a = 0
            
        except Exception as e:
            print(e)
            message = 'Something is wrong when reading data. Please contact the provider'
            ensensia_lp_config_file.communicate_message (message)
            break
        
        time.sleep (5)

message = 'Script will now exit'
ensensia_lp_config_file.communicate_title (message)






















































