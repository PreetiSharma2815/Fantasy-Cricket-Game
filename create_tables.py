# pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode

import db_connection_config as config
import db_and_tables as dbt

# FUCTIONS TO CREATE TABLES

def create_tables(cursor):
    for table_name in dbt.TABLES:
        table_description = dbt.TABLES[table_name]

        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table Already exists!")
            else:
                print(err.msg)
        else:
            print("OK")


################### Setup Connection and Create Tables ######################
try:
  cnx = mysql.connector.connect(**config.config)
  cursor = cnx.cursor()
  print("Connected to the DATABASE!")

  # call create tables
  create_tables(cursor)
  print("Tables created successfully!")

except mysql.connector.Error as err:

  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password!")

  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist!")  

  else:
    print(err)
else:
    cursor.close()
    cnx.close()





