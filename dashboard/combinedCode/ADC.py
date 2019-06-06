import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

phgradient = -0.3289
phintercept = 26.469
moistgradient = -4.3302
moistintercept = 195.82

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
phchan = AnalogIn(ads, ADS.P0)
moistchan = AnalogIn(ads, ADS.P1)


# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#print("{:>5}\t{:>5}".format('raw', 'v'))
def measure():
    #while True:
    #print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    voltage = phchan.voltage
    phValue = phgradient * voltage + phintercept
        #print("pH ", phValue)
    
    moistvoltage = moistchan.voltage
    moistureValue = moistgradient * moistvoltage + moistintercept
    if moistureValue <= 0:
        moistureValue = 0
        #print("Moisture Level ", moistureValue,"%")
    time.sleep(0.5)
    #print("Ph ", phValue)
    #print("Moisture ", moistureValue)
    return phValue, moistureValue


#measure()
