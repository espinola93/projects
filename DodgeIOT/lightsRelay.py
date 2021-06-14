import time
import RPi.GPIO as GPIO

Relay_1_GPIO = 11


def LightsRelaySetup():
	GPIO.setmode(GPIO.BOARD) # GPIO Numbers instead of board numbers
	#Relay_1_GPIO = 12
	GPIO.setup(Relay_1_GPIO, GPIO.OUT) # GPIO Assign mode
	GPIO.output(Relay_1_GPIO, GPIO.LOW)



def LightsOn():
        GPIO.output(Relay_1_GPIO, GPIO.HIGH) # out
def LightsOff():
        GPIO.output(Relay_1_GPIO, GPIO.LOW) # on



GPIO.cleanup()

