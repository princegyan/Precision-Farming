import Adafruit_ADS1x15

import time

adc = Adafruit_ADS1x15.ADS1115()


while True:
    #print 'Value : ', adc.read_adc(0, 1)
    reading = adc.read_adc(0, 1)
    vol = ((reading)/10000) - 3
    localtime = time.asctime( time.localtime(time.time()) )
    f = open("moistureCollector.txt","a")

    level = vol*-31.25
    print "Moisture level: {:>5} %".format(level)
    f.write(str(localtime)+ '\t')
    f.write(str(level)+'\n')
    time.sleep(50)
    #print 'Converted value : ', adc.start_adc(0, 1)
