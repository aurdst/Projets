import mysql.connector
import connectBDD
import os

try:
    connect = mysql.connector.connect(host="localhost",user="root", password="", database="casigamedatabase")
    cur = connect.cursor()
    connect.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
    