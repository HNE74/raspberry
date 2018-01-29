#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep

# Prepare GPIO
GPIO.setmode(GPIO.BOARD)
red = 3
green = 5
blue = 7
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Turn all colors off
def all_off(pwm_r, pwm_g, pwm_b):
    pwm_r.ChangeDutyCycle(0)
    pwm_g.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)
    
    GPIO.output(red, False)
    GPIO.output(green, False)
    GPIO.output(blue, False)
    return

def do_mix(pwm_r, pwm_g, pwm_b):
    while True:
        dcr = eval(input("Red [0-100]:\n"))
        dcg = eval(input("Green [0-100]:\n"))
        dcb = eval(input("Blue [0-100]:\n"))

        pwm_r.ChangeDutyCycle(dcr)
        pwm_g.ChangeDutyCycle(dcg)
        pwm_b.ChangeDutyCycle(dcb)
        print("==========================")

def duty_cycle_change(pwm):
        for i in range(100):
            pwm.ChangeDutyCycle(i)
            sleep(0.05)
            if i == 99:
                for j in range(100, 0, -1):
                    sleep(0.05)
                    pwm.ChangeDutyCycle(j)

def do_auto(pwm_r, pwm_g, pwm_b):
    while True:
        print("Red cylcle")
        duty_cycle_change(pwm_r)
        print("Green cylcle")        
        duty_cycle_change(pwm_g)
        print("Blue cylcle")        
        duty_cycle_change(pwm_b)
        print("==========================")        
        
# Set PWM to 100 Hz
pwm_r=GPIO.PWM(red, 100)
pwm_g=GPIO.PWM(green, 100)
pwm_b=GPIO.PWM(blue, 100)

# Set PWM start values
pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

# Select mode
selection = eval(input("[1] Mix   [2] Auto\n"))

try:
    if selection == 1:
        do_mix(pwm_r, pwm_g, pwm_b)
    elif selection == 2:
        do_auto(pwm_r, pwm_g, pwm_b)
except KeyboardInterrupt:
    all_off(pwm_r, pwm_g, pwm_b)
        
    
