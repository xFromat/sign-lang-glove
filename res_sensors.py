from machine import Pin, ADC

class Res_sensor:
    # 1.3V - 180 deg       |    >1V -> intentional touch 
    # 0.9V - 90 deg        |    
    # 0.5V - full          |
    def __init__(self, pin_val: int, sensor_type: str):
        self.port = ADC(Pin(pin_val))
        self.port.atten(ADC.ATTN_11DB)
        
        self.sensort_type = sensor_type
        
    def get_value(self) -> int:
        return self.port.read()
    
    def get_volts(self) -> float:
        return (3.3*self.get_value())/4095
    
    def get_bit(self) -> int:
        # depends on real thresholds
        return 0