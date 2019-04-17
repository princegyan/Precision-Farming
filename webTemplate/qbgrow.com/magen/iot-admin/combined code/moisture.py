#!/usr/bin/env python
import PCF8591 as ADC
import time
import smbus
#import sqlite3 as sql


#def setup():
    

def measure():
    ADC.setup(0x48)
    bus = smbus.SMBus(1)
    reading = ADC.read(2)
#		print (reading)
    ADC.write(ADC.read(0))
    value = ((0.641025641)*reading)
    moistureLevel = (100 - value)*2
		#print (value)
    #print('Soil Moisture is %f%%'%(moistureLevel))
    return moistureLevel
        #localtime = time.asctime( time.localtime(time.time()) )
	#c.execute('insert into soilMoisture(date, reading) values(?, ?)',(localtime,moistureLevel))
	#con.commit()
#                f = open("moistureCollector.txt", "a")
#                f.write(str(localtime)+ '\t')
#                f.write(str(moistureLevel)+'\n')
#                f.close()        
 	#time.sleep(60)
        
#def run():
#    setup()
#    measure()

def destroy():
    ADC.write(0)

if __name__ == "__main__":
    try:
        measure()
    except KeyboardInterrupt:
        destroy()
