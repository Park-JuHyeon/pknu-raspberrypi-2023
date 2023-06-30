import RPi.GPIO as GPIO
import time

buzzerPin  =14
melody = [131, 147, 165, 175, 196, 220, 247, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)   # 440Hz 를 갖는 객체 생성
try:
  while True:
    buzz.start(50)
    buzz.ChangeFrequency(melody[2])   # 주파수 변경
    time.sleep(0.5)

    buzz.ChangeFrequency(melody[1])
    time.sleep(0.3)

    buzz.ChangeFrequency(melody[0])
    time.sleep(0.3)

    buzz.ChangeFrequency(melody[1])
    time.sleep(0.3)

    buzz.ChangeFrequency(melody[2])
    time.sleep(0.3)

    buzz.ChangeFrequency(melody[2])
    time.sleep(0.3)

    buzz.ChangeFrequency(melody[2])
    time.sleep(0.5)

    buzz.ChangeFrequency(melody[1])
    time.sleep(0.3)

except KeyboardInterrupt:   # 키보드인터럽트
  GPIO.cleanup()
