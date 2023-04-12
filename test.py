import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.OUT,initial=GPIO.LOW)
try:
	while True:
		GPIO.output(25,GPIO.HIGH)
		print("on")
		sleep(5)
		GPIO.output(25,GPIO.LOW)
		print("off")
		sleep(5)
except KeyboardInterrupt:
	GPIO.cleanup()
