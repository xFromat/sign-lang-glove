# main.py -- put your code here!
from time import sleep

from res_sensors import Res_sensor

# program
# sampling frequency
FS = 1 # Hz
#
in_pin = 9 # A3 pin
bend_sensor = Res_sensor(in_pin, "bend") # 3.3V max, 13-bit ADC, bend sensor

while True:
    print("current voltage: ", bend_sensor.get_volts())    
    sleep(1/FS)
