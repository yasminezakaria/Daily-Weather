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

def insertIntoTableForecast():
    conn = connectToDB()
    cur = conn.cursor()
    tup = ('Cairo', 'cold', '20', '10'), ('Bali', 'cold', '10', '0'), ('London', 'rain', '0', '-5'), ('Paris', 'clouds', '0', '-5'), ('Dubai', 'rain', '0', '-5'), ('New York', 'snow', '-10', '-5'), ('Bangkok', 'hot', '35', '40'), ('Kuala Lumpur', 'hot', '35', '40')
    try:
        cur.executemany("INSERT INTO forecast VALUES (%s, %s,%s, %s)", tup)
        conn.commit()
    except:
        print("Error executing insert values")


def insertIntoTableWind():
    conn = connectToDB()
    cur = conn.cursor()
    tup = ('Cairo', '2', 'North'), ('Bali', '1', 'South'), ('London', '5', 'South'), ('Paris', '2', 'North'), ('Dubai', '1', 'South'), ('New York', '5', 'South'), ('Bangkok', '1', 'South'), ('Kuala Lumpur', '5', 'South')
    try:
        cur.executemany("INSERT INTO wind VALUES (%s, %s,%s)", tup)
        conn.commit()
    except:
        print("Error executing insert values")


def insertIntoTableAtmosphere():
    conn = connectToDB()
    cur = conn.cursor()
    tup = ('Cairo', 'high', '5', '3'), ('Bali', 'low', '10', '0'), ('London', 'high', '0', '1'), ('Paris', 'low', '0', '1'), ('Dubai', 'high', '0', '5'), ('New York', 'low', '10', '5'), ('Bangkok', 'high', '5', '0'), ('Kuala Lumpur', 'high', '5', '0')
    try:
        cur.executemany("INSERT INTO atmosphere VALUES (%s, %s,%s, %s)", tup)
        conn.commit()
    except:
        print("Error executing insert values")

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
