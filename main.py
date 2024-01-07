# main.py -- put your code here!
from machine import Pin, ADC
from time import sleep

from res_sensors import Res_sensor

# program
in_pin = 14
bend_sensor = Res_sensor(in_pin, "bend")

while True:
    print(bend_sensor.get_value())
    print(bend_sensor.get_volts())
    sleep(1)
