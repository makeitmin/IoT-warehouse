from machine import Pin
import time
LED = Pin(14, Pin.OUT)
while True:
    LED.value(1)
    time.sleep(10)
    LED.value(0)
    time.sleep(10)