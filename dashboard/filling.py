temp = []
from itertools import islice

# with open('.\collector.txt') as f:
#     #temp.append(f.read().split('\n')[0])
#     #l = f.read().split('\n')[0]
#     #print(l)
#     head = [next(f) for x in range(2)]


def file_read_from_head(fname, nlines):
    with open(fname) as f:
        for line in islice(f, nlines):
            temp.append(line)
            # print(line)


import sqlite3 as sql
from time import sleep

con = sql.connect("IoTDatabase.db")
sleep(0.5)
c = con.cursor()


file_read_from_head("moistureCollector.txt", 22)
# print(temp[0])   #Prints the first line
# print(temp[0][:25])   #prints the first 25 on line 1


for i in range(22):
    # print(temp[i][:25])
    # print(temp[i][25:])
    c.execute('insert into soilMoisture(date, reading) values(?,?)', (temp[i][:25], temp[i][25:]))


con.commit()


# IoTDatabase.db
