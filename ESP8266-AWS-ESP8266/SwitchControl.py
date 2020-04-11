from umqtt.robust import MQTTClient
from machine import Pin
import time
import network

PIR = Pin(5, Pin.IN)

CERT_FILE='/Esp8266.der'
KEY_FILE='/Esp8266.private.der'
MQTT_CLIENT_ID='Esp8266'
MQTT_HOST='a4glsz57ukz4u-ats.iot.us-east-1.amazonaws.com'
WIFI_SSID=b'KPU_WiFi1451'
WIFI_PW=None
MQTT_TOPIC='SWITCH'

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

while True:
    pubfunc(str(PIR.value()))
    time.sleep(1)