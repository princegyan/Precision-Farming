# from ds18b20 import loop, sensor, read, kill
import sqlite3 as sql

# from gy21 import humidity
# import PCF8591 as ADC
# from moisture import measure
# from temp2 import read
import random
import time

connection = sql.connect("IoTDatabase.db")
cur = connection.cursor()
import utils

# serialNum = sensor()
# print("Soil tempersature",loop(serialNum))
# print("The humidity",humidity())
# print("Soil moisture", measure())
# sleep(0.2)
# print("Atmospheric temp", read())

if __name__ == "__main__":
    try:
        while True:
            localtime = time.asctime(time.localtime(time.time()))
            # serialNum = sensor()
            sensor_reading = random.randint(0, 60)
            # minimum = setter()
            # if sensor_reading < minimum:
            #     print(
            #         "I would have called the Twilio because the moisture level is low"
            #     )
            cur.execute(
                "insert into soilTemp(date, reading) values(?,?)",
                (localtime, random.randint(0, 40)),
            )
            cur.execute(
                "insert into humidity(date, reading) values(?,?)",
                (localtime, random.randint(0, 70)),
            )
            time.sleep(1)
            cur.execute(
                "insert into soilMoisture(date, reading) values(?,?)",
                (localtime, sensor_reading),
            )
            cur.execute(
                "insert into atmosphericTemp(date, reading) values(?,?)",
                (localtime, random.randint(0, 100)),
            )
            connection.commit()
            print("Data successfully written")
            time.sleep(60)

    except KeyboardInterrupt:
        connection.close()
