import time, json, ssl
import paho.mqtt.client as mqtt
# 모든 파일 경로 사이는 /로 처리한다.
ENDPOINT='a4glsz57ukz4u-ats.iot.us-east-1.amazonaws.com' #End Point
THING_NAME='Robot_Arm' #사물이름
CERTPATH='C:/Users/sally/Downloads/robotarm/Robot_Arm.cert.pem' #cert파일 경로
KEYPATH='C:/Users/sally/Downloads/robotarm/Robot_Arm.private.key' #key 파일 경로
CAROOTPATH='C:/Users/sally/Downloads/robotarm/root-CA.crt' #RootCaPem 파일 경로
TOPIC = 'test_ColorSorter' #Topic명

def on_connect(mqttc, obj, flags, rc):
    if rc == 0: # 연결 성공
        print('connected')
def on_message(mqttc, obj, msg):
    print(msg.topic+":"+str(msg.payload))
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+TOPIC)

mqtt_client = mqtt.Client(client_id=THING_NAME)
#CallBack에 사용할 메세지
mqtt_client.on_message = on_message
mqtt_client.on_connect = on_connect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.tls_set(CAROOTPATH, certfile= CERTPATH, keyfile=KEYPATH, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqtt_client.connect(ENDPOINT, port=8883)
mqtt_client.subscribe(TOPIC)
mqtt_client.loop_start()
while(1):
    time.sleep(1)