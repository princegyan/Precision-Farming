from twilio.rest import Client
from ds18b20 import loop, sensor, read, kill
import sqlite3 as sql
from gy21 import humidity
import PCF8591 as ADC
from proposed import measure
from temp2 import read
import time
connection = sql.connect("IoTDatabase.db")
cur = connection.cursor()

#Twilio Account Details

account_sid = 'AC1c805cf3f05a5ab71eb7c21e35b7af33'
auth_token = 'd26f62278aae23748d78a7122674b71a'
client = Client(account_sid, auth_token)

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
            serialNum = sensor()
            localtime = time.asctime( time.localtime(time.time()) )
            cur.execute('insert into soilTemp(date, reading) values(?,?)', (localtime, float(loop(serialNum))))
            cur.execute('insert into humidity(date, reading) values(?,?)',(localtime, float(humidity())))
            time.sleep(1)
            cur.execute('insert into soilMoisture(date, reading) values(?,?)',(localtime, float(measure()[0])))
            cur.execute('insert into soilpH(date, reading) values(?,?)',(localtime, float(measure()[1])))
            cur.execute('insert into atmosphericTemp(date, reading) values(?,?)', (localtime, float(read())))
            connection.commit()
            print "Data successfully written"
            
            time.sleep(60)
            
    except KeyboardInterrupt:
        connection.close()
