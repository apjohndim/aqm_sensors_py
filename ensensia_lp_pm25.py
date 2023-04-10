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
from pms5003 import PMS5003

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
ioerror = False
try:
    pms5003 = PMS5003(
        device='/dev/ttyAMA0',
        baudrate=9600,
        pin_enable=13,
        pin_reset=19
    )
except Exception as e:
    if OPTIONS['verbose']:
        print(e)
        message = 'Something is wrong. PMS I/O Error. Please contact the provider'
        ensensia_lp_config_file.communicate_message (message)
        ioerror = True


# read data
if not ioerror:
    
    while True:
        
        try:
            data = pms5003.read()
            pm1_cf1 = data.data[0]
            pm25_cf1 = data.data[1]
            pm10_cf1 = data.data[2]
            pm1_cfatm = data.data[3]
            pm25_cfatm = data.data[4]
            pm10_cfatm = data.data[5]
            um03 = data.data[6]
            um05 = data.data[7]
            um10 = data.data[8]
            um25 = data.data[9]
            um50 = data.data[10]
            um100 = data.data[11]
            
            print ('PM2.5 : {} ug m-3'.format(pm25_cf1))
            print ('PM10 : {} ug m-3'.format(pm10_cf1))
            
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






















































