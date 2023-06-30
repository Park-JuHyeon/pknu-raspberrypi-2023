import RPi.GPIO as GPIO
import time

trig = 23
echo = 24
buzzer = 14

melody = 800

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("초음파 거리 측정기")

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

buzz = GPIO.PWM(buzzer, 440)

GPIO.output(trig, False)
#print("초음파 출력 초기화)
time.sleep(2)

try:
  while True:
  # 구형파 발생
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.0001)
    GPIO.output(trig, GPIO.HIGH)

    while GPIO.input(echo)==0:		# 펄스 발생
      start = time.time()

    while GPIO.input(echo) == 1:	# 펄스 돌아옴
      stop = time.time()

    check_time = stop - start
    distance = check_time * (34300 / 2)
    print("Distance : %.2f cm" % distance)	# 거리 출력
    time.sleep(0.4)

    if(distance <= 40 and distance > 25):
    	buzz.start(50)
    	buzz.ChangeFrequency(melody)
    	time.sleep(0.3)
    	buzz.stop()
    	time.sleep(0.3)

    elif(distance <= 25 and distance > 10):
    	buzz.start(50)
    	buzz.ChangeFrequency(melody)
    	time.sleep(0.15)
    	buzz.stop()
    	time.sleep(0.1)

    elif(distance <=10):
    	buzz.start(50)
    	buzz.ChangeFrequency(melody)
    	time.sleep(0.05)
    	buzz.stop()
    	time.sleep(0.05)
    else:
    	buzz.stop()
    	time.sleep(0.5)

except KeyboardInterrupt:
	print("거리 측정 완료")
	GPIO.cleanup()
