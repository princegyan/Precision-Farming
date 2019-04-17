from ds18b20 import loop, sensor, read, kill
import sqlite3 as sql
from gy21 import humidity
import PCF8591 as ADC
from moisture import measure
from temp2 import read
import time
connection = sql.connect("IoTDatabase.db")
cur = connection.cursor()
#serialNum = sensor()
#print("Soil tempersature",loop(serialNum))
#print("The humidity",humidity())
#print("Soil moisture", measure())
#sleep(0.2)
#print("Atmospheric temp", read())

if __name__ == '__main__':
    try:
        while True:
            localtime = time.asctime( time.localtime(time.time()) )
            serialNum = sensor()
            localtime = time.asctime( time.localtime(time.time()) )
            cur.execute('insert into soilTemp(date, reading) values(?,?)', (localtime, float(loop(serialNum))))
            cur.execute('insert into humidity(date, reading) values(?,?)',(localtime, float(humidity())))
            time.sleep(1)
            cur.execute('insert into soilMoisture(date, reading) values(?,?)',(localtime, float(measure())))
            cur.execute('insert into atmosphericTemp(date, reading) values(?,?)', (localtime, float(read())))
            connection.commit()
            print "Data successfully written"
            time.sleep(60)
            
    except KeyboardInterrupt:
        connection.close()