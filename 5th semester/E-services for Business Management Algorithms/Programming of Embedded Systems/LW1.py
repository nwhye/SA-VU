from machine import Pin
import time
green_LED = Pin("LED1", Pin.OUT)
pin_A1 = Pin("A1", Pin.IN, Pin.PULL_DOWN)
pin_A2 = Pin("A2", Pin.IN, Pin.PULL_UP)
b1_state = True
b2_state = True
iterator = 0
while True:
    if pin_A1.value()==1:
        if b1_state:
            iterator += 1
            print(f"Variable value: {iterator}")
            b1_state = False
    else:
        b1_state = True
        
    
    if pin_A2.value()==1:
        if b2_state:
            print("LED on")
            green_LED.high()
            time.sleep_ms(500)
            b2_state = False
    else:
        b2_state = True
        green_LED.low()
        
