# TODO docker
# TODO connect to database and read the settings.py file

# TODO fill the table after crone job

import psycopg2

import settings


def connectToDB():
    connectionString = "host=" + settings.HOST + " dbname=" + settings.DATABASE + " user=" + settings.USER +\
                       " password=" + settings.PASSWORD
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


# filling the table with dummy data
def insertIntoTableForecast():
    conn = connectToDB()
    cur = conn.cursor()
    tup = ('Cairo', 'cold', '20', '10'), ('Bali', 'cold', '10', '0'), ('London', 'rain', '0', '-5')
    try:
        cur.executemany("INSERT INTO forecast VALUES (%s, %s,%s, %s)", tup)
        conn.commit()
    except:
        print("Error executing insert values")


def insertIntoTableWind():
    conn = connectToDB()
    cur = conn.cursor()
    tup = ('Cairo', '2', 'North'), ('Bali', '1', 'South'), ('London', '5', 'South')
    try:
        cur.executemany("INSERT INTO wind VALUES (%s, %s,%s)", tup)
        conn.commit()
    except:
        print("Error executing insert values")


def insertIntoTableAtmosphere():
    conn = connectToDB()
    cur = conn.cursor()
    tup = ('Cairo', 'high', '5', '3'), ('Bali', 'low', '10', '0'), ('London', 'high', '0', '1')
    try:
        cur.executemany("INSERT INTO atmosphere VALUES (%s, %s,%s, %s)", tup)
        conn.commit()
    except:
        print("Error executing insert values")


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
