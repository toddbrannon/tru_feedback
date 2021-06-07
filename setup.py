import mysql.connector
from mysql.connector import errorcode
from database import cursor
# from database_config import cursor

DB_NAME = 'tru_fdbk'

TABLES = {}

TABLES['responses'] = (
    "CREATE TABLE `responses` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `first_name` varchar(250) NOT NULL,"
    " `last_name` varchar(250) NOT NULL,"
    " `email_address` varchar(250) NOT NULL,"
    " `age_group` tinyint, "
    " `dollars_spent` tinyint, "
    " `on_time` tinyint, "
    " `correct_product` tinyint, "
    " `expectation` tinyint, "
    " `photograph` tinyint, "
    " `description` tinyint, "
    " `recommend` tinyint, "
    " `use_again` tinyint, "
    " `loyalty` tinyint, "
    " `comments` varchar(250), "
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE InnoDB"
)

# create function to create database


def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created".format(DB_NAME))

# create function to create tables


def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({})".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists")
            else:
                print(err.msg)


create_database()
create_tables()
