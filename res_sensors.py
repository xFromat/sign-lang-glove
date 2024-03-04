from machine import Pin, ADC

class Res_sensor:
    """
    Class for instances of resistance sensors
    ---
    `Fields`
    - port - ADC port
    - max_v - maximum input voltage
    - adc_width - ADC width
    - sensor_type - type of sensor
    """
    # 1.3V - 180 deg       |    >1V -> intentional touch 
    # 0.9V - 90 deg        |    
    # 0.5V - full          |
    def __init__(self, pin_num: int, sensor_type: str, max_v: float = 3.3, adc_width: int = 8192):
        self.port = ADC(Pin(pin_num))
        # attenuation allows to measure above reference voltage
        if max_v >= 3.3:
            self.port.atten(ADC.ATTN_11DB)
        self.max_v = max_v
        self.adc_width = adc_width
        self.sensort_type = sensor_type    
    
    def get_value(self) -> int:
        return self.port.read()
    
    def get_volts(self) -> float:
        return self.get_value()*self.max_v/(self.adc_width-1)
    
    def get_bit(self) -> int:
        # depends on real thresholds
        return 0