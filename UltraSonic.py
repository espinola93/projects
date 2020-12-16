import RPI.GPIO as GPIO
import time

#GPIO MODE
GPIO.setmode(GPIO.BOARD)

#GPIO PINS
GPIO_TRIGGER = 11
GPIO_ECHO = 17

#set GPIO irection (In/Out)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
	#set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)
	
	#set Trigger after 0.01ms to low
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER False)
		
	StartTime = time.time()
	StopTime = time.time()
		
	#save StartTime	
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
	#save time of arrivl
	while GPIO.input(GPIO_ECHO == 1:
		StopTime = time.time() 

	#difference b/w start and arrival
	TimeElapsed = StopTime - StartTime
	#multiply w/ sonic speed (34300 cm/s)
	#and devide/2
	distance = (TimeElapse * 34300)/2
	
	return distance

if __name__ == '__main__'
	try:
		while True:
			dist = distance()
			print ("measured Distance = %.1f cm" % dist)
			time.sleep(1)
	
	#reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stoppe by User")
		GPIO.cleanup()
