from umqtt.robust import MQTTClient
import time
import network
from machine import Pin, time_pulse_us
from time import sleep_us

CERT_FILE='/Esp8266.der'
KEY_FILE='/Esp8266.private.der'
MQTT_CLIENT_ID='Esp8266'
MQTT_HOST='a4glsz57ukz4u-ats.iot.us-east-1.amazonaws.com'
WIFI_SSID=b'KPU_WiFi1451'
WIFI_PW=None
MQTT_TOPIC='ULTRASONIC'

with open(KEY_FILE, "rb") as f:
    key=f.read()
    print("Got Key")
with open(CERT_FILE, "rb") as f:
    cert=f.read()
    print("Got Cert")

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFI_SSID, WIFI_PW)
sta_if.ifconfig()

client=MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=8883, keepalive=4000, ssl=True, ssl_params={"key":key, "cert":cert, "server_side":False})

client.connect()
print("Connect")

def pubfunc(msg):
    global client
    client.publish(MQTT_TOPIC, msg)
    print("Sent: " + msg)

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
    pubfunc("{}cm".format(distance))
    time.sleep(1)