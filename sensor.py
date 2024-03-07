from typing import List, Tuple


class Sensor:
    def get_value(self) -> int | float | dict | str:
        raise NotImplementedError
    
    def values_mapper(self, values: dict = None, order: List | Tuple = None) -> List: # type: ignore
        if values is None:
            return [self.get_value()]
        order = order if order is not None else list(values.keys())
        arr_values = []        
        for curr_name in order:
            curr_element: Sensor = values[curr_name]
            # if there is a nested dict, extract value from it
            if isinstance(curr_element, dict):
                self.values_mapper(curr_element, list(curr_element.keys()))
            else:
                arr_values.append(curr_element.get_value())
        return arr_values