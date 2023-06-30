import RPi.GPIO as GPIO
import time

trig = 23
echo = 24 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("초음파 거리 측정기")

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, False)
#print("초음파 출력 초기화)
time.sleep(2)

try:
	while True:
		GPIO.output(trig, True)
		time.sleep(0.0001)
		GPIO.output(trig, False)

		while GPIO.input(echo)==0:
			start = time.time()

		while GPIO.input(echo) == 1:
			stop = time.time()

		check_time = stop - start
		distance = check_time * 34300 / 2
		print("Distance : %.1f cm" % distance)
		time.sleep(0.4)

except KeyboardInterrupt:
	print("거리 측정 완료")
	GPIO.cleanup()
