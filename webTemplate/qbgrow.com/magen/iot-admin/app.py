from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():   
    return render_template('index.html')   
    # return "Hello Boss!  <a href='/logout'>Logout</a>"

time = []
temp=[]
# Route for the evrything under Atmospheric temperature
@app.route('/atmt/<x>')
def atmt(x):
    if x == '1h':
        with open('./reaading2.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e= int(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '24h':
        with open('./reading.embs') as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e= int(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1w':
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e= int(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1m':
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e= int(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    elif x == '1y':
        with open('./reaading2.embs'    ) as file:
            del time[:]
            d = file.readlines()
            for i in d:
                e= int(i.split()[1])
                temp.append(e)
                d=str(i.split()[0])
                if d not in temp:
                    time.append(d)
    return render_template('atm_tmp_1h.html', temp=temp, time=str(time))


if __name__ == '__main__':
    app.run(debug=True)
