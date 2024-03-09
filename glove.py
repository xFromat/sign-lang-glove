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
        self, order: list = SENSOR_TYPES
    ) -> list:
        """Get the value of the sensor"""
        sensors = list(sort_dict(flatten_dict(self._sensors), order).values())
        values = []
        for sensor in sensors:
            temp = sensor.get_value()
            values.append(temp[0])
        return values
    
    def get_info(self, order: list = SENSOR_TYPES) -> list:
        main_sensors: dict = sort_dict(flatten_dict(self._sensors), order)
        results: list = []
        for key, value in main_sensors.items():
            info = value.get_value()
            info = info[1]
            curr = key
            if len(info) > 0:
                curr = []
                for label in info:
                    curr.append(f'{key}.{label}')
            results.append(curr)
        return values_wrapper(results, separator)
        