from pyb import Pin, Timer as pTimer
from machine import Timer as mTimer

led = Pin("LED1", Pin.OUT)
tim_ch = pTimer(8, freq=2500)
ch = tim_ch.channel(2, pTimer.PWM, pin=led)
fade = 0
invert = False

def increase():
    global fade, invert
    fade = round((fade + 0.05), 3)
    if (fade == 100):
        invert = True
    
def decrease():
    global fade, invert
    fade = round((fade - 0.05), 3)
    if (fade == 0):
        invert = False

def heartbeat(t):
    global fade, invert
    
    if invert == False:
        increase()
    else:
        decrease()
        
    if (fade % 1 == 0):
        ch.pulse_width_percent(int(fade))
        print(fade)
    

tim = mTimer()
tim.init(mode=mTimer.PERIODIC, freq=2500, callback=heartbeat)


while True:
    pass 
