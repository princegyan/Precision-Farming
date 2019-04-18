"""This is a small module i made which prepares the files for download from an sqlite database
    You can name it the generator. Because it generates the a file for download :)

    Dennis Effa Amponsah
    Prince Alfred Gyan
"""

import sqlite3 as sql
import csv  # this module assists the reading and writing of CSV

# The commented out data is the initial one

# con = sql.connect("iot.db")
# cur = con.cursor()

# cur.execute(
#     "select date, data from temperature"
# )  # this query can be altered to suit what users want
# with open("data.csv", "w") as file:
#     output = csv.writer(file)
#     output.writerow([i[0] for i in cur.description])

#     for i in cur:
#         output.writerow(i)

# con.close()


def generate(parameter):
    con = sql.connect("./combinedCode/IoTDatabase.db")
    cur = con.cursor()
    cur.execute("select date, reading from %s" % parameter)
    with open("./data/%s_data.csv" % parameter, "w") as file:
        output = csv.writer(
            file
        )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
        output.writerow(
            [i[0] for i in cur.description]
        )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

        for i in cur:    #prints the fields returned from the cursor. Take a breakdown to see what this is doing
            output.writerow(i)

    con.close()


# desc= []
# for i in cur.description:
#     desc.append(i[0])

if __name__ == "__main__":
    generate("humidity")

