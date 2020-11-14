
# -------
# UPDATE 5/11/2020: Need make leader, with 3 widget, print the labels tk about bet and win/lose money.
# and connect with Password for users

# -------

import os
import tkinter as tk
import data_zcasino 
from random import randrange
from math import ceil
import pickle
from operator import itemgetter

#Interface du programme 

root = tk.Tk()
root.title("CasiGame")
root.geometry('750x750')
root.minsize(width=750,height=750)
root.maxsize(width=750,height=750)

# FUNCTIONS


def save_money(money): #This function save your money
    
    files_money = open(data_zcasino.name_file, 'wb')
    the_pickler = pickle.Pickler(files_money)
    the_pickler.dump(money)
    files_money.close()

def retrieve_money(): #This function retrieve the money of players in the files storage
    
    if os.path.exists(data_zcasino.name_file):
        files_money = open(data_zcasino.name_file, 'rb')
        the_depickler = pickle.Unpickler(files_money)
        money = the_depickler.load()
        files_money.close()
        #//// VERIF ERROR FILES EMPTY////
        # try:
        #     the_depickler = pickle.Unpickler(files_money)
        #     money = the_depickler.load()
        #     files_money.close()
        # except EOFError:
        #     money = {}  # or whatever you want
    else:
        money = {}
    return money 

def readmoney():
    files_money = open(data_zcasino.name_file, 'rb')
    sorted(money.items(), key=lambda colonnes: colonnes[1])
    for i in files_money:
        print(i)

a = readmoney()

print(a)
    

# start = True                   
money = retrieve_money()
# We take name money

def getEntryName():

    # if start == True:
    name_user = inputName.get()
    if name_user not in money.keys():
        money[name_user] = 1000
        l1 = tk.Label(root, text='\nYou are not in DataBase you are a new user [{0}] you start with : {1}$'.format(name_user, money[name_user])).pack()
        newtext = 'MyNew text'
        l1.config(text=newtext)
    else:
        tk.Label(root,text ='\nHi ['+ str(name_user) +'] Welcome back to CasiGame ! You have : '+ str(money[name_user]) +'$').pack()
        return name_user
        newtext = 'MyNew text'
        l1.config(text=newtext)

    if money[name_user] == 0:
        tk.Label(root, text = '''You don't have enough money for bet ! you have: 0 $''').pack()
        credit = tk.Entry(root, text = '''Do you want credit your account with 100$ ? y/n : ''').pack()
        credit = input('Do you want credit your account with 100$ ? y/n : ')
        if credit == "y" or credit == "Y":
            money[name_user] =+ 100
        else:
            tk.Label(root, text='Without money you leave the game sorry !').pack()
            start = False

def retrieve_name_user(): #This function save your nameUser
    
    name_user = inputName.get()
    name_user = name_user.capitalize()
    if not name_user.isalnum() or len(name_user)<3:
        lerror = tk.Label(root, text='This name is not valid. Try again').pack()
        return retrieve_name_user()
    else:
        lname = tk.Label(root,text ='\nHi '+ str(name_user) +' Welcome back to CasiGame !').pack()
    return name_user

def getEntryNumberANDBet():
    # start = True
    # while start:
    name_user = inputName.get()
    number_bet = -1
    if number_bet < 0 or number_bet > 50:#Loop for check restriction numb
        number_bet = inputNumber.get()
        try:            #Try Error
            number_bet = int(number_bet)
        except ValueError:
            lNan = tk.Label(root, text='''It's not a number''').pack()
            number_bet = -1
        if number_bet < 0:
            lNgn = tk.Label(root, text='''This number is not good''').pack()
        if number_bet > 49:
            lnO = tk.Label(root, text='''This number is over 50 or equal''').pack()
        #Start Game

    bet = 0
    if bet <= 0 or bet > money[name_user] :
        bet = inputBet.get()
        try:
            bet = int(bet)
        except ValueError:
            lresult = tk.Label(root, text='''It's not a number''').pack()
        if bet <= 0:
            lresult = tk.Label(root, text='''This number is not good''').pack()
        if bet > money[name_user] or money[name_user] == 0:
            tk.Label(root, text = '''You don't have enough money for bet ! you have: 0 $''').pack()
            credit = tk.Entry(root, text = '''Do you want credit your account with 100$ ? y/n : ''').pack()
            credit = input('Do you want credit your account with 100$ ? y/n : ')
            if credit == "y" or credit == "Y":
                money[name_user] =+ 100
            else:
                tk.Label(root, text='Without money you leave the game sorry !').pack()
                start = False
        else:
            number_win = randrange(50)
            lresult = tk.Label(root, text='The roulett turn .... And the roulett stop on the number :'+ str(number_win) +'').pack()

            if number_win == number_bet:
                bet = bet*3
                lresult = tk.Label(root, text='Woh amazing ! You win: '+ str(bet) +' $').pack()
                money[name_user] += bet * 3
            elif number_win % 2 == number_bet % 2:
                bet = ceil(bet * 0.5)
                lresult = tk.Label(root, text='Is a same color, you win : '+ str(bet) +' $').pack()
                money[name_user] += bet
            else:
                lresult = tk.Label(root, text='Sorry but you lose your bet ...').pack()
                money[name_user] -= bet

    save_money(money)

# INTERFACE

l = tk.Label(root, 
            text='\nWELCOME TO THE GASIGAME :\n').pack()

def create():
    win = tk.Toplevel(root) 
    win.geometry('550x750')
    tk.Button(win, text = "Month").pack(ipadx=5,ipady=5, fill=tk.X)
    tk.Button(win, text = "Week").pack(ipadx=5,ipady=5, fill=tk.X)
    tk.Button(win, text = "Day").pack(ipadx=5,ipady=5, fill=tk.X)
btn = tk.Button(root, text="View the Leadder", command = create)
btn.pack(pady = 10) 




# INTERFACE

# Leave the game

def close_window():
    root.destroy()

buttonQuit = tk.Button(root,
                        text='''Quit the game''',
                        bg = 'Red',
                        width=15,
                        command= close_window).pack(side=tk.BOTTOM, pady = 50)

tk.Label(root, 
            text='\nPlease input your name :').pack()

entries = []
for i in range(1):
    inputName = tk.Entry(root)
    inputName.insert(0, "Ex : warrior59")
    inputName.pack()
    entries.append(inputName)
#root.bind("<Return>", lambda event: sendName(event, entries))

buttonName = tk.Button(root,
                        text='''Check if you exist''',
                        width=30,
                        command=getEntryName).pack()

# CHECK AND LET'S BET (input bet)

labreak = tk.Label(root, 
                text='\n').pack()

lab2 = tk.Label(root, 
                text='Please input your bet :').pack()

entries = []
for i in range(1):
    inputBet = tk.Entry(root)
    inputBet.pack()
    entries.append(inputBet)
# root.bind("<Return>", lambda event: sendBet(event, entries))


# CHECK AND LET'S BET (input number)

lab3 = tk.Label(root, 
                text='Please input your number into 0 and 49:').pack()

entries = []
for i in range(1):
    inputNumber = tk.Entry(root)
    inputNumber.pack()
    entries.append(inputNumber)
# root.bind("<Return>", lambda event: sendNumber(event, entries))

buttonStart = tk.Button(root,
                        text='''Let's Bet''',
                        width=30,
                        command=getEntryNumberANDBet).pack()

root.mainloop() 




