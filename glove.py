from typing import Any, Dict, List, Literal
from res_sensors import Res_sensor
from communication import Communication
import pinyPBL
from config import Sensor_types
from sensor import Sensor

Sensor_names = Dict[Sensor_types, Dict[Literal["en", "pl"], str]]

class Glove:

    SENSOR_TYPES = list(Sensor_types.__args__)
    
    # TODO: it should only store some kind of reference to the sensor, not the actual value
    # make the object responsible for reading the value and maybe implementing some interface
    # for the sensor

    def __init__(self, sensors: Dict):
        # controller uart
        self.uart_control = Communication()
        
        
        # finger statuses/values
        # TODO: make a dedicated class for elements of this
        self._sensors = sensors

        
    def read(self, function):
        def read_wrapper(order: set) -> Dict:
            a 
            return {}
            # that should get dictionary of values from sensors
        # for finger in self.status.keys():
        #     if finger == "emg":
        #         continue
        #     temp = self.status[finger]
        #     self.status[finger][self._bend]["val"] = temp[self._bend]["conf"].get_value()
        #     self.status[finger][self._pressure]["val"] = temp[self._pressure]["conf"].get_value()
            
        # self.status[self._emg]["val"] = self.status[self._emg]["conf"].get_value()
        return read_wrapper
    # waits for bluetooth proper handling
    # def send(self):
    #     self.uart_control.send_usb(self.__payload_mapper())        
    
    @read
    def __payload_mapper(self, sensors: Dict, order: set, separator: str = ";") -> List:
        pass
    
    def values(self, order: set, separator: str = ";") -> str:
        return separator.join(self.__payload_mapper(self._sensors, order, separator))