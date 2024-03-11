# import narzedzi podstawowych
import machine
import time
from machine import Pin
from time import sleep

from sensor import Sensor

# definicja peryferiow
accRegAdrr = b'\x08'	#LSB X, MSB X, LSB Y...		6B
magRegAdrr = b'\x0E'	#LSB X, MSB X, LSB Y...		6B 
gyrRegAdrr = b'\x14'	#LSB X, MSB X, LSB Y...		6B
eulersRegAdrr = b'\x1A'	#LSB X, MSB X, LSB Y...	6B
quaternionsRegAdrr = b'\x20'	#LSB W, MSB W, LSB X, MSB X, LSB Y...	8B
linacRegAdrr = b'\x28'	#LSB X, MSB X, LSB Y...	przyspieszenia liniowe	6B
graVecDatRegAdrr = b'\x2E'	#LSB X, MSB X, LSB Y...		s Gravity Vector data 6B
tempDatRegAdrr = b'\x34'  # 1B

def uint16_t(val):
    return val & 0xFFFF

def int16_t(val):
    return ((val + 0x8000) & 0xFFFF) - 0x8000

class c_bno055(Sensor):
    def __init__(self,i2c):
        self.goodInit = False
        self.i2c = i2c
        self.adr = 0x28 #    myDevAddres = b'\x29'	#41
        self.orientEulX = 0
        self.orientEulY = 0
        self.orientEulZ = 0
        self.orientQuatX = 0
        self.orientQuatY = 0
        self.orientQuatZ = 0
        self.orientQuatW = 0
        self.linacceleX = 0
        self.linacceleY = 0
        self.linaccelerZ = 0
        self.gravecX = 0
        self.gravecY = 0
        self.gravecZ = 0
        self.gyrosX = 0
        self.gyrosY = 0
        self.gyrosZ = 0
        self.magnetX = 0
        self.magnetY = 0
        self.magnetZ = 0
        self.accX = 0
        self.accY = 0
        self.accZ = 0
        self.temp = 0
        self.accTreshold = 10

        # devList = self.i2c.scan()
        # myDevAddres = b'\x29'	#41
        # if myDevAddres in devList:   #cos mi nie dziala ten warunek
        if True:
            bn0config = bytearray(2)     # create a buffer with 10 bytes
            bn0config[0] = 0x3D
            bn0config[1] = 0x0C
            self.i2c.writeto(self.adr, bn0config)
            # zmiana jednostek
            bn0config[0] = 0x3B
            bn0config[1] = 0x00
            self.i2c.writeto(self.adr, bn0config)
            self.goodInit = True
        else:
            self.goodInit = False

    def readTemp(self):
        # wybieranie adresu w pamieci urzadzenia
        self.i2c.writeto(self.adr, tempDatRegAdrr)
        # odczyt z pamieci urzadzenia
        temp = self.i2c.readfrom(self.adr, 1)
        # temperatura zawyzona o jakies 3 stopnie celcjusza
        self.temp = (int(temp[0])) - 3
        # print(f"Temperatura", self.temp)

    def readEuler(self):
        self.i2c.writeto(self.adr, eulersRegAdrr)
        data = self.i2c.readfrom(self.adr, 6)
        self.orientEulX = int16_t(data[0] | (data[1] << 8))
        self.orientEulY = int16_t(data[2] | (data[3] << 8))
        self.orientEulZ = int16_t(data[4] | (data[5] << 8))
        # print(f"orientEulerX", self.orientEulX)
        # print(f"orientEulerY", self.orientEulY)
        # print(f"orientEulerZ", self.orientEulZ)

    def readQuaternions(self):
        self.i2c.writeto(self.adr, quaternionsRegAdrr)
        data = self.i2c.readfrom(self.adr, 8)
        self.orientQuatW = int16_t(data[0] | (data[1] << 8))
        self.orientQuatX = int16_t(data[2] | (data[3] << 8))
        self.orientQuatY = int16_t(data[4] | (data[5] << 8))
        self.orientQuatZ = int16_t(data[6] | (data[7] << 8))
        # print(f"orientQuaternionsX", self.orientQuatX)
        # print(f"orientQuaternionsY", self.orientQuatY)
        # print(f"orientQuaternionsZ", self.orientQuatZ)
        # print(f"orientQuaternionsW", self.orientQuatW)

    def readLinearAcc(self):
        self.i2c.writeto(self.adr, linacRegAdrr)
        data = self.i2c.readfrom(self.adr, 6)
        # dane raw
        self.linacceleX = int16_t(data[0] + (data[1] << 8))
        self.linacceleY = int16_t(data[2] + (data[3] << 8))
        self.linacceleZ = int16_t(data[4] + (data[5] << 8))
        # filtrowanie szumu tresholdem (aby lezacy czujnik poakzywal 0)
        if (self.linacceleX < self.accTreshold) and (self.linacceleX > - self.accTreshold):
            self.linacceleX = 0
        if (self.linacceleY < self.accTreshold) and (self.linacceleY > - self.accTreshold):
            self.linacceleY = 0
        if (self.linacceleZ < self.accTreshold) and (self.linacceleZ > - self.accTreshold):
            self.linacceleZ = 0
        # print(f"LinearAccelerationX", self.linacceleX)
        # print(f"LinearAccelerationY", self.linacceleY)
        # print(f"LinearAccelerationZ", self.linacceleZ)

    def measure(self):
        self.readEuler()
        self.readQuaternions()
        self.readLinearAcc()

    def get_value(
        self,
        order: list | tuple = [
            "orientEulX",
            "orientEulY",
            "orientEulZ",
            "orientQuatX",
            "orientQuatY",
            "orientQuatZ",
            "orientQuatW",
            "linacceleX",
            "linacceleY",
            "linacceleZ",
        ],
    ) -> tuple[int | float | str | list, list]:
        self.measure()
        values = []
        for item in order:
            if hasattr(self, item):
                values.append(getattr(self, item))
        return values, [f"imu.{key}" for key in order]

    def printAll(self):
        print(f"orientEulerX", self.orientEulX)
        print(f"orientEulerY", self.orientEulY)
        print(f"orientEulerZ", self.orientEulZ)
        print(f"orientQuaternionsX", self.orientQuatX)
        print(f"orientQuaternionsY", self.orientQuatY)
        print(f"orientQuaternionsZ", self.orientQuatZ)
        print(f"orientQuaternionsW", self.orientQuatW)
        print(f"LinearAccelerationX", self.linacceleX)
        print(f"LinearAccelerationY", self.linacceleY)
        print(f"LinearAccelerationZ", self.linacceleZ)
####### End class ################


# i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

############# petla glowna programu ###################
# bnoSens = c_bno055(i2c)
# if bnoSens.goodInit is True:
# machine.sleep(100)
# bnoSens.readTemp()
# bnoSens.readEuler()
# bnoSens.readQuaternions()
# bnoSens.readLinearAcc()

# else:
# del bnoSens


# while True:
# bnoSens.readLinearAcc()

# machine.sleep(200)
