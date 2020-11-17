import sqlite3

def connectDB():

    connect = sqlite3.connect(user='root', password='', host='localhost', database='casigamedatabase')
    connect.close()