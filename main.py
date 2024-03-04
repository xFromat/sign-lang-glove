# main.py -- put your code here!
from time import sleep
from glove import Glove
from communication import Communication
import bno055
from machine import I2C, Pin

# program
# config
# sampling frequency
FS = 0.1 # Hz

FINGERS = set(["thumb", "index", "middle", "ring", "little"])
# pl: "kciuk", "wskazujacy", "srodkowy", "serdeczny", "maly"
glove = Glove(["bend", "pressure"])
uart_control = Communication()

i2c = I2C(0, scl=Pin(2), sda=Pin(1), freq=100000)
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = bno055.c_bno055(i2c)

fileName = './Julia.txt'

# while True:
t = 5
while t > 0:
    print(t)
    t-=1
    sleep(1)
glove.get_readings()
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

#     glove.getEMG()
# sleep(1/FS)
