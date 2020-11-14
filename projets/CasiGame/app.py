from tkinter import *
root = Tk() # Make a windows

label = Label(root, text='Input your name')
label.grid(column=0, row=0)

label2 = Label(root, text='Input your bet')
label2.grid(column=1, row=0)

button = Button(root, text='Go bet !')
button.grid(column=0, row=2)
root.mainloop() # Start of boucle main



















