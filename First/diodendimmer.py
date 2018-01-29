#!/usr/bin/python3
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 100)
pwm.start(50)

while True:
    dc = input("DC eingeben von 0 bis 100:")
    pwm.ChangeDutyCycle(int(dc))

GPIO.cleanup()