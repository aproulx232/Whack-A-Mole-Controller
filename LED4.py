import RPi.GPIO as GPIO
import time
import random
def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(22,GPIO.OUT)#L1
	GPIO.setup(25,GPIO.IN)#B1
	GPIO.setup(6,GPIO.OUT)#L2
	GPIO.setup(12,GPIO.IN)#B2
	GPIO.setup(5,GPIO.OUT)#L3
	GPIO.setup(24,GPIO.IN)#B3
	GPIO.setup(27,GPIO.OUT)#L4
	GPIO.setup(23,GPIO.IN)#B4
	GPIO.setup(17,GPIO.OUT)#L5
	GPIO.setup(18,GPIO.IN)#B5

	total = 0
	difficulty = 70
	time.sleep(1)
	for index in range(0,10):
		Rnum = random.randrange(1,6)
		print "Rnum", Rnum
		time.sleep(1)
		if Rnum ==1:
			total += mole1(difficulty)
		if Rnum ==2:
			total += mole2(difficulty)
		if Rnum ==3:
			total += mole3(difficulty)
		if Rnum ==4:
			total += mole4(difficulty)
		if Rnum ==5:
			total += mole5(difficulty)
	print "FINAL SCORE: ",total

def mole1 (difficulty):
	print "mole 1"
	total = mole(22,25, difficulty)
	return total
def mole2 (difficulty):
	print "mole 2"
	total = mole(6,12, difficulty)
	return total
def mole3 (difficulty):
	print "mole 3"
	total = mole(5,24, difficulty)
	return total
def mole4(difficulty):
	print "mole 4"
	total = mole(27,23, difficulty)
	return total
def mole5(difficulty):
	print "mole 5"
	total = mole(17,18, difficulty)
	return total


def mole(Lnum , Bnum, diff):	
	loop = 0

	GPIO.output(Lnum,GPIO.HIGH)
	L = 1
	sc = 0
	print "LED ON"
	while loop <= diff:
		if L == 1: 
			B = GPIO.input(Bnum)
			if B == 1:
				print "score "
				sc = 1
		time.sleep(0.01)
		loop += 1
	GPIO.output(Lnum,GPIO.LOW)
	return sc
main()
GPIO.cleanup()

