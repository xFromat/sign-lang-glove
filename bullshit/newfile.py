a = {"thumb": {"bend": {"23adam": 37, "brother": [23, 56], "kupa": {"ham": "szynka"}}, "pressure": 6}, "index": {"bend": 5, "pressure": 6},  "imu": [1,2,3,4,5,6], "emg": 35}

order = ["bend", "pressure", "emg", "imu"]

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
def sort_dict(dictionary, order):
    sorted_keys = sorted([key for key in dictionary if any(key.endswith(pattern) for pattern in order)], key=lambda x: [order.index(pattern) if x.endswith(pattern) else len(order) for pattern in order])
    sorted_dict = {key: dictionary[key] for key in sorted_keys}
    return list(sorted_dict.values())	
	
flat = sort_dict(flatten_dict(a), order)
print(flat)
	
