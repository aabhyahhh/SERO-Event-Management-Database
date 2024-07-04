###############SETTING UP DATABASE##################

#install mysql on your computer
# install sql installer
#pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    passwd = 'JSR', 
)

#prepare a cursor object 
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE SERO")

print("ALL DONE!")
