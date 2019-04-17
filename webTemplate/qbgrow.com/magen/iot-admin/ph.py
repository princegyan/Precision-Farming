import Adafruit_ADS1x15

import time

adc = Adafruit_ADS1x15.ADS1115()

gain = 1

while True:
    value = adc.read_adc(0,gain)
    print ("====================")
    pHVoltage = (value)*(5.0)/1024/6;
    pHValue = -3.70 * (pHVoltage) + 19.34;
    print('Value is: ', value)
##    print (' voltage: ', pHVoltage)
##    print (' pH: ', pHValue)    
    time.sleep(5)
    
##    avgValue+=buf[i];
##    float pHVol=(float)avgValue*5.0/1024/6;
##    float phValue = -5.70 * pHVol + 21.34;
