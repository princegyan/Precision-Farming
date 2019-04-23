from flask import Flask, jsonify
import sqlite3 as s

app = Flask(__name__)


hum = []


@app.route("/")
def index():
    c = s.connect("IoTDatabase.db")
    cu = c.cursor()
    cu.execute("select * from humidity")
    y = cu.fetchall()

    return jsonify({"Success": True, "Data": y})


if __name__ == "__main__":
    app.run(debug=True, port=3000)
