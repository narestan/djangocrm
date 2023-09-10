#mysql creat db
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'iman@2222',
)

# Prepare a cursor object
cursorobject = database.cursor()

#creat database

cursorobject.execute("Create Database djcrm")
