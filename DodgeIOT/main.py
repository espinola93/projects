import RPi.GPIO as GPIO
import time
import HBridge as RearWheels
import lightsRelay as Lights
import reverseLights as RLights
import breakLights as Break
import paho.mqtt.client as mqtt
import steerServo as steering
import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

up = 46
down = 32
left = 18
right = 33

start = 317
select = 318

lTrig = 311
rTrig = 310

#prints out device info at start
print(gamepad)

class car:

        def __init__(self):
                print("Car has been initiated")
        def setupRearWheels(self):
		RearWheels.setup()

	def forward(self):
                print("forward")
                RearWheels.forward()
        def backward(self):
                print("reverse")
	        RearWheels.backward()
        def left(self):
                print("left")
		steering.steerLeft()

        def right(self):
                print("right")
		steering.steerRight()

        def quit(self):
		print("Cleaning and exiting")
                time.sleep(0.5)
                GPIO.cleanup()
                exit()
        def lightsOn(self):
                Lights.LightsOn()
	def lightsOff(self):
		Lights.LightsOff()
        def stopLight(self):
		RearWheels.stop()
		Break.BreakLightsOn()
		time.sleep(5)

ram=car()

ram.setupRearWheels()
Lights.LightsRelaySetup()
RLights.ReverseLightsSetup()
Break.BreakLightsSetup()
#steering.steeringSetup()

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == yBtn:
                print("Y")
		ram.forward()
		RLights.ReverseLightsOff()
		RLights.ReverseLightsOn
            elif event.code == bBtn:
                print("B")
                ram.right()

            elif event.code == aBtn:
                print("A")
		ram.backward()
		RLights.ReverseLightsOn()
            elif event.code == xBtn:
                print("X")
                ram.left()
                #time.sleep(2)
                #GPIO.cleanup()
            elif event.code == up:
                print("up")
            elif event.code == down:
                print("down")
            elif event.code == left:
                print("left")
            elif event.code == right:
                print("right")

            elif event.code == start:
                print("start")
		ram.quit()
            elif event.code == select:
                print("select")
		ram.stopLight()
            elif event.code == lTrig:
                print("left bumper")
		ram.lightsOn()
            elif event.code == rTrig:
                print("right bumper")
		ram.lightsOff()

'''
loop=True


while loop:          ## While loop which will keep going until loop = False

        print 30*"*","CONTROL MENU",30*"*"
        print 30*" ","FORWARD(w)",30*" "
        print 25*" ","<LEFT(a)",7*" ","RIGHT>(d)"
        print 30*" ","REVERSE(S)",30*" ","\n"
        print 30*"*","QUIT(0)",30*"*"

        choice = input("Choice ")

        if choice==1:
                print "Going forward"
                ram.forward()
                time.sleep(0.5)
        elif choice==2:
                print "Going backward"
                RLights.ReverseLightsOn()
		ram.backward()
                time.sleep(0.5)
        elif choice==3:
                print "Going left"
                ram.left()
                
        elif choice==4:
                print "Going right"
                ram.right()

        elif choice==5:
                ram.quit()
                time.sleep(0.5)
                loop=False # This will make the while loop to end as not value of loop is set to False
        elif choice==6:
                ram.lightsOn()
		time.sleep(0.5)
	elif choice==7:
		ram.lightsOff()
		time.sleep(0.5)
	elif choice==8:
		ram.stopLight()
		
        else:
                # Any integer inputs other than values 1-5 we print an error message
                raw_input("Wrong option selection. Enter any key to try again..")

'''



