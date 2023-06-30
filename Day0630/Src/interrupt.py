import RPi.GPIO as GPIO
import time

switchPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN)

def callbackfunc(channel):
	print("Interrupt !!")

GPIO.add_event_detect(switchPin, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
