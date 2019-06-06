"""
This is a submodule that is used to get the readings from the database based
on the table and the limit passed. It passes the test :)

Dennis Effa Amponsah
Prince Alfred Gyan

"""

import sqlite3 as sql


def select(table_name, limit):
    try:
        with sql.connect("combinedCode/IoTDatabase.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "select date, reading from( select * from %s order by id desc limit %d) order by id asc;"
                % (table_name, limit)
            )
    except BaseException as e:
        connection.rollback()
        print("Reason for failure: ", e)

    finally:
        return cursor.fetchall()
        connection.close()


if __name__ == "__main__":
    select("atmosphericTemp", 3)

