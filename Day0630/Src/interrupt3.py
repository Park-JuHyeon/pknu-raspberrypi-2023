import RPi.GPIO as GPIO
import time

buzzerPin = 14
switchPin = 13
ledpin = 18

sound = [294, 523, 493, 440 ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(ledpin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)

def callbackfunc(channel):
  print("Interrupt !!")
	

GPIO.add_event_detect(switchPin, GPIO.RISING, callback=callbackfunc)

try:
  while True:
    buzz.start(50)
    for i in range(0, len(sound)):
    	buzz.ChangeFrequency(sound[i])

    buzz.stop()
    
except KeyboardInterrupt:
  GPIO.cleanup()
