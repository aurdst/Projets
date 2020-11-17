import mysql.connector
import connectBDD
import os


# class DAOsql:
#     # TODO : Function search by ID 
#     def searchById():
#         pass
#     # TODO : Function add user
    #  def searchById():
#     # TODO : Function save money 
#     def saveMoney():
#         pass
#     # TODO : Function search by username 
#     def searchByUserName():
#         pass


connect = mysql.connector.connect(host="localhost",user="root", password="", database="casigamedatabase")
cur = connect.cursor()

# cur.execute("CREATE TABLE users (CHAR name, INTEGER money)")
# cur.execute("INSERT INTO users VALUES ('testeur','1000')")
# cur.execute("SELECT * FROM users")

# result = cur.fetchall()

# for n in result:
#     print(n)

connect.commit()