from flask import Flask, render_template, Response
import csv
from generator import generate
from selection import select
from landingpage import read

import sqlite3 as sql


app = Flask(__name__)


@app.route("/")
def index():
    results = read()
    return render_template(
        "index.html",
        atmtemp=float(round(results[0][0], 2)),
        humidity=float(round(results[1][0], 2)),
        soiltemp=float(round(results[2][0], 2)),
        moisture=float(round(results[3][0], 2)),
    )


time = []
temp = []
moist = []
humidity = []

# Route for the evrything under Atmospheric temperature
@app.route("/atmtemp/<x>")
def atmtemp(x):
    if x == "1h":
        name = "1 HOUR"
        label = "Minutes"
        del time[:]
        del temp[:]
        result = select("atmosphericTemp", 20)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        del time[:]
        del temp[:]
        result = select("atmosphericTemp", 60)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "1w":
        name = "1 WEEK"
        label = "Days"
        del time[:]
        del temp[:]
        result = select("atmosphericTemp", 10080)
        for i in result:
            temp.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    elif x == "1m":
        name = "1 MONTH"
        label = "Weeks"
        del time[:]
        del temp[:]
        result = select("atmosphericTemp", 10)  # please take a look at this one
        for i in result:
            temp.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    elif x == "1y":
        name = "1 YEAR"
        label = "Months"
        del time[:]
        del temp[:]
        result = select("atmosphericTemp", 15)  # please take a look at this one
        for i in result:
            temp.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    return render_template(
        "atm_temp.html", temp=temp, time=str(time), name=name, label=label
    )


@app.route("/soiltemp/<x>")
def soiltemp(x):
    if x == "1h":
        name = "1 HOUR"
        label = "Minutes"
        with open("./readings/stmp1h.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        with open("./readings/stmp24h.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1w":
        name = "1 WEEK"
        label = "Days"
        with open("./readings/stmp1w.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                # print(temp)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1m":
        name = "1 MONTH"
        label = "Weeks"
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1y":
        name = "1 YEAR"
        label = "Months"
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template(
        "soil_temp.html", temp=temp, time=str(time), name=name, label=label
    )


@app.route("/soilmoist/<x>")
def soilmoist(x):
    if x == "1h":
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "24h":
        with open("./reading.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1w":
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1m":
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                temp.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1y":
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                moist.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template(
        "soil_moist.html", moist=moist, time=str(time), name=name, label=label
    )


@app.route("/humidity/<x>")
def humid(x):
    if x == "1h":
        name = "1 Hour"
        label = "Minutes"
        with open("./readings/humidity1h.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                humidity.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "24h":
        name = "24 Hour"
        label = "Hours"

        with open("./readings/humidity24h.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                humidity.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1w":
        name = "1 Week"
        label = "Days"
        with open("./readings/humidity1w.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                humidity.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1m":
        name = "1 Month"
        label = "Weeks"
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                humidity.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == "1y":
        name = "1 Year"
        label = "Months"
        with open("./reaading2.embs") as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e = float(i.split()[1])
                humidity.append(e)
                d = str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template(
        "humidity.html", humidity=humidity, time=str(time), name=name, label=label
    )


@app.route("/download/<parameter>")
def download(parameter):
    # First i need to prepare the file
    generate(parameter)

    # I need to downloaded the file
    with open("./data/%s_data.csv" % parameter, "r") as f:
        returnedfile = f.read().encode("latin-1")
    f.close()
    return Response(
        returnedfile,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=%s_data.csv" % parameter},
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)

