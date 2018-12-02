import requests
from weather import Weather, Unit


def api(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    return format_add


def apiWeather(city):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    forecast = location.forecast
    # Info we can get:-
    # forecast[0].high
    # forecast[0].low
    # forecast[0].text
    # forecast[0].date
    # forecast[0].day
    return forecast[0]


def apiWind(city):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    wind = location.wind
    # Info we can get:-
    # wind.direction
    # wind.speed
    return wind


def apiAtmosphere(city):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    atmosphere = location.atmosphere
    # Info we can get:-
    # atmosphere.humidity
    # atmosphere.pressure
    # atmosphere.rising
    # atmosphere.visibility
    return atmosphere

