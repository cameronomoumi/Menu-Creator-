import json
from tkinter import *
import tkinter as tk

def searchme():
    print(data[0]['title'])
    print("-----------")


    searchstr = text.get()

    for recipe in data:
        try:
            if (searchstr in str(recipe['title'])):
                mylist.insert(END, recipe['title'])
               
        except KeyError:
            print("went past end of file. Try using upper-case letters")
        #print(i['title'])
        #print(data[i]['title'])


# code staring here
win = Tk()
win.geometry('400x200')

text = Entry(win)
text.pack()


btn = Button(win, text="search",command=searchme)
btn.pack()

myfile = open("recipes.json","r")
data = json.load(myfile)
myfile.close()



scrollbar = Scrollbar(win)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(win, yscrollcommand = scrollbar.set )

mylist.pack(fill = BOTH )
scrollbar.config( command = mylist.yview )



