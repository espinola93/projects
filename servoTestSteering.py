import RPi.GPIO as GPIO
import time

servoPIN = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
p.start(0) # Initialization

p.ChangeDutyCycle(2.5)#backwards
time.sleep(0.14)
#p.ChangeDutyCycle(7.5)
#time.sleep(0.25)
#p.ChangeDutyCycle(12.5)
#time.sleep(0.14)

p.stop()
GPIO.cleanup()

"""try:
  while True:
  	p.ChangeDutyCycle(2.5)#backwards
	time.sleep(0.28)
	p.ChangeDutyCycle(7.5)
	time.sleep(0.25)
	p.ChangeDutyCycle(12.5)
	time.sleep(0.27)

except KeyboardInterrupt:
 p.stop()
 GPIO.cleanup()"""