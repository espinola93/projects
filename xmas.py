import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

Relay_1_GPIO = 37
GPIO.setup(Relay_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(Relay_1_GPIO, GPIO.LOW)
#a=input("input on(1) OR off(0)")

GPIO.output(Relay_1_GPIO, GPIO.HIGH) # out
time.sleep(5)
GPIO.output(Relay_1_GPIO, GPIO.LOW) # on
		
time.sleep(0.5)

GPIO.cleanup()
