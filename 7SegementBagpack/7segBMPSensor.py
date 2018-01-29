#!/usr/bin/python
import os, time
from Adafruit_LED_Backpack import SevenSegment
import Adafruit_BMP.BMP085 as BMP085

def showCPUTemperature(segment):
    state = 0
    read = None
    while True:
        segment = initSegmentDisplay()
        if state == 0:
            read = sensor.read_temperature()
            digits = 1
            segment.print_float(read, decimal_digits=digits)
            state = 1
        else:
            read = sensor.read_pressure() / 100
            if read >= 1000.0:
                digits = 0
            else:
                digits = 1
            state = 0
        
        segment.print_float(read, decimal_digits=digits)
        segment.write_display()        
        time.sleep(10)
        
def initSegmentDisplay():
    segment = SevenSegment.SevenSegment(address=0x70)
    segment.begin()
    segment.clear()
    return segment
  
def main():
    global sensor
    sensor = BMP085.BMP085()    
    segment = initSegmentDisplay()
    showCPUTemperature(segment)

if __name__ == "__main__":
    main()

