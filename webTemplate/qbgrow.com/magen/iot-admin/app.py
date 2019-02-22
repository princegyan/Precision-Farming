from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():   
    return render_template('index.html')   
    # return "Hello Boss!  <a href='/logout'>Logout</a>"

time = []
temp=[]
moist = []
humidity=[]
# Route for the evrything under Atmospheric temperature
@app.route('/atmtemp/<x>')
def atmtemp(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
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
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('atm_temp.html', temp=temp, time=str(time))




@app.route('/soiltemp/<x>')
def soiltemp(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
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
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('soil_temp.html', temp=temp, time=str(time))

@app.route('/soilmoist/<x>')
def soilmoist(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
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
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                moist.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('soil_moist.html', moist=moist, time=str(time))


@app.route('/humidity/<x>')
def humid(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        with open('./reading.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e=float(i.split()[1])
                humidity.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('humidity.html', humidity=humidity, time=str(time))


if __name__ == '__main__':
    app.run(debug=True)
