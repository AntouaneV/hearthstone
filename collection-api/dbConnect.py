import os
from dotenv import load_dotenv
import mysql.connector as con
from mysql.connector import Error
load_dotenv()

# minimum requirements to run the app
# pip install Flask
# pip install python-dotenv
# pip install mysql-connector-python

# Connexion à la base de données
def connectDB() :
    connection_params = {
    'host': os.getenv('HOST_NAME'),
    'user': os.getenv('USER_NAME'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE_NAME'),
    }
    try :
        connection = con.connect(**connection_params)
        if connection and connection.is_connected():
            return connection
    except Error as e :
        print("Failed to connect: {}".format(e))

#######################################################
# REWARDS
# ##################################################### 

    
