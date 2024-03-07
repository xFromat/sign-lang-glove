from typing import Literal

from glove import Sensor_names
################################################################################################################################
# config
sensors_config: Sensor_names = {"bend": {"en": "bend", "pl": "pinUgiecie"}, "pressure": {"en": "pressure", "pl": "pinNacisk"}}
Sensor_types = Literal["bend", "pressure", "emg", "imu"]
# fingers for bend and pressure sensors
FINGERS = set(["thumb", "index", "middle", "ring", "little"])
# pl: "kciuk", "wskazujacy", "srodkowy", "serdeczny", "maly"
# file extension to save data
ext = ".csv"
################################################################################################################################