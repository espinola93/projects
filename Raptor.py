import RPi.GPIO as GPIO 
import time

rservoPIN = 15 #rear wheels 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rservoPIN, GPIO.OUT)
rearServo = GPIO.PWM(rservoPIN, 50) # GPIO 11 for PWM with 50Hz
rearServo.start(0) # Initialization

fservoPIN = 11 #front wheels
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fservoPIN, GPIO.OUT)
frontServo = GPIO.PWM(fservoPIN, 50) # GPIO 11 for PWM with 50Hz
frontServo.start(0) # Initialization


class car:
	
	def __init__(self):
		print("Car has been initiated")
	def forward(self):
		print("forward")
		rearServo.ChangeDutyCycle(8)
	def backward(self):
		print("reverse")
		rearServo.ChangeDutyCycle(2.5)#backwards
	def left(self):
		print("left")
		frontServo.ChangeDutyCycle(8)
	def right(self):
		print("right")
		frontServo.ChangeDutyCycle(2.5)
		#time.sleep(0.5)
	def center(self):
		print("center")
		frontServo.ChangeDutyCycle(2.5)
		
		
	def quit(self):
		rearServo.stop()
		time.sleep(0.5)
		frontServo.stop()
		GPIO.cleanup()
		exit()
	def tozero(self):
		frontServo.ChangeDutyCycle(0)
	def othercenter(self):
		frontServo.ChangeDutyCycle(8)
	def brake(self):
		rearServo.stop()   		
raptor=car()

loop=True      

while loop:          ## While loop which will keep going until loop = False
    
	print 30*"*","CONTROL MENU",30*"*"
	print 30*" ","FORWARD(w)",30*" "
	print 25*" ","<LEFT(a)",7*" ","RIGHT>(d)"
	print 30*" ","REVERSE(S)",30*" ","\n"
	print 30*"*","QUIT(0)",30*"*"
	
	choice = input(" ")
     
	if choice==1:     
	        print "Going forward"
       		raptor.forward()	
		time.sleep(0.5)	
  	elif choice==2:
        	print "Going backward"
		raptor.backward()
		time.sleep(0.5)
	elif choice==3:
	      	print "Going left"
		raptor.left()
		time.sleep(0.5)
		raptor.center()
		time.sleep(0.3)
		raptor.tozero()
		
				
	elif choice==4:
        	print "Going right"
		raptor.right()
		time.sleep(0.3)
		raptor.othercenter()
		time.sleep(0.3)
		raptor.tozero()
		
      	elif choice==5:
     	   	raptor.quit()
		time.sleep(0.5)
		loop=False # This will make the while loop to end as not value of loop is set to False
    	elif choice==6:
		print("BRAKE")
		raptor.brake()
		time.sleep(0.5)
	else:
        	# Any integer inputs other than values 1-5 we print an error message
        	raw_input("Wrong option selection. Enter any key to try again..")



