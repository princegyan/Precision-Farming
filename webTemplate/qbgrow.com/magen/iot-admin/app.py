from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():   
    return render_template('index.html')   
    # return "Hello Boss!  <a href='/logout'>Logout</a>"



if __name__ == '__main__':
    app.run(debug=True)
