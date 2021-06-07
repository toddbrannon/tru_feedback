# Config for database
import mysql.connector

# create dictionary with db connection attributes
config = {
    'user': 'root',
    'password': '', #insert your password
    'host': 'localhost',
    'database': '' #insert your database name
}

# create connection passing in config dictionary as argument
db = mysql.connector.connect(**config)

# create cursor to execute queries
cursor = db.cursor()
