#!/usr/bin/python
import os, time
from Adafruit_LED_Backpack import SevenSegment

# Return CPU temperature as a character string                                      
def getCPUTemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def showCPUTemperature(segment):
    while True:
        cpu_temp = getCPUTemperature()
        print ("CPU Temperature: " + cpu_temp)
        segment.print_float(float(cpu_temp), decimal_digits=1)
        segment.write_display()
        time.sleep(1)
        
def initSegmentDisplay():
    segment = SevenSegment.SevenSegment(address=0x70)
    segment.begin()
    segment.clear()
    return segment
  
def main():
    segment = initSegmentDisplay()
    showCPUTemperature(segment)

if __name__ == "__main__":
    main()

