## Final Program
## Jack Wood
from tkinter import*
import sqlite3
from turtle import window_width
import tkinter as tk


##Global
global InputScreen
global SelectTab
global BookingsView
global BookingsDelete
global DBView_Table2022
global DBView_Table2023
global DBView_Table2024
global DBView_Table2025   



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
                    Username["bg"] = "red"
                    Password["bg"] = "red"

                else:
                    print(Username.get(),Password.get(),"User not found")
                    Username["bg"] = "red"
                    Password["bg"] = "red"

    # def IncorrectDetails():
    #     IncorrectDetails = PhotoImage(file="/Users/macbookpro/Documents/Python course work/GUI/IncorrectDetails.png")
    #     label=Label(windowLogin, image = IncorrectDetails)
    #     Label.image = IncorrectDetails
    #     label.pack(pady=1)

    def CancelPress(Username,Password):
        Username.delete(0, END)
        Password.delete(0, END)
        Username["bg"] = "#282828"
        Password["bg"] = "#282828"


    def LoginTab():
    
        #windowLogin.geometry('800x600+0+0')
        width= windowLogin.winfo_screenwidth()               
        height= windowLogin.winfo_screenheight()               
        windowLogin.geometry("%dx%d" % (width, height))
        windowLogin.title("SGQ - Calendar Login")
        windowLogin["bg"] = "#282828"
    
        Login = PhotoImage(file = "GUI\LoginGUI.png")
        label = Label(windowLogin, image=Login)
        label.pack(pady=1)

        Username = Entry(windowLogin, bg="#282828",fg="white")
        Password = Entry(windowLogin,bg="#282828",fg="white",show = "*")
        Username.pack(pady=1)
        Password.pack(pady=1)

        Loginbutton = PhotoImage(file ="GUI\loginbutton.png")
        Button1 = Button(windowLogin,image = Loginbutton,command =lambda: Authentication(Username,Password))
        Button1.pack(pady=1)

        CancelButton = PhotoImage(file = "GUI\Cancel.png")
        ButtonC = Button(windowLogin, image = CancelButton,command=lambda: CancelPress(Username,Password))  
        ButtonC.pack(pady=1)
        windowLogin.mainloop()

    LoginTab()

def InputScreen():
    Bookingwindow = Tk()

    conn = sqlite3.connect('SGW_Database.db')

    c = conn.cursor()

    c.execute ("""CREATE TABLE IF NOT EXISTS bookings(
        First_Name text,
        Last_Name text,
        Address text,
        Mobile text,
        Service text,
        Day text,
        Month text,
        Year text
        )""")

    conn.commit
    conn.close



    def Booking_Window():
        width= Bookingwindow.winfo_screenwidth()               
        height= Bookingwindow.winfo_screenheight()               
        Bookingwindow.geometry("%dx%d" % (width, height))
        Bookingwindow.title("SGW: Create a Booking")
        Bookingwindow["bg"] = '#282828'

        def BookingDestroy():
            Bookingwindow.destroy()
            
        def BackToSelect():
            BookingDestroy()
            SelectTab()
    
        def Submit():
            global Booking_Window

            print(First_Name.get(),Last_Name.get(),Address.get(),Mobile.get(),Day_Entry.get(),Service_Entry.get(),Month_Entry.get(),Year_Entry.get())
           
            conn = sqlite3.connect('SGW_Database.db',isolation_level=None)

            c = conn.cursor()

            c.execute("INSERT INTO bookings VALUES (:First_Name,:Last_Name,:Address,:Mobile,:Service,:Day,:Month,:Year)",
                    {
                        'First_Name':First_Name.get(),
                        'Last_Name':Last_Name.get(),
                        'Address':Address.get(),
                        'Mobile':Mobile.get(),
                        'Service':Service_Entry.get(), 
                        'Day':Day_Entry.get(),
                        'Month':Month_Entry.get(),
                        'Year':Year_Entry.get()
                    })

            conn.commit
            conn.close
            
            First_Name.delete(0,END)
            Last_Name.delete(0,END)
            Address.delete(0,END)
            Mobile.delete(0,END)
      
## Creates options for Dropdown Menu's

        S_Options = [
            "Fitting",
            "Sourcing",
            "Fitting and Sourcing"
            ]

        D_Options = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31"
            ]
        
        M_Options = [
            "Jan",
            "Feb",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]

        Y_Options = [
            "2022",
            "2023",
            "2024",
            "2025"
            ]

        Service_Entry = StringVar(Bookingwindow)
        Service_Entry.set(S_Options[0])

        Day_Entry = StringVar(Bookingwindow)
        Day_Entry.set(D_Options[0])

        Month_Entry = StringVar(Bookingwindow)
        Month_Entry.set(M_Options[0])
        
        Year_Entry = StringVar(Bookingwindow)
        Year_Entry.set(Y_Options[0])

    
        Login = PhotoImage(file = "GUI\LoginGUI.png")
        label = Label(Bookingwindow, image=Login)
        label.image = Login
        label.pack(pady=1)
        
                ## Create Text Boxes
        First_Name = Entry(Bookingwindow,bg="#282828",fg="white", width = 30)
        First_Name.pack()
        Last_Name = Entry(Bookingwindow,bg="#282828",fg="white", width = 30)
        Last_Name.pack()
        Address = Entry(Bookingwindow,bg="#282828",fg="white", width = 30)
        Address.pack()
        Mobile = Entry(Bookingwindow,bg="#282828",fg="white",width=30)
        Mobile.pack()
        Service = OptionMenu(Bookingwindow,Service_Entry,*S_Options,)
        Service.configure(width=30,bg="#282828",fg="white")
        Service.pack()
        Day = OptionMenu(Bookingwindow,Day_Entry,*D_Options,)
        Day.configure(width=30,bg="#282828",fg="white")
        Day.pack()
        Month = OptionMenu(Bookingwindow,Month_Entry,*M_Options,)
        Month.configure(width=30,bg="#282828",fg="white")
        Month.pack()
        Year = OptionMenu(Bookingwindow,Year_Entry,*Y_Options)
        Year.configure(width=30,bg="#282828",fg="white")
        Year.pack()   
        
        Book = Button(Bookingwindow,text="Book",command=Submit)
        Book.pack(pady=2)

        Back = Button(Bookingwindow,text="Back",command=BackToSelect)
        Back.pack(pady=2)
                      
        Bookingwindow.mainloop
    Booking_Window()

def SelectTab():
    selectionwindow = Tk()

    def DestroySelect():
        selectionwindow.destroy()

    def Bookings():
        DestroySelect()
        BookingsView()

    def BookingCreate():
        DestroySelect()
        InputScreen()

    def BookingDeletion():
        DestroySelect()
        BookingsDelete()

    def Logout():
        DestroySelect()
        Login()
    
    def Select_Tab():
        width= selectionwindow.winfo_screenwidth()               
        height= selectionwindow.winfo_screenheight()               
        selectionwindow.geometry("%dx%d" % (width, height))
        selectionwindow.title("SGW: Selection Tab")
        selectionwindow["bg"] = '#282828'

        SGW = PhotoImage(file ="GUI\LoginGUI.png")
        label = Label(selectionwindow,image=SGW)
        label.pack(pady=10)
        
        ViewBookings = PhotoImage(file ="GUI\ViewBooking.drawio.png")
        button1 = Button(selectionwindow,image = ViewBookings,command = Bookings)
        button1.pack(pady=10)

        DataInsertion = PhotoImage(file="GUI\DataInsert.drawio.png")
        BookingButton = Button(selectionwindow,image=DataInsertion,command=BookingCreate)
        BookingButton.pack(pady=10)

        # DeleteBooking = PhotoImage(file="")
        DeleteBookingBtn = Button(selectionwindow,text="Delete a Booking",command=BookingDeletion)
        DeleteBookingBtn.pack()


        LogoutButton = PhotoImage(file="GUI\LogoutButton.png")
        button2 = Button(selectionwindow,image = LogoutButton,command = Logout)
        button2.pack(pady=10)

        selectionwindow.mainloop()
    Select_Tab()

def DBView_Table2022():
    global Database_Query2022
    DBView_Window1 = Tk()
    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(DBView_Window1, image=Login)
    label.image = Login
    label.pack(pady=1)
    DBView_Window1.title("Database 2022 View")
    width= DBView_Window1.winfo_screenwidth()               
    height= DBView_Window1.winfo_screenheight()               
    DBView_Window1.geometry("%dx%d" % (width, height))
    DBView_Window1["bg"] = "#282828"

    

    def DB_View1Destroy():
        DBView_Window1.destroy()

    def DBViewBack1():
        DB_View1Destroy()
        BookingsView()

    def Database_Query2022():
            conn = sqlite3.connect("SGW_Database.db")
            c = conn.cursor()
            c.execute("SELECT oid,* FROM bookings WHERE Year='2022'")
            
            MainRecords = c.fetchall()
            Print_MainRecords = ''

            for record in MainRecords:
                Print_MainRecords += str(record) + "\n"
                
                
            MainRecordsshow = Label(DBView_Window1,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
            MainRecordsshow.pack()

            conn.commit
            conn.close

            def DBView_TableMonth22():
                conn = sqlite3.connect("SGW_Database.db")
                c = conn.cursor()
                Select = ("SELECT oid,* FROM bookings WHERE Year='2022'AND Month=?")
                Month_EntryDB = (Month_Entry.get(),)
                c.execute(Select,Month_EntryDB) 
                    
                MainRecords1 = c.fetchall()
                Print_MainRecords1 =''

                for record in MainRecords1:
                    Print_MainRecords1 += str(record) + "\n"
                
                
                    MainRecordsshow1 = Label(DBView_Window1,text=(Print_MainRecords1).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
                    MainRecordsshow1.pack()

                    conn.commit
                    conn.close

            M_Options = [
            "Jan",
            "Feb",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
            
            Month_Entry = StringVar(DBView_Window1)
            Month_Entry.set(M_Options[0])

            Month22 = OptionMenu(DBView_Window1,Month_Entry,*M_Options,)
            Month22.configure(width=30,bg="#282828",fg="white")
            Month22.pack()

            MonthSelect = Button(DBView_Window1,text="View Months bookings",command=DBView_TableMonth22)
            MonthSelect.pack()

            BackBtn = Button(DBView_Window1,text="Back",command = DBViewBack1)
            BackBtn.pack()

            DBView_Window1.mainloop
    DBView_Window1.mainloop
    Database_Query2022()

def DBView_Table2023():
    global Database_Query2023
    DBView_Window2 = Tk()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(DBView_Window2, image=Login)
    label.image = Login
    label.pack(pady=10)

    DBView_Window2.title("Database 2023 View")
    width= DBView_Window2.winfo_screenwidth()               
    height= DBView_Window2.winfo_screenheight()               
    DBView_Window2.geometry("%dx%d" % (width, height))
    DBView_Window2["bg"] = "#282828"


    def DB_View2Destroy():
        DBView_Window2.destroy()

    def DBViewBack2():
        DB_View2Destroy()
        BookingsView()

    def Database_Query2023():
            conn = sqlite3.connect("SGW_Database.db")
            c = conn.cursor()
            c.execute("SELECT oid,* FROM bookings WHERE Year='2023'")
            
            MainRecords = c.fetchall()
            Print_MainRecords = ''

            for record in MainRecords:
                Print_MainRecords += str(record) + "\n"
                
                
            MainRecordsshow = Label(DBView_Window2,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
            MainRecordsshow.pack()

            conn.commit
            conn.close

            def DBView_TableMonth23():
                conn = sqlite3.connect("SGW_Database.db")
                c = conn.cursor()
                Select = ("SELECT oid,* FROM bookings WHERE Year='2023'AND Month=?")
                Month_EntryDB = (Month_Entry.get(),)
                c.execute(Select,Month_EntryDB) 
                    
                MainRecords1 = c.fetchall()
                Print_MainRecords1 =''

                for record in MainRecords1:
                    Print_MainRecords1 += str(record) + "\n"
                
                
                    MainRecordsshow1 = Label(DBView_Window2,text=(Print_MainRecords1).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
                    MainRecordsshow1.pack()

                    conn.commit
                    conn.close

            M_Options = [
            "Jan",
            "Feb",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
            
            Month_Entry = StringVar(DBView_Window2)
            Month_Entry.set(M_Options[0])

            Month22 = OptionMenu(DBView_Window2,Month_Entry,*M_Options,)
            Month22.configure(width=30,bg="#282828",fg="white")
            Month22.pack()

            MonthSelect = Button(DBView_Window2,text="View Months bookings",command=DBView_TableMonth23)
            MonthSelect.pack()

            BackBtn = Button(DBView_Window2,text="Back",command = DBViewBack2)
            BackBtn.pack()

            DBView_Window2.mainloop

    Database_Query2023()

def DBView_Table2024():
    global Database_Query2024
    DBView_Window3 = Tk()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(DBView_Window3, image=Login)
    label.image = Login
    label.pack(pady=10)

    DBView_Window3.title("Database 2024 View")
    width= DBView_Window3.winfo_screenwidth()               
    height= DBView_Window3.winfo_screenheight()               
    DBView_Window3.geometry("%dx%d" % (width, height))
    DBView_Window3["bg"] = "#282828"


    def DB_View3Destroy():
        DBView_Window3.destroy()

    def DBViewBack3():
        DB_View3Destroy()
        BookingsView()

    def Database_Query2024():
            global DBView_Window
            conn = sqlite3.connect("SGW_Database.db")
            c = conn.cursor()
            c.execute("SELECT oid,* FROM bookings WHERE Year='2024'")
            
            MainRecords = c.fetchall()
            Print_MainRecords = ''

            for record in MainRecords:
                Print_MainRecords += str(record) + "\n"
                
                
            MainRecordsshow = Label(DBView_Window3,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
            MainRecordsshow.pack()

            conn.commit
            conn.close

            def DBView_TableMonth24():
                conn = sqlite3.connect("SGW_Database.db")
                c = conn.cursor()
                Select = ("SELECT oid,* FROM bookings WHERE Year='2024'AND Month=?")
                Month_EntryDB = (Month_Entry.get(),)
                c.execute(Select,Month_EntryDB) 
                    
                MainRecords1 = c.fetchall()
                Print_MainRecords1 =''

                for record in MainRecords1:
                    Print_MainRecords1 += str(record) + "\n"
                
                
                    MainRecordsshow1 = Label(DBView_Window3,text=(Print_MainRecords1).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
                    MainRecordsshow1.pack()

                    conn.commit
                    conn.close

            M_Options = [
            "Jan",
            "Feb",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
            
            Month_Entry = StringVar(DBView_Window3)
            Month_Entry.set(M_Options[0])

            Month22 = OptionMenu(DBView_Window3,Month_Entry,*M_Options,)
            Month22.configure(width=30,bg="#282828",fg="white")
            Month22.pack()

            MonthSelect = Button(DBView_Window3,text="View Months bookings",command=DBView_TableMonth24)
            MonthSelect.pack()

            BackBtn = Button(DBView_Window3,text="Back",command = DBViewBack3)
            BackBtn.pack()

            DBView_Window3.mainloop

    Database_Query2024()

def DBView_Table2025():
    global Database_Query2025
    DBView_Window4 = Tk()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(DBView_Window4, image=Login)
    label.image = Login
    label.pack(pady=10)

    DBView_Window4.title("Database 2025 View")
    width= DBView_Window4.winfo_screenwidth()               
    height= DBView_Window4.winfo_screenheight()               
    DBView_Window4.geometry("%dx%d" % (width, height))
    DBView_Window4["bg"] = "#282828"


    def DB_View4Destroy():
        DBView_Window4.destroy()

    def DBViewBack4():
        DB_View4Destroy()
        BookingsView()

    def Database_Query2025():
            conn = sqlite3.connect("SGW_Database.db")
            c = conn.cursor()
            c.execute("SELECT oid,* FROM bookings WHERE Year='2025'")
            
            MainRecords = c.fetchall()
            Print_MainRecords = ''

            for record in MainRecords:
                Print_MainRecords += str(record) + "\n"
                
                
            MainRecordsshow = Label(DBView_Window4,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
            MainRecordsshow.pack()

            conn.commit
            conn.close
            
            def DBView_TableMonth25():
                conn = sqlite3.connect("SGW_Database.db")
                c = conn.cursor()
                Select = ("SELECT oid,* FROM bookings WHERE Year='2025'AND Month=?")
                Month_EntryDB = (Month_Entry.get(),)
                c.execute(Select,Month_EntryDB) 
                    
                MainRecords1 = c.fetchall()
                Print_MainRecords1 =''

                for record in MainRecords1:
                    Print_MainRecords1 += str(record) + "\n"
                
                    MainRecordsshow1 = Label(DBView_Window4,text=(Print_MainRecords1).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
                    MainRecordsshow1.pack()

                    conn.commit
                    conn.close

            M_Options = [
            "Jan",
            "Feb",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
            
            Month_Entry = StringVar(DBView_Window4)
            Month_Entry.set(M_Options[0])

            Month22 = OptionMenu(DBView_Window4,Month_Entry,*M_Options,)
            Month22.configure(width=30,bg="#282828",fg="white")
            Month22.pack()

            MonthSelect = Button(DBView_Window4,text="View Months bookings",command=DBView_TableMonth25)
            MonthSelect.pack()

            BackBtn = Button(DBView_Window4,text="Back",command = DBViewBack4)
            BackBtn.pack()
            DBView_Window4.mainloop
            
    Database_Query2025()

def BookingsDelete():
    BookingDeleteWindow = Tk()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(BookingDeleteWindow, image=Login)
    label.image = Login
    label.pack(pady=1)

    def BookingsDelete():
        BookingDeleteWindow.destroy()
    
    def Back2Select():
        BookingsDelete()
        SelectTab()

    def BookingsDeleteView():
        width= BookingDeleteWindow.winfo_screenwidth()               
        height= BookingDeleteWindow.winfo_screenheight()               
        BookingDeleteWindow.geometry("%dx%d" % (width, height))
        BookingDeleteWindow.title("SGW:Delete a Booking")
        BookingDeleteWindow["bg"] = '#282828'

        def Database_Whole():
            conn = sqlite3.connect("SGW_Database.db")
            c = conn.cursor()
            c.execute("SELECT oid,* FROM bookings")
            
            MainRecords = c.fetchall()
            Print_MainRecords = ''

            for record in MainRecords:
                Print_MainRecords += str(record) + "\n"
    
            MainRecordsshow = Label(BookingDeleteWindow,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
            MainRecordsshow.pack()

            conn.commit

            conn.close

        Database_Whole()

        def Delete():
            conn = sqlite3.connect("SGW_Database.db",isolation_level=None)
            c = conn.cursor()

            c.execute("DELETE FROM bookings WHERE oid = " + ID_Entry.get())
    
        ID_Entry = Entry(BookingDeleteWindow,bg="#282828",fg="white", width = 30)
        ID_Entry.pack(pady=10)

        DeleteBtn = Button(BookingDeleteWindow,text="Delete",command=Delete)
        DeleteBtn.pack()

        BackBtn = Button(BookingDeleteWindow,text="Back",command = Back2Select)
        BackBtn.pack()
        
    BookingsDeleteView()

def BookingsView():
    bookingswindow = Tk()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(bookingswindow, image=Login)
    label.image = Login
    label.pack(pady=1)

    def BookingsViewDestroy():
        bookingswindow.destroy()

    def Back2Select():
        BookingsViewDestroy()
        SelectTab()

    def Booking_View():

        #calendarwindow.geometry('1560x1080')
        width= bookingswindow.winfo_screenwidth()               
        height= bookingswindow.winfo_screenheight()               
        bookingswindow.geometry("%dx%d" % (width, height))
        bookingswindow.title("SGW: Bookings View")
        bookingswindow["bg"] = '#282828'


        def Booking_Destroy():
            bookingswindow.destroy()

        def DBView22():
            Booking_Destroy()
            DBView_Table2022()

        def DBView23():
            Booking_Destroy()
            DBView_Table2023()

        def DBView24():
            Booking_Destroy()
            DBView_Table2024()

        def DBView25():
            Booking_Destroy()
            DBView_Table2025()               

        # def Database_Query2022():
        #     conn = sqlite3.connect("SGW_Database.db")
        #     c = conn.cursor()
        #     c.execute("SELECT oid,* FROM bookings WHERE Year='2022'")
            
        #     MainRecords = c.fetchall()
        #     Print_MainRecords = ''

        #     for record in MainRecords:
        #         Print_MainRecords += str(record) + "\n"
                
                
        #     MainRecordsshow = Label(DBView_Window,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
        #     MainRecordsshow.pack()

        #     conn.commit
        #     conn.close
        # Database_Query2022()

        # def Database_Query2023():
        #     conn = sqlite3.connect("SGW_Database.db")
        #     c = conn.cursor()
        #     c.execute("SELECT oid,* FROM bookings WHERE Year='2023'")
            
        #     MainRecords = c.fetchall()
        #     Print_MainRecords = ''

        #     for record in MainRecords:
        #         Print_MainRecords += str(record) + "\n"
                
                
        #     MainRecordsshow = Label(bookingswindow,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
        #     MainRecordsshow.pack()

        #     conn.commit
        #     conn.close
        # Database_Query2023()

        # def Database_Query2024():
        #     conn = sqlite3.connect("SGW_Database.db")
        #     c = conn.cursor()
        #     c.execute("SELECT oid,* FROM bookings WHERE Year='2024'")
            
        #     MainRecords = c.fetchall()
        #     Print_MainRecords = ''

        #     for record in MainRecords:
        #         Print_MainRecords += str(record) + "\n"
                
                
        #     MainRecordsshow = Label(DBView_Table2022,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
        #     MainRecordsshow.pack()

        #     conn.commit
        #     conn.close
        # Database_Query2024()

        # def Database_Query2025():
        #     conn = sqlite3.connect("SGW_Database.db")
        #     c = conn.cursor()
        #     c.execute("SELECT oid,* FROM bookings WHERE Year='2025'")
            
        #     MainRecords = c.fetchall()
        #     Print_MainRecords = ''

        #     for record in MainRecords:
        #         Print_MainRecords += str(record) + "\n"
                
                
        #     MainRecordsshow = Label(bookingswindow,text=(Print_MainRecords).replace('(','').replace(')','').replace(',','').replace('[','').replace(']','').replace("'",""), bg = "#282828",fg="white")
        #     MainRecordsshow.pack()

        #     conn.commit
        #     conn.close
        # Database_Query2025()

        ViewBooking2022 = Button(bookingswindow,text="View Bookings from 2022",command =DBView22)
        ViewBooking2022.pack()

        ViewBooking2023 = Button(bookingswindow,text="View Bookings from 2023",command=DBView23)
        ViewBooking2023.pack()

        ViewBooking2024 = Button(bookingswindow,text="View Bookings from 2024",command=DBView24)
        ViewBooking2024.pack()

        ViewBooking2025 = Button(bookingswindow,text="View Bookings from 2025",command=DBView25)
        ViewBooking2025.pack()

        BackBtn = Button(bookingswindow,text="Back",command = Back2Select)
        BackBtn.pack()

        bookingswindow.mainloop()

    Booking_View()
   
Login()