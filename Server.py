from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import requests

from backend import WeatherAPI

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

app = Flask(__name__)
Bootstrap(app)


city = ""   #Global variable that contains which city was chosen
cities = ["Cairo", "Bali", "Paris", "London", "Dubai", "New York", "Bangkok", "Kuala Lumpur"]  #list of cities to choose from


@app.route('/')     #homepage
def index():
    global city
    city = ''
    main = ''
    return render_template('index.html', main2=' ', main=main, cities=cities, city=city)


@app.route('/<string:c>')      #user choose city, but hasn't requested to view current temperature
def cityEntered(c):
    main = WeatherAPI.api(c)
    return render_template('index.html', main2=' ', main=main, cities=cities, city=c)



@app.route('/<string:c>/currentTemp')       #user chose to view current temperature for the selected city
def currentTemp(c):
    main = WeatherAPI.api(c)
    return render_template('index.html', main=main, main2=main, cities=cities, city=c)


if __name__ == '__main__':
    app.run(debug=True)