"""This is a small module i made which prepares the files for download from an sqlite database
    You can name it the generator. Because it generates the a file for download :)

    Dennis Effa Amponsah
    Prince Alfred Gyan
"""

import sqlite3 as sql
import csv  # this module assists the reading and writing of CSV
from selection import select

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

heading = ["date", "reading"]


def generate(parameter, *limit):
    if limit:
        result = select(parameter, limit[0])
        if limit[0] == 60:
            with open("./data/%s_1hour_data.csv" % parameter, "w") as file:
                output = csv.writer(
                    file
                )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
                output.writerow(
                    [i for i in heading]
                )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

                for (
                    i
                ) in (
                    result
                ):  # prints the fields returned from the cursor. Take a breakdown to see what this is doing
                    output.writerow(i)
        elif limit[0] == 1440:
            with open("./data/%s_1day_data.csv" % parameter, "w") as file:
                output = csv.writer(
                    file
                )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
                output.writerow(
                    [i for i in heading]
                )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

                for (
                    i
                ) in (
                    result
                ):  # prints the fields returned from the cursor. Take a breakdown to see what this is doing
                    output.writerow(i)
        elif limit[0] == 10080:
            with open("./data/%s_1week_data.csv" % parameter, "w") as file:
                output = csv.writer(
                    file
                )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
                output.writerow(
                    [i for i in heading]
                )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

                for (
                    i
                ) in (
                    result
                ):  # prints the fields returned from the cursor. Take a breakdown to see what this is doing
                    output.writerow(i)
        
        elif limit[0] == 1441:
            with open('./data/%s_1month_data.csv'%parameter, 'w') as f:
                output = csv.writer(
                    f
                )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
                output.writerow(
                    [i for i in heading]
                )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

                for i in result:    #prints the fields returned from the cursor. Take a breakdown to see what this is doing
                    output.writerow(i)
        
        elif limit[0] == 5:
            with open("./data/%s_1year_data.csv" % parameter, "w") as file:
                output = csv.writer(
                    file
                )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
                output.writerow(
                    [i for i in heading]
                )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

                for (
                    i
                ) in (
                    result
                ):  # prints the fields returned from the cursor. Take a breakdown to see what this is doing
                    output.writerow(i)
    else:
        con = sql.connect("./combinedCode/IoTDatabase.db")
        cur = con.cursor()
        cur.execute("select date, reading from %s" % parameter)
        with open("./data/all_%s_data.csv" % parameter, "w") as file:
            output = csv.writer(
                file
            )  # the writer is function which takes a file object and an optional dilect. Refer to the docs of the librarys
            output.writerow(
                [i[0] for i in cur.description]
            )  # gets the fields in the table name. It uses list comprehension. See below for a more clearer view

            for (
                i
            ) in (
                cur
            ):  # prints the fields returned from the cursor. Take a breakdown to see what this is doing
                output.writerow(i)

        con.close()


# desc= []
# for i in cur.description:
#     desc.append(i[0])

if __name__ == "__main__":
    generate("humidity", 60)

