import RPi.GPIO as GPIO 
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
p.start(0) # Initialization

p.ChangeDutyCycle(2.5)#backwards
time.sleep(0.08)
p.ChangeDutyCycle(0)
time.sleep(1)
p.ChangeDutyCycle(8)
time.sleep(0.15)
p.stop()
#time.sleep(.5)
GPIO.cleanup()

'''try:
  while True:
  	p.ChangeDutyCycle(5)#backwards

  	time.sleep(.25)
   	#p.ChangeDutyCycle(7.5)
 	#time.sleep(.5)
    	p.ChangeDutyCycle(8)
    	time.sleep(0.25)
except KeyboardInterrupt:
 p.stop()
 GPIO.cleanup()'''
