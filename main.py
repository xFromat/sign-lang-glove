# main.py -- put your code here!
from time import sleep
from glove import Glove
from communication import Communication
import bno055
from machine import I2C, Pin
from config import *
from res_sensors import Res_sensor
import pinyPBL


# sampling frequency
FS = 0.1 # Hz

# build sensors sets
sensors = {}
sensor_names = list(Sensor_types.__args__)
# bend & pressure
sensors_pl = [sensor["pl"] for sensor in sensors_config.values()]
for i in range (0, len(FINGERS)):
    finger = list(FINGERS)[i]
    sensors[finger][sensor_names[0]] = Res_sensor(getattr(pinyPBL, f'{sensors_pl[0]+str(i+1)}'))
    sensors[finger][sensor_names[1]] = Res_sensor(getattr(pinyPBL, f'{sensors_pl[1]+str(i+1)}'))    
# emg
sensors["emg"] = Res_sensor(pinyPBL.pinEMG)
# imu
sensors["imu"] = bno055.c_bno055(I2C(0, scl=Pin(2), sda=Pin(1), freq=100000))
# build glove object
glove = Glove(sensors_config, FINGERS)
# uart_control = Communication()

fileName = f'./Julia{ext}'

# while True:
t = 5
while t > 0:
    print(t)
    t-=1
    sleep(1)
glove.read()
sensor.measure()
#     sensor.f.writeAll()
# Open the file in append mode ('a')
with open(fileName, 'a') as f:
    # Write the line you want to add followed by a newline character
    f.write(f"{glove.__payload_mapper()}\n")
    f.write(f"orientEulerX {sensor.orientEulX}\n")
    f.write(f"orientEulerY {sensor.orientEulY}\n")
    f.write(f"orientEulerZ {sensor.orientEulZ}\n")
    f.write(f"LinearAccelerationX {sensor.linacceleX}\n")
    f.write(f"LinearAccelerationY {sensor.linacceleY}\n")
    f.write(f"LinearAccelerationZ {sensor.linacceleZ}\n")
    f.write("#######################################################################################################\n")
