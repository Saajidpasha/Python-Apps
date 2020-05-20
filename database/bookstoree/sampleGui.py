import tkinter
import json
from difflib import get_close_matches
class Gui:
    word = StringVar()
    def __init__(self):
        window = Tk()

        e = Entry(window,textvariable = word)
        e.grid(row=0,column=0)
        b = Button(window,text="Search",width=12,command = search)
        b.grid(row=0,column=1)
        listbox = Listbox(window,height=6,width=35)
        listbox.grid(row=1,column=0,rowspan=6,columnspan=2)
        scrollbar = Scrollbar(window)
        scrollbar.grid(row=1,column=2,rowspan=6)
        listbox.configure(yscrollcommand = scrollbar.set)
        scrollbar.configure(command=listbox.yview)
        window.mainloop()
    def search():
        data = json.load(".json")
        word = lower(word)
        if word in data:
            rows =  data[word]
            listbox.insert(END,rows)

        elif len(get_close_matches(word,data.keys())) > 0:
            rows = ("Did you mean %s instead ? "%get_close_matches(word,data.keys()))
            listbox.insert(END,rows)
            if Y == 'y' or Y=='Y':
                listbox.insert(END,get_close_matches(word,data.keys()))
            elif yn == 'N' or yn == 'n':
                listbox.insert(END,"The word doesnt exist please cheeck it again.")
            else:
                listbox.insert(END, "Please enter a valid option.")
Gui()
