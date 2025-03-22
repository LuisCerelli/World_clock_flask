from flask import Flask, render_template, jsonify
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

zones = {
    "Argentina": "America/Argentina/Buenos_Aires",
    "Europa Central": "Europe/Paris",
    "Hamilton Island": "Australia/Lindeman"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/time")
def api_time():
    times = {
        name: datetime.now(timezone(tz)).strftime("%H:%M:%S")
        for name, tz in zones.items()
    }
    return jsonify(times)

if __name__ == "__main__":
    app.run(debug=True)