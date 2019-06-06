#!/usr/bin/env python
#this file should return both the value of the ph and the moisture of the soil
#since they are al being passed through the same  ADC
import PCF8591 as ADC
import time
import smbus

gradient = -0.114285714
intercept = 33.21128521

def measure():
    ADC.setup(0x48)
    bus = smbus.SMBus(1)
    reading = ADC.read(2)
    voltage = ADC.read(1)
    #ADC.write(ADC.read(0))
    value = ((0.641025641)*reading)
    moistureLevel = (100 - value)*2
    phValue = gradient * voltage + intercept 
    if moistureLevel > 100:
        moistureLevel = 100
    print(voltage,phValue)
    return moistureLevel, phValue

def destroy():
    ADC.write(0)

if __name__ == "__main__":
    try:
        while True:
            measure()
            time.sleep(2)
    except KeyboardInterrupt:
        destroy()
