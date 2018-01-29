#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, sys, signal

def prepare_gpio():
    global led_status  
    global input_port, output_port
    input_port = 21
    output_port = 23
    
    GPIO.setmode(GPIO.BOARD)
    led_status = 0
    GPIO.setup(input_port, GPIO.IN)
    print ("GPIO port " + str(input_port) + " configured for input.")
    GPIO.setup(output_port, GPIO.OUT)
    print ("GPIO port " + str(output_port) + " configured for output.")
    GPIO.output(output_port, led_status)

def switch_on(port):
    print ("Key pressed signal received")
    global led_status
    led_status = not led_status
    GPIO.output(output_port, led_status)

def reset(signal, frame):
    if not in_reset:
        global in_reset
        in_reset = True
        print ("")
        print ("Received signal: " + str(signal) + ", frame: " + str(frame))
        print ("Reset GPIO.")
        time.sleep(1)
        GPIO.cleanup()
        print ("Program exit.")
        sys.exit(130)

def process():
    while True:
        time.sleep(5)

def main():
    # CTRL-C signal handler to end program
    global in_reset
    in_reset = False
    signal.signal(signal.SIGINT, reset)
    
    # Configure input and output port
    prepare_gpio()    
    
    # Callback for change GPIO input state
    GPIO.add_event_detect(input_port, GPIO.FALLING, bouncetime=200)
    GPIO.add_event_callback(input_port, switch_on)
    
    # Process input
    process()

if __name__ == "__main__":
    main()
