from tkinter import *
import app1

def search_command():

    listbox.delete(0,END)
    output = app1.translate(word.get())
    if type(output) == list:
        for item in output:
            listbox.insert(END,item)
    else:
        listbox.insert(END,output)


window = Tk()
word = StringVar()
e = Entry(window,textvariable = word)
e.grid(row=0,column=0)

listbox = Listbox(window,height=6,width=35)
listbox.grid(row=1,column=0,rowspan=6,columnspan=2)
scrollbar = Scrollbar(window)
scrollbar.grid(row=1,column=2,rowspan=6)
listbox.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command=listbox.yview)
b = Button(window,text="Search",width=12,command = search_command)
b.grid(row=0,column=1)
window.mainloop()
