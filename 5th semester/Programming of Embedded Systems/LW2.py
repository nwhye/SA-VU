from pyb import DAC
from machine import Pin
from machine import ADC
import time

pin_SW = Pin("SW", Pin.IN, Pin.PULL_DOWN)
A2 = Pin("A2", Pin.ANALOG) 
adc = ADC(A2)
dac = DAC(2)
global dac_val
dac_val = 0

while True:
    if pin_SW.value()!=0:
        
        if dac_val < 250:
            dac_val += 10
        else:
            dac_val = 250
        dac.write(dac_val)
        val = adc.read_u16()
        print(f"DAC value: {dac_val}")
        print(f"Source value: {val}")
        sens_val = (val/65536 * 2000)
        print(f"CO2 value: {sens_val} ppm\n")
        
        time.sleep_ms(200)
