# install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = '1234',


)

# prepare a cursor object
cursourobject = database.cursor()
# create a database
cursourobject.execute("CREATE DATABASE GANGA")
print("All Done!")