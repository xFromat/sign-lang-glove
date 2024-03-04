import machine
import time
import ubluetooth
#from ssd1306 import SSD1306_I2C

#ble = ubluetooth.BLE()

# oled = SSD1306_I2C(128, 64, machine.I2C(0, scl=4, sda=5))

def usb_communication():
    usb = machine.UART(0, baudrate=115200, tx=17, rx=16)

    while True:
        if usb.any():
            received_data = usb.read()
            print("Received data over USB:", received_data)
            #oled.fill(0)
            #oled.text("USB: {}".format(received_data), 0, 0)
            #oled.show()

def ble_communication():
    def on_rx(event, data):
        print("Received data over BLE:", data)
        #oled.fill(0)
        #oled.text("BLE: {}".format(data), 0, 0)
        #oled.show()
    #oled.init_display()
    ble.config(rxbuf=256)
    ble.gatts_register_read_callback(0, on_rx)
    ble.gap_advertise(1000)

# usb_communication()
# ble_communication()