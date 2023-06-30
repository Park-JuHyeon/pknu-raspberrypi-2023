from flask import Flask, request, render_template
import Rpi.GPIO as GPIO

ledpin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledpin, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def home():
	return "Hello Flask!"

@app.route('/led/on')
def Led_On():
	try:
		GPIO.output(ledpin, GPIO.HIGH)
		return 'ok'
	except:
		return 'fail'

@app.route('/led/off')
def Led_Off():
	try:
		GPIO.output(ledpin, GPIO.LOW)
		return 'ok'
	except:
		return 'fail'

@app.route('/led')
def led_onoff():
	return render_template('led.html')

@app.route('/test')
def get():
	return render_template('get.html')

@app.route('/post')
def post():
	return render_template('default.html')

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 8800, debug=True)

