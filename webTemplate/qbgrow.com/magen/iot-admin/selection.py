"""
This is a submodule that is used to get the readings from the database based
on the table and the limit passed. It passes the test :)

Dennis Effa Amponsah
Prince Alfred Gyan

"""

import sqlite3 as sql


def select(table_name, limit):
    connection = sql.connect("combinedCode/IoTDatabase.db")
    cursor = connection.cursor()
    cursor.execute(
        "select date, reading from( select * from %s order by id desc limit %d) order by id asc;"
        % (table_name, limit)
    )

    return cursor.fetchall()
    connection.close()


if __name__ == "__main__":
    select("atmosphericTemp", 3)

