
import RPi.GPIO as GPIO 
import time

servoPIN = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
s = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
s.start(0) # Initialization

def leftsteer():
	s.ChangeDutyCycle(2.5)#backwards
	time.sleep(1)
	s.ChangeDutyCycle(2.5)#backwards
	time.sleep(1)
	s.ChangeDutyCycle(8)
	time.sleep(1)

def rightsteer():
	s.ChangeDutyCycle(8)
	time.sleep(1)
	s.ChangeDutyCycle(2.5)
	time.sleep(1)
