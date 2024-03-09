# main.py -- put your code here!
import os
from time import sleep, ticks_ms

from machine import I2C, Pin

import bno055
import config
import pinyPBL
from glove import Glove
from res_sensors import Res_sensor
from tools import values_wrapper

# sampling frequency
FS = 200 # Hz
t = 3  # s

# build sensors sets
sensors = {}
sensor_names = config.Sensor_types
# bend & pressure
for i in range(0, len(config.FINGERS)):
    finger = config.FINGERS[i]
    sensors[finger] = {}
    sensors[finger]["bend"] = Res_sensor(getattr(pinyPBL, f"pinUgiecie{str(i+1)}"))
    sensors[finger]["pressure"] = Res_sensor(getattr(pinyPBL, f"pinNacisk{str(i+1)}"))
# emg
sensors["emg"] = Res_sensor(pinyPBL.pinEMG)
# imu
sensors["imu"] = bno055.c_bno055(I2C(0, scl=Pin(2), sda=Pin(1), freq=100000))
#######################################################################################################
# build glove object
glove = Glove(sensors)
# uart_control = Communication()

# I propose it is to be a name of the person who is testing the glove with path to the file at the beginning
testSubject = "./Piotrek"

# while True:
while True:
    sign = input("Name of sign to record: ")
    t_current = t
    # record sign
    filename = f"{testSubject}_{sign}{config.ext}"
    # delete file if it exists
#     if not os.path.exists("./tests/"):
#           os.makedirs("./tests/")  # Create the directory if needed
#     try:
#         remove(filename)
#     except Exception:
#         pass    
    print("Recording...")
    
    try:
        with open(filename, "w") as file:
            file.write(f"time;{glove.get_info()}\n")            
            while t_current > 0:
                if int(t_current) == t_current:
                    print(f"{int(t_current)}s")
                # get status
                status = glove.get_status(order = sensor_names)
                values = values_wrapper(status, config.separator)
                file.write(f"{ticks_ms()};{values}\n")
                sleep(1 / FS)
                t_current -= 1/FS
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        break
        

    print(f"Recording finished: {filename}")
    # just waiter
    sleep(1)
