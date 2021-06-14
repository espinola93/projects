
import time
import RPi.GPIO as GPIO

pin29 = 29


def ReverseLightsSetup():
        GPIO.setmode(GPIO.BOARD) # GPIO Numbers instead of board numbers
        #Relay_1_GPIO = 12
        GPIO.setup(pin29, GPIO.OUT) # GPIO Assign mode
        GPIO.output(pin29, GPIO.LOW)



def ReverseLightsOn():
        GPIO.output(pin29, GPIO.HIGH) # out
def ReverseLightsOff():
        GPIO.output(pin29, GPIO.LOW) # on



GPIO.cleanup()

