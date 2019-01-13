import paho.mqtt.client as mqtt


def on_publish(client, usedata, mid):
	pass


SSclient = mqtt.Client()
SSclient.on_publish = on_publish


def publish(payload):
	try:
		SSclient.connect("192.168.8.88", 1883, 60)
		SSclient.loop_start()
	except Exception as e:
		print("Connect Failure|_|")
		print(e)
	else:
		SSclient.publish("SunShine",payload, qos=1)
		SSclient.loop_stop(force=False)


if __name__ == '__main__':
	publish("nihao")
'''
import paho.mqtt.publish as publish

publish.single("SunShine", payload="Hello AI", qos=1, hostname="192.168.8.88")
'''