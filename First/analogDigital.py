#!/usr/bin/python3
import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

while True:
    antwort = spi.xfer([1,128,0])
    if 0 <= antwort[1] <=3:
        print(antwort[0] + antwort[1] + antwort[2])
        wert = ((antwort[1] * 256) + antwort[2]) * 0.00322
        print(str(wert) + " V")
        time.sleep(1)
        