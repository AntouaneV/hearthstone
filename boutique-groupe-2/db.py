
import mysql.connector

def db_connect():
    return mysql.connector.connect(
        host="mysql-sham94.alwaysdata.net",
        user="sham94",
        password="awajaba",
        database="sham94_db",
    )

def execute(db, query):
    mycursor = db.cursor()
    mycursor.execute(query)
    return mycursor