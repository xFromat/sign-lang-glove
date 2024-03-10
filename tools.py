from time import sleep

def list_flatterner(func):
    def flatterner_wrapper(values: list, sep: str) -> list:  # type: ignore
        """Flatten the list of values to a list of strings"""
        return func(
            [
                str(item)
                for sublist in values
                for item in (sublist if isinstance(sublist, list) else [sublist])
            ],
            sep
        )

    return flatterner_wrapper

@list_flatterner
def values_wrapper(values: list, separator: str = ";") -> str:
    return separator.join(values)


@mkhashmap
def sort_dict(dictionary: dict, order: list) -> dict:
    order_sorted = order.copy()
    order_sorted.sort()
    dictionary_keys = list(dictionary.keys())
    sorted_dict = {}
    while order_sorted:
        key = order.index(order_sorted.pop(0))    
        sorted_dict[dictionary_keys[key]] = dictionary[dictionary_keys[key]]
        order.pop(key)
        dictionary_keys.pop(key)
    return sorted_dict

def flatten_dict(given: dict):
    new_dict = {}
    for key, val in given.items():
        if not isinstance(val, dict):
            new_dict[key] = val
            continue
        
        fl = flatten_dict(val)
        for k, v in fl.items():
            new_dict[f'{key}.{k}'] = v
        
    return new_dict

def signalize_recording(led, status: list) -> None:
    while status[0]:        
        if status[1] > 0:
            led.value(not led.value())
            sleep(status[1])
        else:
            led.value(1)
    led.value(0)
    
def mkhashmap(func):
    def hashmapwrapper(dictionary: dict, order: list = []):
        order_numbers = list(range(len(order)))
        hashed = []
        for index, value in enumerate(order):
            keys = [key for key in dictionary.keys() if key.endswith(value)]
            hashed.extend([index]*len(keys))
        return func(dictionary, hashed)
    return hashmapwrapper