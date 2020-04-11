from machine import Pin

outpin = Pin(5,Pin.OUT)
outpin.value(0)
inpin = Pin(4,Pin.IN)
value=inpin.value()
print(value)