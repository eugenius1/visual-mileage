#-------------------------------------------------------------------------------
# Name:        visual-mileage
# Purpose:     opens multiple Google maps with driving directions for given start-destination pairs
#
# Author:      github.com/eugenius1
# Created:     01/09/2015
# Copyright:   (c) Eusebius Ngemera 2015
#-------------------------------------------------------------------------------

import webbrowser
from Tkinter import *

baseurl = "https://www.google.com/maps"

def gui_main(n):
    global root, variables, entries, col_w
    root = Tk()

    col_w = 50
    btn_w = 20
    variables = []
    entries = []

    Label(root, text="Start").grid(row=0,column=0)
    Label(root, text="End").grid(row=0,column=1)
    Button(root, text='Go!', width=btn_w, command=open_maps).grid(row=0, column=2)
    Button(root, text='Clear all', width=btn_w, command=clear_entries).grid(row=1, column=2)
    Button(root, text='Add pair', width=btn_w, command=add_line).grid(row=2, column=2)

    for unused in range(n):
        add_line()

    root.mainloop()

def clear_entries():
    for e in entries:
        e.delete(0, END)

def add_line():
    add_entry()
    add_entry()

def add_entry():
    va = StringVar()
    en = Entry(root, width=col_w, textvariable=va)
    i = len(entries)
    en.grid(row=(i/2)+1, column=i%2)
    variables.append(va)
    entries.append(en)

def open_maps():
    for i in range(0, len(entries), 2):
        start = entries[i].get()
        end = entries[i+1].get()
        if start and end:
            url = baseurl + "?saddr="+start+"&daddr="+end+"&dirflg=d"
            webbrowser.open(url, new=0, autoraise=True)

n = input("How many journeys to lookup?")
if not isinstance(n, int) or n<=0 or n>101:
    n=5   # default number of entry pairs
gui_main(n)
