from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import requests

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


@app.route('/<string:c>')      #user chose city, but hasnt requested to view current temperature
def cityEntered(c):
    #data brought from db should be set here instead of calling the api again
    #main2 is for the data from the API, here is is set to ' ' as it should not be used
    #main is for the data from the server (provisionally)
    global city
    city = c
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    main = format_add
    return render_template('index.html', main2=' ', main=main, cities=cities, city=city)



@app.route('/<string:c>/currentTemp')       #user chose to view current temperature for the selected city
def currentTemp(c):
    global city
    city = c
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    main = format_add
    return render_template('index.html', main=main, main2=main, cities=cities, city=city)


if __name__ == '__main__':
    app.run(debug=True)