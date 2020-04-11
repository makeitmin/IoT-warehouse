import time, json, ssl
import paho.mqtt.client as mqtt
# 모든 파일 경로 사이는 /로 처리한다.
ENDPOINT='a4glsz57ukz4u-ats.iot.us-east-1.amazonaws.com' #End Point
THING_NAME='AndreaHa' #사물이름
CERTPATH='C:/AWS_certification/AndreaHa/AndreaHa.cert.pem' #cert파일 경로
KEYPATH='C:/AWS_certification/AndreaHa/AndreaHa.private.key' #key 파일 경로
CAROOTPATH='C:/AWS_certification/AndreaHa/root-CA.crt' #RootCaPem 파일 경로
TOPIC = 'test_home' #Topic명

def on_connect(mqttc, obj, flags, rc):
	if rc == 0: # 연결 성공
		print('connected!!')
mqtt_client = mqtt.Client(client_id=THING_NAME)
mqtt_client.on_connect = on_connect
mqtt_client.tls_set(CAROOTPATH, certfile= CERTPATH, keyfile=KEYPATH ,
tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqtt_client.connect(ENDPOINT, port=8883)
mqtt_client.loop_start()
while True:
	payload = json.dumps({'action': 'test_home'}) #메시지 포맷
	mqtt_client.publish('test_home', payload, qos=1) #메시지 발행
	time.sleep(1)