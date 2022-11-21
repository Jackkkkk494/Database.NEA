## Jack Wood Course Work

from tkinter import *

def SelectTab():
    window = Tk()
    window.geometry('500x400')
    window.title("SGW: Selection Tab")
    window["bg"] = '#282828'

    SGW = PhotoImage(file ="/Users/macbookpro/Downloads/Logo.drawio.png")
    label = Label(window,image=SGW)
    label.pack(pady=1)
    
    button1 = Button(window,text ="Calendar",height = 1,width = 20,command = CalendarTab)
    button1.pack(pady=10)

    button2 = Button(window,text ="Logout",height = 1,width = 20, command = LoginTab)
    button2.pack(pady=10)
    window.mainloop()

SelectTab()
