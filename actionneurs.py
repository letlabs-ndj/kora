import RPi.GPIO as GPIO
from gpiozero import PWMLED
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
light = PMWLED(17)
GPIO.setup(LED, GPIO.OUT)

def actionner(state,sensorPin):
    if state:
        print('arrosage actif')
    else:
        print('arrosage non-actif')

    ledState = not state
    GPIO.output(sensorPin, ledState)

def ajusterLuminosite(val):
    light.value = val/100
