from flask import Flask
from flask import render_template
from flask import request
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def render_results():
    city = request.form['city']
    owm = OWM('55ab3b72ce60553c9d1a2cd9208b4e0e')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    details = w.detailed_status
    if details == "mist":
        icon = "fas fa-smog"
    elif details == "clear sky":
        icon = "fas fa-sun"
    elif details == "few clouds":
        icon = "fas fa-cloud-sun"
    elif details == "thunderstorm":
        icon = "fas fa-bolt"
    elif details == "snow":
        icon = "far fa-snowflake"
    elif details == "rain":
        icon = "fas fa-cloud-rain"
    elif details == "shower rain":
        icon = "fas fa-cloud-showers-heavy"
    else:
        icon = "fas fa-cloud"

    return render_template('results.html', city=city, temp=temp, details=details, icon=icon)


if __name__ == '__main__':
    app.run(debug=True)
