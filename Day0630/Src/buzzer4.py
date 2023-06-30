import RPi.GPIO as GPIO
import time

buzzerPin = 14
melody  = [261, 294, 329, 349, 392, 440, 493, 523]

#O = 1
#C = 261
#D = 294
#E = 329
#F = 349
#G = 392
#A = 440
#B = 493
#Cp = 523

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)
buzz.start(90.0)

try:
		while True:
			key = int(input())
			buzz.start(90)
			
			buzz.ChangeFrequency(melody[key])
			time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	


