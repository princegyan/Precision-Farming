#!/usr/bin/env python
import PCF8591 as ADC
import time
import smbus
import sqlite3 as sql


gradient = -0.114285714
intercept = 29.771428522
def setup():
	ADC.setup(0x48)

def loop():
	con = sql.connect("IoTDatabase.db")
	c = con.cursor()
	while True:
                bus = smbus.SMBus(1)
                voltage = ADC.read(1)
		#print (reading)
		#ADC.write(ADC.read(0))
		#value = ((0.641025641)*reading)
                phValue = gradient * voltage + intercept 
                localtime = time.asctime( time.localtime(time.time()) )
	#	c.execute('insert into soilpH(date, reading) values(?, ?)',(localtime,phValue))
	#	con.commit()
                print ("The ph is ", phValue)
#                f.close()        
 		time.sleep(2)
                
               

def destroy():
        con.close()
	ADC.write(0)

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
