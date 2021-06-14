
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

