#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, sys, signal
from pygame import mixer

diode_port = [3, 5, 7, 8]

def prepare_gpio():
    GPIO.setmode(GPIO.BOARD)
    for port in diode_port:
        GPIO.setup(port, GPIO.OUT)
        print ("GPIO Port " + str(port) + " configured for output.")
    print ("")    

def off(port, sleep):
        print ("Diode port " + str(port) + " off")
        GPIO.output(port, GPIO.LOW)
        time.sleep(sleep)     

def on(port, sleep):
        print ("Diode port " + str(port) + " off")
        GPIO.output(port, GPIO.HIGH)
        time.sleep(sleep)     

def on_off(port, sleep):
        on(port, sleep)
        off(port, sleep)                  

def right_left():
    for port in reversed(diode_port):
        on_off(port, 0.05)
    
def left_right():
    for port in diode_port:
        on_off(port, 0.05)
        
def knight_rider():
    mixer.init()
    mixer.music.load("./Knight-Rider-Theme-Song.mp3")
    mixer.music.play()    
    
    pos = 0
    delta = 1
    while True:
        port = diode_port[pos]
        on_off(port, 0.05)
               
        if pos >= len(diode_port)-1:
            delta = -1
        elif pos == 0:
            delta = 1
        pos = pos + delta

def reset(signal, frame):
    if not in_reset:
        global in_reset
        in_reset = True
        print ("")
        print ("Received signal: " + str(signal) + ", frame: " + str(frame))
        print ("Reset GPIO.")
        for port in diode_port:
            GPIO.output(port, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
        print ("Program exit.")
        sys.exit(130)

def process(pattern):
    while True:
        pattern()
        
def select_pattern():
    result = None
    while result == None:
        print ("")
        print ("Please select diode pattern to be processed:")
        print ("[1] = Left to right")
        print ("[2] = Right to left")
        print ("[3] = Knight rider")
        sel = input(">")
        
        sel = str(sel)
        if sel == '1':
            return left_right
        elif sel == '2':
            return right_left
        elif sel == '3':
            return knight_rider
        else:
            print ("Invalid selection!")
            sel = None

def main():
    global in_reset
    in_reset = False
    signal.signal(signal.SIGINT, reset)
    prepare_gpio()
    pattern = select_pattern()    
    process(pattern)

if __name__ == "__main__":
    main()
