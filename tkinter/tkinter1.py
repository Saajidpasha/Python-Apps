#tkinter is used for gui
from tkinter import *#importing everythingg
window = Tk()#making window object
def k_m():#this function will run when the button is clicked
    print(e1_value.get())
    rupees = int(e1_value.get())*67
    t.insert(END,rupees)
b = Button(window,text="Execute",command=k_m)#command arg is used to invoke the f/n
b.grid(row=0,column=0)
e1_value = StringVar() #getting the string value from the window

e = Entry(window,textvariable = e1_value)#a text box,textvariable points tp var which has string
e.grid(row=0,column=1)
t=Text(window,height=1,width=20)
t.grid(row=0,column=2)
window.mainloop()#this is used to keep the window stay On else closes
