import RPi.GPIO as GPIO
import time

swPin = 13
ledpin = 18
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledpin, GPIO.OUT)

def callbackfunc(channel):
  print("Interrupt !!")
  
	if flag == False:
		flag = True
	else:
		flag = False
	
GPIO.add_event_detect(switchPin, GPIO.RISING, callback=callbackfunc)

try:
  while True:

	 if flag == True:
	 	GPIO.output(ledpin, True)

	 else:
	 	GPIO.output(ledpin, False)
	    	
except KeyboardInterrupt:
  GPIO.cleanup()
