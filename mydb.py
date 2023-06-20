import mysql.connector

# connect a databse
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@My1234#',

    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
