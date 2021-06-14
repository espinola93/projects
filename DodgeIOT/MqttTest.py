
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

pin35 = 11
MQTT_SERVER = "10.10.10.1"
MQTT_PATH = "test/light"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload=="1":
        print"lights on"
	BreakLightsOn()
    elif msg.payload=="0":
	BreakLightsOff()
	print"lights off"
        # more callbacks, etc

def BreakLightsSetup():
        GPIO.setmode(GPIO.BOARD) # GPIO Numbers instead of board numbers
        GPIO.setup(pin35, GPIO.OUT) # GPIO Assign mode
        GPIO.output(pin35, GPIO.LOW)



def BreakLightsOn():
        GPIO.output(pin35, GPIO.HIGH) # out
def BreakLightsOff():
        GPIO.output(pin35, GPIO.LOW) # on


BreakLightsSetup()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


