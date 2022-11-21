## Jack Wood - Course Work

from tkinter import *


def CalendarTab():
    window = Tk()
    window.geometry('600x600')
    window.title("SGW: Calendar Tab")
    window["bg"] = '#282828'
    CalendarGUI = PhotoImage(file ="/Users/macbookpro/Downloads/Calendar.drawio.png")
    label4 = Label(window, image=CalendarGUI)
    label4.image = CalendarGUI
    label4.pack(pady=20)

    window.mainloop()

CalendarTab()
    
