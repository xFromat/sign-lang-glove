from machine import Pin
import time
import bluetooth

led = Pin(2, Pin.OUT)

class BLEServer:
    def __init__(self, name):
        self.name = name
        self.ble = bluetooth.BLE()
        self.ble.active(True)
        self.ble.config(gap_name=name)

    def advertise(self):
        # Rozpoczyna reklamowanie urządzenia, aby mogło być widoczne dla innych urządzeń Bluetooth
        self.ble.gap_advertise(100, b"\x02\x01\x06\x0b\x09" + self.name)

# Tworzenie instancji serwera BLE
ble_server = BLEServer("ESP32-BLE-Server")

# Rozpoczęcie reklamowania
ble_server.advertise()

print("ESP32 teraz reklamuje się jako", ble_server.name)

try:
    while True:
        led.value(not led.value())
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Zatrzymano program")
    ble_server.ble.active(False)
    
