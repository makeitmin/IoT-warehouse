from machine import Pin
import time

PIR = Pin(5, Pin.IN)

while True:
    print(PIR.value())
    time.sleep(1)