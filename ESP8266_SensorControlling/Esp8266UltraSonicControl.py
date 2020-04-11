from machine import Pin, time_pulse_us
from time import sleep_us
from machine import Pin
import time

class UltrasonicRanger:
    def __init__(self, sig_pin, timeout=10000):
        self.sig_pin = sig_pin
        self.timeout = timeout
    def get_distance(self):
        self.activate()
        t = time_pulse_us(self.signal, 1, self.timeout)
        distance = t / 29 / 2 # 실제 거리 측정하여 수치 확인 필요
        return distance

    def activate(self):
        self.signal = Pin(self.sig_pin, mode=Pin.OUT) # trigger pin
        self.signal.value(0)
        sleep_us(2)
        self.signal.value(1)
        sleep_us(10)
        self.signal.value(0)
        self.signal = Pin(self.sig_pin, mode=Pin.IN) # echo pin
ultrasonic = UltrasonicRanger(12) #핀번호

while True:
    distance = ultrasonic.get_distance()
    print("{}cm".format(distance))
    time.sleep(1)