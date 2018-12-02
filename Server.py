from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import requests

from backend import WeatherAPI

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

app = Flask(__name__)
Bootstrap(app)

city = ""  # Global variable that contains which city was chosen
cities = ["Cairo", "Bali", "Paris", "London", "Dubai", "New York", "Bangkok",
          "Kuala Lumpur"]  # list of cities to choose from


@app.route('/')  # homepage
def index():
    return render_template('index.html', city='', cities=cities)


@app.route('/<string:c>')  # user choose city, but hasn't requested to view current temperature
def cityEntered(c):
    ### to be changed
    forecast = WeatherAPI.apiWeather(c)
    wind = WeatherAPI.apiWind(c)
    atmosphere = WeatherAPI.apiAtmosphere(c)
    ###
    return render_template('index.html', forecast=forecast, wind=wind, atmosphere=atmosphere,
                           cities=cities, city=c, condition=' ')


@app.route('/<string:c>/currentTemp')  # user chose to view current temperature for the selected city
def currentTemp(c):
    ### to be changed
    forecast = WeatherAPI.apiWeather(c)
    wind = WeatherAPI.apiWind(c)
    atmosphere = WeatherAPI.apiAtmosphere(c)
    ###
    condition = WeatherAPI.apiCondition(c)
    return render_template('index.html', forecast=forecast, wind=wind, atmosphere=atmosphere,
                           cities=cities, city=c, condition=condition)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')