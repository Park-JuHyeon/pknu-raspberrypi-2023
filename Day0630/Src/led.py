import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)

GPIO.setup(18, GPIO.IN)

try:
	while True:
		input_state = GPIO.input(18)
		if input_state == False:
			GPIO.output(13, GPIO.HIGH)
		else:
			GPIO.output(13, GPIO.LOW)

except KeyboardInterrupt:
	GPIO.cleanup()		
