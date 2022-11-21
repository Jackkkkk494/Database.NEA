## Prototype 2
## Jack Wood

from tkinter import*

##Global

def Login():
    windowLogin = Tk()   
    def DestroyLogin():
        windowLogin.destroy()
    def Select():
        DestroyLogin()
        SelectTab()
    def Authentication(Username,Password):
            result = 0
            if Username and Password:
                with open("passwords.txt") as f:
                    for line in f:
                        user, _ , pwd = line.strip().partition(";")
                        result = ((user == Username.get()) + (pwd == Password.get())) or result
                        if result == 2:
                            break
                if result == 2:
                    print ("Welcome",Username.get(), Password.get())
                    Select()
                elif result:
                    print(Username.get(), Password.get(),"Wrong Username or Password")
                else:
                    print(Username.get(),Password.get(),"User not found")
    def LoginTab():
    
        windowLogin.geometry('800x600')
        windowLogin.title("SGQ - Calendar Login")
        windowLogin["bg"] = "#282828"
        Login = PhotoImage(file = "/Users/macbookpro/Documents/Python course work/LoginGUI.png")
        label = Label(windowLogin, image=Login)
        label.image = Login
        label.pack(pady=1)

        Username = Entry(windowLogin)
        Password = Entry(windowLogin)
        Username.pack(pady=1)
        Password.pack(pady=1)


        Loginbutton = PhotoImage(file ="/Users/macbookpro/Documents/Python course work/loginbutton.png")
        Button1 = Button(windowLogin,image = Loginbutton,command =lambda: Authentication(Username,Password))
        Button1.pack(pady=1)
        windowLogin.mainloop()
    LoginTab()

def SelectTab():
    selectionwindow = Tk()

    def DestroySelect():
        selectionwindow.destroy()

    def Calendar():
        DestroySelect()
        CalendarTab()

    def Logout():
        DestroySelect()
        Login()
    
    def Select_Tab():
        
        selectionwindow.geometry('600x600')
        selectionwindow.title("SGW: Selection Tab")
        selectionwindow["bg"] = '#282828'

        SGW = PhotoImage(file ="/Users/macbookpro/Documents/Python course work/Logo.drawio.png")
        label = Label(selectionwindow,image=SGW)
        label.pack(pady=10)
        
        button1 = Button(selectionwindow,text ="Calendar",height = 1,width = 20,command = Calendar)
        button1.pack(pady=10)
        button2 = Button(selectionwindow,text ="Logout",height = 1,width = 20,command = Logout)
        button2.pack(pady=10)   

        selectionwindow.mainloop()
    Select_Tab()

def CalendarTab():
    calendarwindow = Tk()
        
    def Calendar_Tab():
        calendarwindow.geometry('600x600')
        calendarwindow.title("SGW: Calendar Tab")
        calendarwindow["bg"] = '#282828'

        CalendarGUI = PhotoImage(file ="/Users/macbookpro/Documents/Python course work/Calendar.drawio.png")
        label = Label(calendarwindow,image=CalendarGUI)
        label.image = CalendarGUI
        label.pack(pady=1)
    calendarwindow.mainloop()    

    Calendar_Tab()
    
Login()



    
