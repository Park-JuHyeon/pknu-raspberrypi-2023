import RPi.GPIO as GPIO
import time

buzzerPin = 14
melody  = [131, 147, 165, 175, 196, 220, 247, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)
buzz.start(90.0)

twinkle = [1,1,5,5,6,6,5,4,4,3,3,2,2,1, 
					5,5,4,4,3,3,2,5,5,4,4,3,3,2,
					1,1,5,5,6,6,5,4,4,3,3,2,2,1]

try:
		for i in range(0,len(twinkle)):
			buzz.ChangeFrequency(melody[twinkle[i]])
			if i == 6 or i == 13 or i == 20 or i == 27 or i==34 or i == 41:
				time.sleep(1.0)		# 2분음표 1초동안

			else:
				time.sleep(0.5)		# 4분음표 0.5초 동안
		buzz.stop()

finally :
	GPIO.cleanup()
				
