from flask import Flask, render_template, Response
import csv
from generator import generate
from selection import select
from landingpage import read
from views.settings import render_settings
import sqlite3 as sql
from Utils.temp_picker import setter
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()
    
    
    results = read()
    reading = "Your atmospheric temperature is %d, humidity is %d, soil moisture is %d, soil temperature is %d, soil pH is %d. Thank you."%(float(round(results[0][0], 2)), float(round(results[1][0], 2)), float(round(results[2][0], 2)), float(round(results[3][0], 2)), float(round(results[4][0], 2)))
    # Read a message aloud to the caller
    #resp.say("Your ph is in critcal state. Please visit your farm", voice='alice')
    say = Say(voice='Polly.Joanna')
    say.ssml_prosody(reading, pitch='-10%', rate='85%', volume='-6dB')
    #say.
    #resp.say(reading, voice='alice')
    resp.append(say)

    return str(resp)


@app.route("/")
def index():
    results = read()
    print("This is the setter", setter())
    return render_template(
        "index.html",
        atmtemp=float(round(results[0][0], 2)),
        humidity=float(round(results[1][0], 2)),
        moisture=float(round(results[2][0], 2)),
        soiltemp=float(round(results[3][0], 2)),
        ph = float(round(results[4][0], 2))
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
        result = select("atmosphericTemp", 60)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        del time[:]
        del temp[:]
        result = select("atmosphericTemp", 1440)
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

@app.route("/ph/<x>")
def ph(x):
    if x == "1h":
        name = "1 HOUR"
        label = "Minutes"
        del time[:]
        del temp[:]
        result = select("soilpH", 60)
        print(result)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        del time[:]
        del temp[:]
        result = select("soilpH", 1440)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "1w":
        name = "1 WEEK"
        label = "Days"
        del time[:]
        del temp[:]
        result = select("soilpH", 10080)
        for i in result:
            temp.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    elif x == "1m":
        name = "1 MONTH"
        label = "Weeks"
        del time[:]
        del temp[:]
        result = select("soilpH", 10)  # please take a look at this one
        for i in result:
            temp.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    elif x == "1y":
        name = "1 YEAR"
        label = "Months"
        del time[:]
        del temp[:]
        result = select("soilpH", 15)  # please take a look at this one
        for i in result:
            temp.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    return render_template(
        "soil_ph.html", ph=temp, time=str(time), name=name, label=label
    )



@app.route("/soilmoist/<x>")
def soilmoist(x):
    if x == "1h":
        name = "1 HOUR"
        label = "Minutes"
        del time[:]
        del moist[:]
        result = select("soilMoisture", 60)
        for i in result:
            moist.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        del time[:]
        del moist[:]
        result = select("soilMoisture", 1440)
        for i in result:
            moist.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "1w":
        name = "1 WEEK"
        label = "Days"
        del time[:]
        del temp[:]
        result = select("soilMoisture", 10080)
        for i in result:
            moist.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    elif x == "1m":
        name = "1 MONTH"
        label = "Weeks"
        del time[:]
        del temp[:]
        result = select("soilMoisture", 10)  # please take a look at this one
        for i in result:
            moist.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    elif x == "1y":
        name = "1 YEAR"
        label = "Months"
        del time[:]
        del temp[:]
        result = select("soilMoisture", 15)  # please take a look at this one
        for i in result:
            moist.append(float(round(i[1], 2)))
            time.append(str(i[0][11:16]))

    return render_template(
        "soil_moist.html", moist=moist, time=str(time), name=name, label=label
    )


@app.route("/soiltemp/<x>")
def soiltemp(x):
    if x == "1h":
        name = "1 HOUR"
        label = "Minutes"
        del time[:]
        del temp[:]
        result = select("soilTemp", 60)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        del time[:]
        del temp[:]
        result = select("soilTemp", 1440)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "1w":
        name = "1 WEEK"
        label = "Days"
        del time[:]
        del temp[:]
        result = select("soilTemp", 10080)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))
    elif x == "1m":
        name = "1 MONTH"
        label = "Weeks"
        del time[:]
        del temp[:]
        result = select("soilTemp", 100)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))
    elif x == "1y":
        name = "1 YEAR"
        label = "Months"
        del time[:]
        del temp[:]
        result = select("soilTemp", 200)
        for i in result:
            temp.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))
    return render_template(
        "soil_temp.html", temp=temp, time=str(time), name=name, label=label
    )


@app.route("/humidity/<x>")
def humid(x):
    if x == "1h":
        name = "1 HOUR"
        label = "Minutes"
        # with open("./readings/humidity1h.embs") as file:
        # d = file.readlines()
        # del time[:]
        # del temp[:]
        del time[:]
        del humidity[:]
        result = select("humidity", 60)
        for i in result:
            humidity.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))
    elif x == "24h":
        name = "24 HOUR"
        label = "Hours"
        del time[:]
        del humidity[:]
        result = select("humidity", 1440)
        for i in result:
            humidity.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))

    elif x == "1w":
        name = "1 WEEK"
        label = "Days"
        del time[:]
        del humidity[:]
        result = select("humidity", 10080)
        for i in result:
            humidity.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][0:4]))
    elif x == "1m":
        name = "1 MONTH"
        label = "Weeks"
        del time[:]
        del humidity[:]
        result = select("humidity", 4)
        for i in result:
            humidity.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))
    elif x == "1y":
        name = "1 YEAR"
        label = "Months"
        del time[:]
        del humidity[:]
        result = select("humidity", 10)
        for i in result:
            humidity.append(float(round(i[1], 2)))  # works for the time
            time.append(str(i[0][11:16]))
    return render_template(
        "humidity.html", humidity=humidity, time=str(time), name=name, label=label
    )


#@app.route("/ph/<x>")
#def ph(x):
#    name = "this is the ph"
#    label = "Yao Mings job"
 #   time = "It is time"
#    ph = "12"
#    return render_template(
#        "soil_ph.html", ph=ph, time=str(time), name=name, label=label
#    )


@app.route("/analyse")
def analysis():
    return """<h2>Analysis is coming. You get to know the ideal time to plant, the ideal time to water your plants and the idea</h2>"""


@app.route("/settings", methods=['GET', 'POST'])
def settings():
    # return """<h2>Settings is coming soon. You get to set the threshold of sensors for an alert</h2>"""
    return render_settings()


@app.route("/download/<table_name>")
@app.route("/download/<table_name>/<limit>")
def download(table_name, **limit):
    if limit:
        if limit["limit"] == "1 HOUR":
            generate(table_name, 60)
            with open("./data/%s_1hour_data.csv" % table_name, "r") as file:
                returnfile = file.read().encode("latin-1")
            file.close()
            return Response(
                returnfile,
                mimetype="text/csv",
                headers={
                    "Content-disposition": "attachment; filename=%s_1hour_data.csv"
                    % table_name
                },
            )
        elif limit["limit"] == "24 HOUR":
            generate(table_name, 1440)
            with open("./data/%s_1day_data.csv" % table_name, "r") as file:
                returnfile = file.read().encode("latin-1")
            file.close()
            return Response(
                returnfile,
                mimetype="text/csv",
                headers={
                    "Content-disposition": "attachment; filename=%s_1day_data.csv"
                    % table_name
                },
            )
        elif limit["limit"] == "1 WEEK":
            generate(table_name, 10080)
            with open("./data/%s_1week_data.csv" % table_name, "r") as file:
                returnfile = file.read().encode("latin-1")
            file.close()
            return Response(
                returnfile,
                mimetype="text/csv",
                headers={
                    "Content-disposition": "attachment; filename=%s_1week_data.csv"
                    % table_name
                },
            )
        elif limit["limit"] == "1 MONTH":
            generate(table_name, 1441)
            with open("./data/%s_1month_data.csv" % table_name, "r") as file:
                returnfile = file.read().encode("latin-1")
            file.close()
            return Response(
                returnfile,
                mimetype="text/csv",
                headers={
                    "Content-disposition": "attachment; filename=%s_1month_data.csv"
                    % table_name
                },
            )
        elif limit["limit"] == "1 YEAR":
            generate(table_name, 5)
            with open("./data/%s_1year_data.csv" % table_name, "r") as file:
                returnfile = file.read().encode("latin-1")
            file.close()
            return Response(
                returnfile,
                mimetype="text/csv",
                headers={
                    "Content-disposition": "attachment; filename=%s_1year_data.csv"
                    % table_name
                },
            )
    else:
        generate(table_name)
        with open("./data/all_%s_data.csv" % table_name, "r") as f:
            returnedfile = f.read().encode("latin-1")
        f.close()
        return Response(
            returnedfile,
            mimetype="text/csv",
            headers={
                "Content-disposition": "attachment; filename=%s_all_data.csv"
                % table_name
            },
        )


if __name__ == "__main__":
    app.run()

