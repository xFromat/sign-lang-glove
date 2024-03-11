from res_sensors import Res_sensor
# from communication import Communication
import pinyPBL
from config import Sensor_types, separator
from sensor import Sensor
from tools import values_wrapper, flatten_dict, sort_dict


class Glove:

    SENSOR_TYPES = Sensor_types

    def __init__(self, sensors: dict):
        # controller uart
#         self.uart_control = Communication()

        self._sensors = sensors

    def get_status(
        self, order: list
    ) -> list:
        """Get the value of the sensor"""        
        objs = sort_dict(flatten_dict(self._sensors), order)
        
        return [obj.get_value()[0] for obj in objs["values"]]
        
    def get_info(self, order: list) -> dict:
         sorted_dict = sort_dict(flatten_dict(self._sensors), order)         
         names = []
         for key, val in enumerate(sorted_dict["values"]):
             temp = val.get_value()[1]
             if not temp:
                 temp = [sorted_dict["keys"][key]]
             names.extend(temp)
             
         return values_wrapper(names, ";")
