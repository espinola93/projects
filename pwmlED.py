import RPi.GPIO as GPIO
import time

servoPIN = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
p.start(0) # Initialization
'''number=10
for x in range(6):
	p.ChangeDutyCycle(100)#backwards
	time.sleep(2)
	p.ChangeDutyCycle(5)
	time.sleep(2)
time.sleep(1)	
p.stop()
GPIO.cleanup()'''
time_=0.5
try:
  while True:
  	p.ChangeDutyCycle(100)#backwards
  	time.sleep(time_)
   	'''p.ChangeDutyCycle(90)
 	time.sleep(time_)
    	p.ChangeDutyCycle(80)
    	time.sleep(time_)
	p.ChangeDutyCycle(70)#backwards
  	time.sleep(time_)
   	p.ChangeDutyCycle(60)
 	time.sleep(time_)
    	p.ChangeDutyCycle(50)
    	time.sleep(time_)
	p.ChangeDutyCycle(40)#backwards
  	time.sleep(time_)
   	p.ChangeDutyCycle(30)
 	time.sleep(time_)
    	p.ChangeDutyCycle(20)
    	time.sleep(time_)
	p.ChangeDutyCycle(10)
    	time.sleep(time_)
	

	p.ChangeDutyCycle(10)#backwards
  	time.sleep(time_)
   	p.ChangeDutyCycle(20)
 	time.sleep(time_)
    	p.ChangeDutyCycle(30)
    	time.sleep(time_)
	p.ChangeDutyCycle(40)#backwards
  	time.sleep(time_)
   	p.ChangeDutyCycle(50)
 	time.sleep(time_)
    	p.ChangeDutyCycle(60)
    	time.sleep(time_)
	p.ChangeDutyCycle(70)#backwards
  	time.sleep(time_)
   	p.ChangeDutyCycle(80)
 	time.sleep(time_)
    	p.ChangeDutyCycle(90)
    	time.sleep(time_)'''
	p.ChangeDutyCycle(0)
    	time.sleep(time_)
	
	

except KeyboardInterrupt:
 p.stop()
 GPIO.cleanup()

