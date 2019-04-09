#!/usr/bin/env python
import PCF8591 as ADC
import time


def setup():
	ADC.setup(0x48)

def loop():
	while True:
                reading = ADC.read(0)
		print ADC.read(0)
		print (reading)
		time.sleep(10)
		ADC.write(ADC.read(0))

def destroy():
	ADC.write(0)

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()