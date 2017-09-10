import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

str = raw_input("enter 1 or 2: ")
print "received input: " + str
if str == "1":
	GPIO.output(18,GPIO.HIGH)
if str == "2":
	GPIO.output(23,GPIO.HIGH)
time.sleep(2)
print "LED off"
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
#set other segments on
