import mysql.connector
import connectBDD
import os

connect = mysql.connector.connect(host="localhost",user="root", password="", database="casigamedatabase")
cur = connect.cursor()
connect.commit()