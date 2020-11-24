
# -------
# UPDATE 5/11/2020: Need make leader, with 3 widget, print the labels tk about bet and win/lose money.
# and connect with Password for users. AND print the Entry for credit the account
# -------

import os
import tkinter as tk
import data_zcasino 
from random import randrange
from math import ceil
import pickle
from operator import itemgetter
import mysql.connector
import connectBDD
from DAO_sql import *
from pprint import pprint

#*Interface du programme 
root = tk.Tk()
root.title("CasiGame")
root.geometry('750x750')
root.minsize(width=750,height=750)
root.maxsize(width=750,height=750)

#* FUNCTIONS
def save_money(money):
    pass

def retrieve_name_user():
    
    name_user = inputName.get()
    name_user = name_user.capitalize()
    if not name_user.isalnum() or len(name_user)<3:
        lerror = tk.Label(root, text='This name is not valid. Try again').pack()
        return retrieve_name_user()
    else:
        lname = tk.Label(root,text ='\nHi '+ str(name_user) +' Welcome back to CasiGame !').pack()
    return name_user

def retrieve_money(): 
    table_users_money = cur.execute("SELECT * FROM users WHERE name_user = %s", usernameEntry)
    money = cur.fetchall()

    for n in money:
        print (money)
    
    return money

def readmoney():
    pass

def CheckUserExist(name): 

    print(name)
    name2 = name
    query = ("SELECT * FROM users WHERE name_user = " + str(name2))
    print(query)
    request = cur.execute(query, name2)

    #! FOR PRINT A QUERY REQUEST
    for (identifiant,nom,password,money) in cur:
        print("id -> {}, nom -> {}, password -> {}, money -> {}".format(identifiant, nom, password, money))
    
    if query is True:
        return True 
    else:
        return False

def CheckPassword(passw):

    print(passw)
    pwd2 = (passw,)
    queryPass = ("SELECT * FROM users WHERE pwd = %s")
    requestPass = cur.execute(queryPass, pwd2)

    #! FOR PRINT A QUERY REQUEST
    for (idf,name,password,money) in cur:
        print("id = {0}, name = {1}, passw = {2}, money = {3}".format(idf,name,password,money))

    if queryPass is True:
        return True
    else:
        return False

def connectToDB():
    cur        = connect.cursor(buffered = True)
    name       = inputName.get()
    pwd        = inputPassword.get()
    user_exist = CheckUserExist(inputName.get())
    passw_correct = CheckPassword(inputPassword.get())
    money      = 1000
    if user_exist == True :
        l1 = tk.Label(root, text='\n Welcome [{0}]'.format(name, money)).pack()
    else:
        addUser = ("INSERT INTO users (name_user, pwd, money) VALUES (%s, %s, %s)")
        User    = (name, pwd, money)
        cur.execute(addUser, User)
        connect.commit()
        l1 = tk.Label(root, text='\nYou are not in DataBase you are a new user [{0}] you start with : {1}$'.format(name, money)).pack()

def getEntryNumberANDBet():

    name_user = inputName.get()
    money = retrieve_money()
    number_bet = -1
    if number_bet < 0 or number_bet > 50:
        try:            #Try Error
            number_bet = int(number_bet)
        except ValueError:
            lNan = tk.Label(root, text='''It's not a number''').pack()
            number_bet = -1
        if number_bet < 0:
            lNgn = tk.Label(root, text='''This number is not good''').pack()
        if number_bet > 49:
            lnO = tk.Label(root, text='''This number is over 50 or equal''').pack()

    bet = 0
    if bet <= 0 or bet > money :
        bet = inputBet.get()
        try:
            bet = int(bet)
        except ValueError:
            lresult = tk.Label(root, text='''It's not a number''').pack()
        if bet <= 0:
            lresult = tk.Label(root, text='''This number is not good''').pack()
        if money > bet or money == 0:
            tk.Label(root, text = '''You don't have enough money for bet ! you have: 0 $''').pack()
            credit = tk.Entry(root, text = '''Do you want credit your account with 100$ ? y/n : ''').pack()
            credit = input('Do you want credit your account with 100$ ? y/n : ')
            if credit == "y" or credit == "Y":
                money =+ 100
            else:
                tk.Label(root, text='Without money you leave the game sorry !').pack()
                start = False
        else:
            number_win = randrange(50)
            lresult = tk.Label(root, text='The roulett turn .... And the roulett stop on the number :'+ str(number_win) +'').pack()

            if number_win == number_bet:
                bet = bet*3
                lresult = tk.Label(root, text='Woh amazing ! You win: '+ str(bet) +' $').pack()
                money += bet * 3
            elif number_win % 2 == number_bet % 2:
                bet = ceil(bet * 0.5)
                lresult = tk.Label(root, text='Is a same color, you win : '+ str(bet) +' $').pack()
                money += bet
            else:
                lresult = tk.Label(root, text='Sorry but you lose your bet ...').pack()
                money -= bet

    save_money(money)


"""   INTERFACE  """

def createLabel(textContent):
    return tk.Label(root, text=textContent).pack()

def createEntryPwd():
    return tk.Entry(root, show="*")

def createEntry():
    return tk.Entry(root)

def createButton(textContent, widthButton, callFunction, paddingY):

    return tk.Button(root, text=textContent, width=widthButton, command=callFunction).pack(pady=paddingY) 

def close_window():
    root.destroy()

def createWindow():
    win = tk.Toplevel(root) 
    win.geometry('550x750')
    tk.Button(win, text = "Month").pack(ipadx=5,ipady=5, fill=tk.X)
    tk.Button(win, text = "Week").pack(ipadx=5,ipady=5, fill=tk.X)
    tk.Button(win, text = "Day").pack(ipadx=5,ipady=5, fill=tk.X)

createLabel('\nWELCOME TO THE GASIGAME :\n')

btn = createButton('View the Leadder', 30, createWindow,10)

buttonQuit = tk.Button(root, text='''Quit the game''', bg = 'Red', width=15, command= close_window).pack(side=tk.BOTTOM, pady = 50)

entries = []
for i in range(1):
    createLabel('\n Please input your name :')
    inputName = createEntry()
    inputName.insert(0, "Ex : warrior59")
    inputName.pack()
    inputPassword = createEntryPwd()
    createLabel('\n Please input your password :')
    inputPassword.pack()
    entries.append(inputName)
    entries.append(inputPassword)

ButtonCheckExist = createButton('Check if you exist', 30, connectToDB,10)

createLabel('\n Please input your bet :')

entries = []
for i in range(1):
    inputBet = createEntry()
    inputBet.pack()
    entries.append(inputBet)

createLabel('Please input your number into 0 and 49:')

entries = []
for i in range(1):
    inputNumber = createEntry()
    inputNumber.pack()
    entries.append(inputNumber)

buttonBet = createButton('Let\'s Bet', 30, getEntryNumberANDBet,0)

root.mainloop() 
