
import time
import RPi.GPIO as GPIO

pin35 = 35


def BreakLightsSetup():
        GPIO.setmode(GPIO.BOARD) # GPIO Numbers instead of board numbers
        #Relay_1_GPIO = 12
        GPIO.setup(pin35, GPIO.OUT) # GPIO Assign mode
        GPIO.output(pin35, GPIO.LOW)



def BreakLightsOn():
        GPIO.output(pin35, GPIO.HIGH) # out
def BreakLightsOff():
        GPIO.output(pin35, GPIO.LOW) # on
