from machine import Pin
import time
PIR = Pin(13, Pin.IN)
while True:
    print(PIR.value())
    time.sleep(1)