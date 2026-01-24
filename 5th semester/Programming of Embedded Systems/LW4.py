from machine import Pin
from pyb import USB_VCP, Timer

vcp = USB_VCP()
green_LED = Pin("LED1", Pin.OUT)
red_LED = Pin ("LED3", Pin.OUT)
pin_SW = Pin("SW", Pin.IN, Pin.PULL_DOWN)

width_per = 1
tim = Timer(1, freq=1000)
ch = tim.channel(2, Timer.PWM, pin=red_LED)

while True:
    cmd = vcp.recv(7, timeout=200)
    if (cmd == b'led'):
        vcp.send("Green led toggled\r\n", timeout=200)
        if green_LED.value():
            green_LED.low()
        else:
            green_LED.high()
    elif ('pwm' in cmd):
        divided = str(cmd).split(' ')
        if len(divided) > 2:
            vcp.send(f"Error, bad argument\r\n", timeout=200)
        else:
            value = int(divided[1].strip("'"))
            ch.pulse_width_percent(value)
            vcp.send(f"Red led pulse changed\r\n", timeout=200)
    elif (cmd == b'state'):
        if pin_SW.value():
            vcp.send(f"SW is pressed\r\n", timeout=200)
        else:
            vcp.send(f"SW is unpressed\r\n", timeout=200)
        
        
        
    