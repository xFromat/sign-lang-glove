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



def sort_dict(dictionary: dict, order: list = []) -> dict:
    sorted_keys = sorted([key for key in dictionary if any(key.endswith(pattern) for pattern in order)], key=lambda x: [order.index(pattern) if x.endswith(pattern) else len(order) for pattern in order])
    return {key: dictionary[key] for key in sorted_keys}

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
