#design work

from tkinter import *

def LoginTab():
    window = Tk()
    window.geometry('400x400')
    window.title("SGW: Calendar Login")
    window["bg"] = "#282828"
    Login = PhotoImage(file ="/Users/macbookpro/Documents/Python/loginhud.drawio.png")
    label = Label(window,image=Login)
    label.image = Login
    label.pack(pady=1)

    text1 = Text(window,height = 1.5, width = 20)
    text2 = Text(window,height = 1.5, width = 20)
    text1.pack(pady=1)
    text2.pack(pady=1)

    Loginbutton = PhotoImage(file ="/Users/macbookpro/Documents/Python/loginbutton.png")
    label2 = Button(window,image=Loginbutton,command = SelectTab)
    label2.pack(pady=1)
    
    window.mainloop()
def SelectTab():
    window = Tk()
    window.geometry('300x200')
    window.title("SGW: Selection Tab")
    window["bg"] = '#282828'

    SGW = PhotoImage(file ="/Users/macbookpro/Downloads/Logo.drawio.png")
    label = Label(window,image=SGW)
    label.pack(pady=1)
    
    button1 = Button(window,text ="Calendar",height = 1,width = 20,command = CalendarTab)
    button1.pack(pady=10)

    button2 = Button(window,text ="Logout",height = 1,width = 20, command = LoginTab)
    button2.pack(pady=10)
    

def CalendarTab():
    window = Tk()
    window.geometry('600x600')
    window.title("SGW: Calendar Tab")
    window["bg"] = '#282828'
    CalendarGUI = PhotoImage(file ="/Users/macbookpro/Downloads/Calendar.drawio.png")
    label4 = Label(window, image=CalendarGUI)
    label4.image = CalendarGUI
    label4.pack(pady=20)

    

LoginTab()

