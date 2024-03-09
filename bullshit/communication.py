import machine
import utime


class Communication:
    def __init__(self):
        self.uart = machine.UART(1, baudrate=115200, tx=0, rx=1)  # CHYBA ustawienia dla ESP32-S2

    def send_usb(self, flex_value) -> None:
        # tak zeby mozna bylo je wyslac
        data_to_send = "Flex: {}".format(flex_value)

        # wyslanie
        self.uart.write(data_to_send + '\n')
    
