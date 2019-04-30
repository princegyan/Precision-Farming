#!/usr/bin/env python
import PCF8591 as ADC
import time
import smbus

    

def measure():
    ADC.setup(0x48)
    bus = smbus.SMBus(1)
    reading = ADC.read(2)
    ADC.write(ADC.read(0))
    value = ((0.641025641)*reading)
    moistureLevel = (100 - value)*2
    if moistureLevel > 100:
        moistureLevel = 100
    return moistureLevel

def destroy():
    ADC.write(0)

if __name__ == "__main__":
    try:
        measure()
    except KeyboardInterrupt:
        destroy()
