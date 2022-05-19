from machine import Pin
import time


# PIN 0 1 2 
#     0 1 0 30ms
#     0 0 1 100ms
#     1 0 1 1sec 
#     0 1 1 10sec

red_led = Pin(0,Pin.OUT)                    # ESP32 enable pin indicator 
watchdog = Pin(2, Pin.IN)                   # Watch dog trigger indicator 
wd1 = Pin(4,Pin.OUT)                        # Act as WD1 pulse


#Toggle green using wd1 pulse
def toggle (void):
    wd1.value(0)
    time.sleep(0.5)
    wd1.value(1)
    time.sleep(0.5)

#track wd timer cycles
def trigger (void):
    print("triggered")


#Watch dog pulses after timeout period

while True:
    
    if watchdog.value() == 1:
        red_led(0)
        print("nah")
    elif watchdog.value() == 0:
        red_led(1)
        print("yeah")
