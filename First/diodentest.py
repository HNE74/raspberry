#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
print ("GPIO Port 11 für Ausgabe konfiguriert.")

done = False
while not done:
	print ("Diode an")
	GPIO.output(11, GPIO.HIGH)
	try:
		time.sleep(2)
	except KeyboardInterrupt:
		done = True
		break

	print ("Diode aus")
	GPIO.output(11, GPIO.LOW)
	try:
		time.sleep(2)
	except KeyboardInterrupt:
		done = True;



print ("GPIO zurücksetzen.")
GPIO.cleanup()

