import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
p.start(0) # Initialization

#Right
p.ChangeDutyCycle(2.5)#backwards
time.sleep(.05)
p.ChangeDutyCycle(0)
time.sleep(1)
p.ChangeDutyCycle(7.5)
time.sleep(.15)
p.ChangeDutyCycle(0)
time.sleep(2)

#left
p.ChangeDutyCycle(7.5)
time.sleep(.15)
p.ChangeDutyCycle(0)
time.sleep(1)
p.ChangeDutyCycle(2.5)
time.sleep(.07)

p.stop()
GPIO.cleanup()
