# main.py -- put your code here!
import os
from time import sleep, ticks_ms

from machine import I2C, Pin
import _thread as th

import bno055
import config
import pinyPBL
from glove import Glove
from res_sensors import Res_sensor
from tools import values_wrapper, signalize_recording

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
signal_led = Pin(13, Pin.OUT)

while True:
    led_status = [True, 0.5] # is on + sleep time between blinking
    th.start_new_thread(signalize_recording, (signal_led, led_status))
    try:
        sign = input("Name of sign to record: ")
    except KeyboardInterrupt:
        led_status[0] = False
        break
    t_current = t
    # record sign
    filename = f"{testSubject}_{sign}{config.ext}"
    led_status[1] = 0.2    
    print("Recording...")    
    try:
        with open(filename, "w") as file:
            led_status[1] = 0
            sleep(1)
            if "jednozna" in filename.lower():
                t_current = 1/FS            
            file.write(f"time{config.separator}{glove.get_info(sensor_names)}\n")            
            while t_current > 0:
                if t_current > int(t_current)-1/FS and t_current < int(t_current)+1/FS:
                    print(f"{int(t_current)}s")
                # get status
                status = glove.get_status(sensor_names)
                values = values_wrapper(status, config.separator)                
                file.write(f"{ticks_ms()};{values}\n")
                sleep(1 / FS)
                t_current -= 1/FS
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        led_status[0] = False
        break
        
    
    print(f"Recording finished: {filename}")
    led_status[0] = False
    # just waiter
    sleep(1)
led_status[0] = False