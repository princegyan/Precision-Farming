
import smbus
import time
import sqlite3 as sql

counter = 1
connection = sql.connect("IoTDatabase.db")
cur = connection.cursor()
while(counter ==1 ):
        bus = smbus.SMBus(1)
        bus.write_byte(0x40, 0xF3)
        time.sleep(0.3)
        data0 = bus.read_byte(0x40)
        data1 = bus.read_byte(0x40)
        cels = ((data0 * 256 + data1) * 175.72 / 65536.0)-46.85
        localtime = time.asctime( time.localtime(time.time()) )
        #print ("data0  :", data0)
        #f = open("collector.txt", "a")
        print('Atmospheric Temperature is %fc' % (cels))
        cels = round(cels,2)
        cur.execute('insert into atmosphericTemp(date, reading) values(?,?)', (localtime, float(cels)))
        connection.commit()
        connection.close()
        ##f.write(str(localtime)+ '\t')
        #f.write(str(cels)+'\n')
        #f.close()

        time.sleep(60)

        #time.sleep(10)

	

