from res_sensors import Res_sensor
from communication import Communication
from pinyPBL import *

class Glove:
    def __init__(self, sensor_names: list[str, str, str]):
        # controller uart
        self.uart_control = Communication()
        
        bend = sensor_names[0]
        pressure = sensor_names[1]
        # finger statuses/values
        self.status = {
            "fingers": {
                "thumb": {
                    bend: {
                        "conf": Res_sensor(pinUgiecie1, bend),
                        "value": -1
                    },
                    pressure: {
                        "conf": Res_sensor(pinNacisk1, pressure),
                        "value": -1
                    }
                },
                "index": {
                    bend: {
                        "conf": Res_sensor(pinUgiecie2, bend),
                        "value": -1
                    },
                    pressure: {
                        "conf": Res_sensor(pinNacisk2, pressure),
                        "value": -1
                    }
                },
                "middle": {
                    bend: {
                        "conf": Res_sensor(pinUgiecie3, bend),
                        "value": -1
                    },
                    pressure: {
                        "conf": Res_sensor(pinNacisk3, pressure),
                        "value": -1
                    }
                },
                "ring": {
                    bend: {
                        "conf": Res_sensor(pinUgiecie4, bend),
                        "value": -1
                    },
                    pressure: {
                        "conf": Res_sensor(pinNacisk4, pressure),
                        "value": -1
                    }
                },
                "little": {
                    bend: {
                        "conf": Res_sensor(pinUgiecie5, bend),
                        "value": -1
                    },
                    pressure: {
                        "conf": Res_sensor(pinNacisk5, pressure),
                        "value": -1
                    }
                }
            },
            "emg": {
                    "conf": Res_sensor(pinEMG, "emg"),
                    "value": -1
            }
        }
        
    def get_readings(self):
        for finger in self.status["fingers"].keys():
            temp = self.status["fingers"][finger]
            self.status["fingers"][finger]["bend"]["value"] = temp["bend"]["conf"].get_value()
            self.status["fingers"][finger]["pressure"]["value"] = temp["pressure"]["conf"].get_value()
            
        self.status["emg"]["value"] = self.status["emg"]["conf"].get_value()
        
    def send(self):
        self.uart_control.send_usb(self.__payload_mapper())
    
    def getEMG(self):
        print(self.status["emg"]["value"])
    
    def __payload_mapper(self):
        return {
            "fingers": {
                "thumb": {
                    "bend": self.status["fingers"]["thumb"]["bend"]["value"],
                    "pressure": self.status["fingers"]["thumb"]["pressure"]["value"]
                },
                "index": {
                    "bend": self.status["fingers"]["index"]["bend"]["value"],
                    "pressure": self.status["fingers"]["index"]["pressure"]["value"]
                },
                "middle": {
                    "bend": self.status["fingers"]["middle"]["bend"]["value"],
                    "pressure": self.status["fingers"]["middle"]["pressure"]["value"]
                },
                "ring": {
                    "bend": self.status["fingers"]["ring"]["bend"]["value"],
                    "pressure": self.status["fingers"]["ring"]["pressure"]["value"]
                },
                "little": {
                    "bend": self.status["fingers"]["little"]["bend"]["value"],
                    "pressure": self.status["fingers"]["little"]["pressure"]["value"]
                }
            },
                "emg": self.status["emg"]["value"]
        }
        
                