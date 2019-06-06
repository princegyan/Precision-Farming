from call import callUser
#from ds18b20 import loop, sensor, read, kill
import sqlite3 as sql
from gy21 import humidity

from ADC import measure

from temp2 import read
import time
connection = sql.connect("IoTDatabase.db")
cur = connection.cursor()

#Twilio Account Details

'''message = client.messages \
                .create(
                     body="This Is From IntelFarm...{{label}} needs to attended to check the latest reading {{label}}{{reading}} here {{weblink}}",
                     from_='+19513833556',
                     to='+233274008316'
                 )

print(message.sid)
'''

'''call = client.calls.create(
                        url='http://10.10.64.13:8000', #this links to voice to be played
                     from_='+19513833556',
                     to='+233274008316'
                    )

print(call.sid)
'''

if __name__ == '__main__':
    try:
        while True:
            atmtemp = float(read())
            soilph = float(measure()[0])
            humid = float(humidity())
            soilmoist = float(measure()[1])
            soiltemp = atmtemp-1.53
            if soilph < 5:
                callUser()
                print("Soil ph")
            if atmtemp > 35:
                callUser()
                print("atm temp")
            if humid > 45:
                callUser()
                print("humid")
            if soilmoist < 20:
                callUser()
                print("soil moist")
            if soiltemp > 36:
                callUser()
                print("Soil temp")
            
            #serialNum = sensor()
            localtime = time.asctime( time.localtime(time.time()) )
            cur.execute('insert into soilTemp(date, reading) values(?,?)', (localtime, (atmtemp-1.5)))
            cur.execute('insert into humidity(date, reading) values(?,?)',(localtime, float(humidity())))
            time.sleep(1)
            cur.execute('insert into soilMoisture(date, reading) values(?,?)',(localtime, float(measure()[1])))
            cur.execute('insert into soilpH(date, reading) values(?,?)',(localtime,soilph ))
            cur.execute('insert into atmosphericTemp(date, reading) values(?,?)', (localtime, read()))
            connection.commit()
            print("Data")
            time.sleep(60)
            
    except KeyboardInterrupt:
        connection.close()
    finally:
        print("Exiting gracefully")
