from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def index():
    #with open('./readings/atmp1h.embs') as file:
        #u = file.readlines()[-1]
        #atmtemp = u[8:12]
    with open('./readings/atmp1h.embs') as file:
        x = file.readlines()[-1]
        atmtemp=x[7:12]
    with open('./readings/humidity1h.embs') as file:
        x = file.readlines()[-1]
        humidity=x[7:12]
    with open('./readings/stmp1h.embs') as file:
        x = file.readlines()[-1]
        soiltemp=x[7:12]
    with open('./readings/moisture1h.embs') as file:
        x = file.readlines()[-1]
        moisture=x[7:12]
        return render_template('index.html',atmtemp=atmtemp, humidity=humidity, soiltemp=soiltemp, moisture=moisture)   
    # return "Hello Boss!  <a href='/logout'>Logout</a>"

time = []
temp=[]
moist = []
humidity=[]
# Route for the evrything under Atmospheric temperature
@app.route('/atmtemp/<x>')
def atmtemp(x):
    if x == '1h':
        name = '1 HOUR'
        label = 'Minutes'
        with open('./readings/atmp1h.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        name = '24 HOUR'
        label = 'Hours'
<<<<<<< HEAD
        with open('./readings/atmp24h.embs') as file:
=======
        with open('./reading.embs') as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        name = '1 WEEK'
        label = 'Days'
<<<<<<< HEAD
        with open('./readings/atmp1w.embs') as file:
=======
        with open('./reaading2.embs'    ) as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        name = '1 MONTH'
        label = 'Weeks'
<<<<<<< HEAD
        with open('./reaading2.embs') as file:
=======
        with open('./reaading2.embs'    ) as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        name = '1 YEAR'
        label = 'Months'
<<<<<<< HEAD
        with open('./reaading2.embs') as file:
=======
        with open('./reaading2.embs'    ) as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('atm_temp.html', temp=temp, time=str(time), name=name, label=label)




@app.route('/soiltemp/<x>')
def soiltemp(x):
    if x == '1h':
        name = '1 HOUR'
        label = 'Minutes'
        with open('./readings/stmp1h.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        name = '24 HOUR'
        label = 'Hours'
<<<<<<< HEAD
        with open('./readings/stmp24h.embs') as file:
=======
        with open('./reading.embs') as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        name = '1 WEEK'
        label = 'Days'
<<<<<<< HEAD
        with open('./readings/stmp1w.embs') as file:
=======
        with open('./reaading2.embs') as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                #print(temp)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        name = '1 MONTH'
        label = 'Weeks'
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        name = '1 YEAR'
        label = 'Months'
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('soil_temp.html', temp=temp, time=str(time), name=name, label=label)

@app.route('/soilmoist/<x>')
def soilmoist(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        with open('./reading.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                moist.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('soil_moist.html', moist=moist, time=str(time), name=name, label=label)


@app.route('/humidity/<x>')
def humid(x):
    if x == '1h':
        name =  '1 Hour'
        label = 'Minutes'
        with open('./readings/humidity1h.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        name = '24 Hour'
        label = 'Hours'
<<<<<<< HEAD
        with open('./readings/humidity24h.embs') as file:
=======
        with open('./reading.embs') as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        name = '1 Week'
        label = 'Days'
<<<<<<< HEAD
        with open('./readings/humidity1w.embs') as file:
=======
        with open('./reaading2.embs') as file:
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        name = '1 Month'
        label = 'Weeks'
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        name = '1 Year'
        label = 'Months'
        with open('./reaading2.embs') as file:
            del time[:]
            del temp[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('humidity.html', humidity=humidity, time=str(time), name=name, label=label)


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, host='10.10.64.13')
=======
    app.run(debug=True,)
>>>>>>> 17238407395f85472e9bf997d1904c86efa14906
