'''
This is a proposed code for the ph

Dennis Effa Amponsah
Prince Alfred Gyan

'''


#!/usr/bin/env python
import PCF8591 as ADC
import time
import smbus


m = -12.4   #this is also a dummy data
b = 3.3    #this is dummy data

def setup():
	ADC.setup(0x48)

def loop():

	while True:
                bus = smbus.SMBus(1)
                volatge = ADC.read(2)

                #usig the linear equation  y = mx + b
                ph = m * volatge + b
		ADC.write(ADC.read(0))
        # y = mx + b 
        print(ph)
		
               

def destroy():
	ADC.write(0)

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
