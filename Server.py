from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from apscheduler.schedulers.background import BackgroundScheduler
from backend import WeatherAPI, postgres


app = Flask(__name__)
Bootstrap(app)

city = ""  # Global variable that contains which city was chosen
cities = ["Cairo", "Bali", "Paris", "London", "Dubai", "New York", "Bangkok",
          "Kuala Lumpur", "Berlin", "Riyadh", "Madrid"]  # list of cities to choose from


@app.route('/')  # homepage
def index():
    return render_template('index.html', city='', cities=cities)


@app.route('/<string:c>')  # user choose city, but hasn't requested to view current temperature
def cityEntered(c):
    forecast = postgres.showForecastForCity(c)
    wind = postgres.showWindForCity(c)
    atmosphere = postgres.showAtmosphereForCity(c)
    return render_template('index.html', forecast=forecast, wind=wind, atmosphere=atmosphere, cities=cities, city=c,
                           condition=' ')


@app.route('/<string:c>/currentTemp')  # user chose to view current temperature for the selected city
def currentTemp(c):
    forecast = postgres.showForecastForCity(c)
    wind = postgres.showWindForCity(c)
    atmosphere = postgres.showAtmosphereForCity(c)
    condition = WeatherAPI.apiCondition(c)
    return render_template('index.html', forecast=forecast, wind=wind, atmosphere=atmosphere,
                           cities=cities, city=c, condition=condition)


postgres.createTableForecast()
postgres.createTableWind()
postgres.createTableAtmosphere()
postgres.insertIntoTableForecast()
postgres.insertIntoTableWind()
postgres.insertIntoTableAtmosphere()
job1()

def job1():
    for c in cities:
        postgres.updateTableAtmosphere(c)
        postgres.updateTableForecast(c)
        postgres.updateTableWind(c)
    print("DONE!")



if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=job1, trigger="interval", hours=24)
    scheduler.start()
    app.run(host="0.0.0.0", debug=True)

