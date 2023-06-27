
## 1/2일차
- 라즈베리파이 학습
   - 라즈베리파이 소개
   - 라즈비안 설치
      - Bulleseye
   - 라즈비안 설정
      - 기본 업데이트/업그레이드
      - 한글 폰트 및 입력기
      - 스크린세이버, 와이파이 연결 끊김 해제
   - pi-apps 설치
      - Visual Studio Code 설치
      - Github Desktop 설치 및 설정
      - Visual Studio Code
         - Python 플러그인
      - 리눅스 기본
         - 리눅스 명령어(대표 20여가지)

## 3일차
- 라즈베리파이 학습
   - 통신 설정
      - AnyDesk 실패
   - 리눅스 일반
      - 서비스 실행, 확인, 종료
         - systemctl [start|stop|status] 서비스명
      - MySQL DB
   - Flask 기본
   
## 4일차
- 라즈베리파이 학습
   - PyQt5 설치
   - QtDesigner 설치 및 실행확인
   - 하드웨어 제어 - GPIO

## 5일차
- 라즈베리파이 학습
   - 네트워크 셋팅(VNC)
   - RGB LED / Button 클릭
   
## 6일차
- 라즈베리파이 학습
   - MQTT 통신
      - MQTT Broker IP, port 설정, 계정설정(옵션)
      - RPi <--> WPF
      - RPi 온습도 센서값 MQTT 전송
      - WPF 모터, LED 제어값 전송
      - DPi Python paho-mqtt 패키지
      - WPF C# M2Mqtt 패키지

라즈베리파이 테스트 결과

<img
src="https://raw.githubusercontent.com/Park-JuHyeon/pknu-raspberrypi-2023/main/images/raspberrypi01.jpg" width="700">

WPF 모니터링, 컨트롤화면

<img
src="https://raw.githubusercontent.com/Park-JuHyeon/pknu-raspberrypi-2023/main/images/raspberrypi02.png" width="700">

## 7일차
- 라즈베리파이 학습
   - 파이 카메라 v1.3 ov5647
   - OpenCV 4.7
   - 카메라 연동 및 QRcode

## Day0626
- 라즈베리파이 학습
   - 7segment와 스위치 활용
      - 스위치 클릭 시 7segment값 1씩 증가.

## Day0627
- 라즈베리파이 학습
   - switch 활용한 Led/buzzer제어
      - Buzzer : 주파수 활용해 노래 출력
      - Led : 스위치 클릭시 LED 제어

- 학습내용정리
   - RPI GPIO Interrupt

   - 핀설정
      - GPIO.add_event_detect(channel, GPIO.Mode)
      - channel : Pin number
      - GPIO.Mode : RISING or FALLING or BOTH
   - 콜백함수 설정
      - GPIO.add_event_callback(channel, function)
         - channel: Pin number
         - function : call back function

   - 하나의 인터럽트 사용시
   - GPIO.add_event_detect(channel, GPIO.Mode, callback=my_callback) : my_callback은 정의하는 함수

   - LED를 제어하는 출력문구는 GPIO.output(핀넘버, True/False) : True: led on , False : led off
   - Buzzer를 제어하는 출력문구는 ChangeFrequency(선언한 주파수)
   - GPIO.setup전 GPIO.setmode(GPIO.BCM/BOARD) 필수