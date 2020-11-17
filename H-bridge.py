import RPi.GPIO as GPIO
import time

RelayOne = 12
RelayTwo = 16

def forward():
    GPIO.output(RelayOne, GPIO.HIGH)
    GPIO.output(RelayTwo, GPIO.LOW)

def backward():        
    GPIO.output(RelayOne, GPIO.LOW)
    GPIO.output(RelayTwo, GPIO.HIGH)
    
def stop():
    GPIO.output(RelayOne, GPIO.HIGH)
    GPIO.output(RelayTwo, GPIO.HIGH)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RelayOne, GPIO.OUT)
    GPIO.setup(RelayTwo, GPIO.OUT)
    
print "starting"
setup()
while True:
    print "forward"
    forward()
    time.sleep(2)
    print "backward"
    backward()
    time.sleep(2)
    print "stop"
    stop()
    time.sleep(5)
'''UnoRelay = GPIO.PWM(RelayOne,50) 
UnoRelay.start(0)
DosRelay = GPIO.PWM(RelayTwo,50)
DosRelay.start(0)

UnoRelay.ChangeDutyCycle(7.5)
time.sleep(1)
DosRelay.ChangeDutyCycle(0)
time.sleep(1)

def forward():
    UnoRelay.ChangeDutyCycle(7.5)
    time.sleep(1)
    DosRelay.ChangeDutyCycle(0)
    time.sleep(1) 

try:
	while True:
	    print "forward"
	    forward()
	    time.sleep(2)
except KeyboardInterrupt:
	UnoRelay.stop()
	DosRelay.stop()
	GPIO.cleanup()  '''

