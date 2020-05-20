from tkinter import *#importing everythingg
import backend
def get_selected_rows(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])





def view_command():
    listbox.delete(0,END)
    for rows in backend.view():
        listbox.insert(END,rows)

def search_command():
    listbox.delete(0,END)
    for rows in backend.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
        listbox.insert(END,rows)

def addEntry_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    listbox.delete(0,END)
    listbox.insert(END,(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])






def update_command():

    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())




window = Tk()#making window object
l1 = Label(window,text="Title")
l1.grid(row = 0,column=0)
l2 = Label(window,text="Author")
l2.grid(row = 0,column=2)
l3 = Label(window,text="Year")
l3.grid(row = 1,column=0)
l4 = Label(window,text="ISBN")
l4.grid(row = 1,column=2)
title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
author_text = StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)
year_text = StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)
ISBN_text = StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)
listbox = Listbox(window,height=6,width=35)
listbox.grid(row=2,column=0,rowspan = 6,columnspan = 2)
s1 = Scrollbar(window)
s1.grid(row=2,column=2,rowspan=6)
listbox.configure(yscrollcommand=s1.set)

s1.configure(command=listbox.yview)
listbox.bind('<<ListboxSelect>>',get_selected_rows)
b1=Button(window,text="viewAll",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="search entry",width=12,command = search_command)
b2.grid(row=3,column=3)
b3 = Button(window,text="addEntry",width=12,command = addEntry_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command = update_command)
b4.grid(row=5,column=3)

b4=Button(window,text="Delete",width=12,command = delete_command)
b4.grid(row=6,column=3)
b4=Button(window,text="close",width=12,command=window.destroy)
b4.grid(row=7,column=3)

window.mainloop()
