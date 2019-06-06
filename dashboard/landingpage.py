"""
This is a submodule that is used to collect the required data to be rendered 
on the landing page. It passed the test :)

Dennis Effa Amponsah
Price Alfred Gyan

"""

import sqlite3 as sql

db_tables = ["atmosphericTemp", "humidity", "soilMoisture", "soilTemp", "soilpH"]

data = []  # This should hold the data from the database


def read():
    del data[:]
    # connection = sql.connect("combinedCode/IoTDatabase.db")
    # cursor = connection.cursor()
    # for i in db_tables:
    #     cursor.execute("select reading from %s order by id desc limit 1" % i)
    #     data.append(cursor.fetchone())
    # connection.close()

    # return data

    try:
        with sql.connect("combinedCode/IoTDatabase.db") as connection:
            cursor = connection.cursor()
            for i in db_tables:
                cursor.execute("select reading from %s order by id desc limit 1" % i)
                data.append(cursor.fetchone())
    except Exception as e:
        connection.rollback()
        print("This is the reason", e)
    finally:
        return data
        connection.close()


if __name__ == "__main__":
    read()
