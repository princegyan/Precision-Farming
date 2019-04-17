

#--------------------------------------------------------------------------------------------------
#
#
#
#--------------------------------------------------------------------------------------------------
#!/usr/bin/python
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import time
 
#GPIO SETUP
pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
 
def callback(pin):
        if GPIO.input(pin):
                print ("Water Not Detected!")
        else:
                print ("Water Detected!")
 
#GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(pin, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        callback(pin)
        level = Adafruit_ADS1x15.read_adc(5)
        print ("Moisture level: {:>5} ".format(level))
        time.sleep(5)
    
        time.sleep(5)
