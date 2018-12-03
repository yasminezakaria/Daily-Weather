# TODO docker
# TODO connect to database and read the settings.py file

# TODO fill the table after crone job

import psycopg2

import settings
from backend import WeatherAPI


def connectToDB():
    connectionString = "host=" + settings.HOST + " dbname=" + settings.DATABASE + " user=" + settings.USER
    print(connectionString)
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to database")


# create forecast table
def createTableForecast():
    conn = connectToDB()
    cur = conn.cursor()
    createTableCommand = """CREATE TABLE IF NOT EXISTS forecast(city text UNIQUE,text text,high text,low text)"""
    try:
        cur.execute(createTableCommand)
        conn.commit()
    except:
        print("Error executing create table")


# create wind table
def createTableWind():
    conn = connectToDB()
    cur = conn.cursor()
    createTableCommand = """CREATE TABLE IF NOT EXISTS wind(city text UNIQUE,speed text,direction text)"""
    try:
        cur.execute(createTableCommand)
        conn.commit()
    except:
        print("Error executing create table")


# create atmosphere table
def createTableAtmosphere():
    conn = connectToDB()
    cur = conn.cursor()
    createTableCommand = """CREATE TABLE IF NOT EXISTS atmosphere(city text UNIQUE,pressure text,humidity text,visibility 
    text) """
    try:
        cur.execute(createTableCommand)
        conn.commit()
    except:
        print("Error executing create table")

def updateTableForecast(c):
    conn = connectToDB()
    cur = conn.cursor()
    forecast = WeatherAPI.apiWeather(c)
    try:
        cur.execute('UPDATE forecast SET (text,high,low)=(%s, %s,%s) WHERE city = %s ',
                    (forecast.text, forecast.high, forecast.low, c))
        conn.commit()
    except:
        print("Error executing update values")


# filling the table with dummy data
def updateTableWind(c):
    conn = connectToDB()
    cur = conn.cursor()
    wind = WeatherAPI.apiWind(c)
    try:
        cur.execute('UPDATE wind SET (speed,direction)=(%s, %s) WHERE city = %s ',
                    (wind.speed, wind.direction, c))
        conn.commit()
    except:
        print("Error executing update values")


# filling the table with dummy data
def updateTableAtmosphere(c):
    conn = connectToDB()
    cur = conn.cursor()
    atmosphere = WeatherAPI.apiAtmosphere(c)
    try:
        cur.execute('UPDATE atmosphere SET (pressure,humidity,visibility)=(%s, %s,%s) WHERE city = %s ',
                    (atmosphere.pressure, atmosphere.humidity, atmosphere.visibility, c))
        conn.commit()
    except:
        print("Error executing update values")

# function that return forecast values in json format to server
def showForecastForCity(c):
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM forecast WHERE city LIKE %s", (c,))
    except:
        print("Error executing select")
    columns = ('city', 'text', 'high', 'low')
    forecast = dict(zip(columns, cur.fetchone()))
    print(forecast)
    return forecast


# function that return wind values in json format to server
def showWindForCity(c):
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM wind WHERE city LIKE %s", (c,))
    except:
        print("Error executing select")
    columns = ('city', 'speed', 'direction')
    wind = dict(zip(columns, cur.fetchone()))
    print(wind)
    return wind


# function that return wind values in json format to server
def showAtmosphereForCity(c):
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM atmosphere WHERE city LIKE %s", (c,))
    except:
        print("Error executing select")
    columns = ('city', 'pressure', 'humidity', 'visibility')
    wind = dict(zip(columns, cur.fetchone()))
    print(wind)
    return wind
