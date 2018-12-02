# TODO change it from local
# TODO connect to database and read the config file
# TODO call create table in the right place
# TODO fill the table with dummy data
# TODO fill the table after crone job
import json

import psycopg2


def connectToDB():
    connectionString = "host=localhost dbname=postgres user=postgres port=5432"
    print(connectionString)
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to database")


# TODO ask yasmin about the entries
# create table
def createTable():
    conn = connectToDB()
    cur = conn.cursor()
    createTableCommand = """
    CREATE TABLE FORECAST(
    city varchar(100),
    temp varchar(100),
    windDirection varchar(100),
    windSpeed varchar(100),
    humidity varchar(100),
    pressure varchar(100)
)
"""
    cur.execute(createTableCommand)
    conn.commit()


# function that return the value in json format to server
def showForecastForCity(c):
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM FORECAST WHERE city=%s", c)
    except:
        print("Error executing select")
    result = cur.fetchone()
    main2 = json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
    return main2
