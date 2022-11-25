## Final Program
## Jack Wood
from tkinter import*
import sqlite3
from turtle import window_width
import tkinter.ttk as ttk
from tkinter import font

##Global
global InputScreen
global SelectTab
global DBView
global BookingsDelete
global DeleteWindow


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
        label.pack(pady=10)

        Username = Entry(windowLogin,font=('MsSerif 14 bold'),bg="#282828",fg="white",justify=CENTER,highlightbackground="white",highlightthickness=3,bd=0)
        Password = Entry(windowLogin,font=('MsSerif 14 bold'),bg="#282828",fg="white",justify=CENTER,show = "*",highlightbackground="white",highlightthickness=3,bd=0)
        Username.pack(pady=3)
        Password.pack(pady=3)

        ButtonLogin = Button(windowLogin,text="LOGIN",font=('MsSerif 14 bold'),highlightbackground="White",highlightthickness=5,bd=0,command =lambda: Authentication(Username,Password))
        ButtonLogin.configure(width=8)
        ButtonLogin.pack(pady=3)

        ButtonC = Button(windowLogin,text="CANCEL",font=('MsSeif 14 bold'),highlightbackground="White",highlightthickness=5,bd=0,command=lambda: CancelPress(Username,Password))  
        ButtonC.configure(width=8)
        ButtonC.pack(pady=3)
        windowLogin.mainloop()

    LoginTab() 

def SelectTab():
    selectionwindow = Tk()

    def DestroySelect():
        selectionwindow.destroy()

    def DB_Viewer():
        DestroySelect()
        DBView()

    def DB_AddViewer():
        DestroySelect()
        DBAdd()

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
        label.pack(pady=3)

        DBViewBtn = Button(selectionwindow,text="VIEW BOOKINGS",font=('MsSeif 14 bold'),highlightbackground="#282828",highlightthickness=5,bd=0,command = DB_Viewer)
        DBViewBtn.pack(pady=3)

        DBViewBtn = Button(selectionwindow,text="EDIT BOOKINGS",font=('MsSeif 14 bold'),highlightbackground="#282828",highlightthickness=5,bd=0,command = DB_AddViewer)
        DBViewBtn.pack(pady=3)
        
        LogoutBtn = Button(selectionwindow,text="LOGOUT",font=('MsSeif 14 bold'),highlightbackground="#282828",highlightthickness=5,bd=0,command = Logout)
        LogoutBtn.pack(pady=3)

        selectionwindow.mainloop()
    Select_Tab()   

def DBView():
    DBView_Window = Tk()

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

    def BookingsViewDestroy():
        DBView_Window.destroy()

    def Back2Select():
        BookingsViewDestroy()
        SelectTab()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(DBView_Window, image=Login)
    label.image = Login
    label.pack(pady=10)
    
    def DB_ViewTable():
        DBView_Window.title("Database Full View")
        width= DBView_Window.winfo_screenwidth()               
        height= DBView_Window.winfo_screenheight()               
        DBView_Window.geometry("%dx%d" % (width, height))
        DBView_Window["bg"] = "#282828"

        #Styling Table
        Style = ttk.Style()
        # Theme Choice
        Style.theme_use("clam")
        # Configuring the colour
        Style.configure("Treeview",
            background= "white",
            foreground="black",
            rowheight=25,
            fieldbackground="white") 

        #Selection colour 
        Style.map('Treeview',
            background=[('selected','#203354')])

        #Created a Treeview Frame    
        Table_All = Frame(DBView_Window)
        Table_All.pack(pady=10)

        #Treeview Scrollbar   
        Table_AllScroll = Scrollbar(Table_All)
        Table_AllScroll.pack(side=RIGHT, fill=Y)

        #Creates Table
        MYTable_All = ttk.Treeview(Table_All, yscrollcommand=Table_AllScroll.set,selectmode="extended")
        MYTable_All.pack()

        #Config Scrollbar
        Table_AllScroll.config(command=MYTable_All.yview)
        
        #Defining Columns
        MYTable_All['columns']=('ID','Client_FirstName','Client_Surname','Client_Postcode','Client_Mobile','Service','Day','Month','Year')

        MYTable_All.column("#0",width=0,stretch=NO)
        MYTable_All.column("ID",anchor=CENTER,width=120)
        MYTable_All.column("Client_FirstName",anchor=W, width=120,minwidth=120)
        MYTable_All.column("Client_Surname",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Client_Postcode",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Client_Mobile",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Service",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Day",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Month",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Year",anchor=W,width=120,minwidth=120)

        MYTable_All.heading('#0',text='',anchor=W)
        MYTable_All.heading("ID",text="Booking ID",anchor=CENTER)
        MYTable_All.heading("Client_FirstName",text="Clients Name",anchor=W)
        MYTable_All.heading("Client_Surname",text="Clients Surname",anchor=W)
        MYTable_All.heading("Client_Postcode",text="Postcode",anchor=W)
        MYTable_All.heading("Client_Mobile",text="Mobile",anchor=W)
        MYTable_All.heading("Service",text="Service",anchor=W)
        MYTable_All.heading("Day",text="Day",anchor=W)
        MYTable_All.heading("Month",text="Month",anchor=W)
        MYTable_All.heading("Year",text="Year",anchor=W)

        MYTable_All.tag_configure('evenrow',background="#282828",foreground="white")
        MYTable_All.tag_configure('oddrow',background="#D3D3D3")

        conn = sqlite3.connect("SGW_Database.db")
        c = conn.cursor()

        c.execute("SELECT rowid,* FROM bookings")
        records = c.fetchall()

        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                MYTable_All.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]),tags=('evenrow',))
                MYTable_All.pack()
            else:
                MYTable_All.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]),tags=('oddrow',))
            count += 1          
        conn.commit
        conn.close

        # Add Record Entry Box
        data_frame = LabelFrame(Table_All,text="Records")
        data_frame.pack(fill="x",expand="yes",padx=20)

        id_l = Label(data_frame, text="ID")
        id_l.grid(row=0,column=0,padx=8,pady=10)
        id_entry = Entry(data_frame)
        id_entry.grid(row=0,column=1,padx=8,pady=10)

        firstn_l = Label(data_frame, text="Client Name")
        firstn_l.grid(row=0,column=2,padx=8,pady=10)
        firstn_entry = Entry(data_frame)
        firstn_entry.grid(row=0,column=3,padx=8,pady=10)

        lastn = Label(data_frame, text="Surname")
        lastn.grid(row=0,column=4,padx=8,pady=10)
        lastn_entry = Entry(data_frame)
        lastn_entry.grid(row=0,column=5,padx=8,pady=10)

        postcode_l = Label(data_frame, text="Postcode")
        postcode_l.grid(row=0,column=6,padx=8,pady=10)
        postcode_entry = Entry(data_frame)
        postcode_entry.grid(row=0,column=7,padx=8,pady=10)

        mobile_l = Label(data_frame, text="Mobile")
        mobile_l.grid(row=1,column=0,padx=8,pady=10)
        mobile_entry = Entry(data_frame)
        mobile_entry.grid(row=1,column=1,padx=8,pady=10)

        service_l = Label(data_frame, text="Service")
        service_l.grid(row=1,column=2,padx=8,pady=10)
        service_entry = Entry(data_frame)
        service_entry.grid(row=1,column=3,padx=8,pady=10)

        day_l = Label(data_frame, text="Day")
        day_l.grid(row=1,column=4,padx=8,pady=10)
        day_entry = Entry(data_frame)
        day_entry.grid(row=1,column=5,padx=8,pady=10)

        month_l = Label(data_frame, text="Month")
        month_l.grid(row=1,column=6,padx=8,pady=10)
        month_entry = Entry(data_frame)
        month_entry.grid(row=1,column=7,padx=8,pady=10)

        year_l = Label(data_frame, text="Year")
        year_l.grid(row=1,column=8,padx=8,pady=10)
        year_entry = Entry(data_frame)
        year_entry.grid(row=1,column=9,padx=8,pady=10)

        def selectpress(e):
            # Wipe entry boxes
            id_entry.delete(0,END)
            firstn_entry.delete(0,END)
            lastn_entry.delete(0,END)
            postcode_entry.delete(0,END)
            mobile_entry.delete(0,END)
            service_entry.delete(0,END)
            day_entry.delete(0,END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)

            # Grab Record Number
            Selected = MYTable_All.focus()
            Details = MYTable_All.item(Selected,'values')

            #Insert to EntryBox
            id_entry.insert(0,Details[0])
            firstn_entry.insert(0,Details[1])
            lastn_entry.insert(0,Details[2])
            postcode_entry.insert(0,Details[3])
            mobile_entry.insert(0,Details[4])
            service_entry.insert(0,Details[5])
            day_entry.insert(0,Details[6])
            month_entry.insert(0,Details[7])
            year_entry.insert(0,Details[8])

        def clearentry():
            id_entry.delete(0,END)
            firstn_entry.delete(0,END)
            lastn_entry.delete(0,END)
            postcode_entry.delete(0,END)
            mobile_entry.delete(0,END)
            service_entry.delete(0,END)
            day_entry.delete(0,END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)


        Clear = Button(data_frame,text='Clear Entry Boxes',command=clearentry)
        Clear.grid(row=2,column=0,padx=8,pady=10)

        # binding treeview
        MYTable_All.bind("<ButtonRelease-1>",selectpress)

        BackBtn = Button(DBView_Window,text="Back",font=('MsSeif 14 bold'),highlightbackground="#282828",highlightthickness=5,bd=0,command = Back2Select)
        BackBtn.pack(pady=10)
        DBView_Window.mainloop
    DB_ViewTable()

def DBAdd():
    DBAdd_Window = Tk()

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

    def ADDDestroy():
        DBAdd_Window.destroy()

    def Back2Select():
        ADDDestroy()
        SelectTab()

    Login = PhotoImage(file = "GUI\LoginGUI.png")
    label = Label(DBAdd_Window, image=Login)
    label.image = Login
    label.pack(pady=10)
    
    def DB_ViewTable():
        DBAdd_Window.title("Database Full View")
        width= DBAdd_Window.winfo_screenwidth()               
        height= DBAdd_Window.winfo_screenheight()               
        DBAdd_Window.geometry("%dx%d" % (width, height))
        DBAdd_Window["bg"] = "#282828"

        #Styling Table
        Style = ttk.Style()
        # Theme Choice
        Style.theme_use("clam")
        # Configuring the colour
        Style.configure("Treeview",
            background= "white",
            foreground="black",
            rowheight=25,
            fieldbackground="white") 

        #Selection colour 
        Style.map('Treeview',
            background=[('selected','#203354')])

        #Created a Treeview Frame    
        Table_All = Frame(DBAdd_Window)
        Table_All.pack(pady=10)

        #Treeview Scrollbar   
        Table_AllScroll = Scrollbar(Table_All)
        Table_AllScroll.pack(side=RIGHT, fill=Y)

        #Creates Table
        MYTable_All = ttk.Treeview(Table_All, yscrollcommand=Table_AllScroll.set,selectmode="extended")
        MYTable_All.pack()

        #Config Scrollbar
        Table_AllScroll.config(command=MYTable_All.yview)
        
        #Defining Columns
        MYTable_All['columns']=('ID','Client_FirstName','Client_Surname','Client_Postcode','Client_Mobile','Service','Day','Month','Year')

        MYTable_All.column("#0",width=0,stretch=NO)
        MYTable_All.column("ID",anchor=CENTER,width=120)
        MYTable_All.column("Client_FirstName",anchor=W, width=120,minwidth=120)
        MYTable_All.column("Client_Surname",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Client_Postcode",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Client_Mobile",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Service",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Day",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Month",anchor=W,width=120,minwidth=120)
        MYTable_All.column("Year",anchor=W,width=120,minwidth=120)

        MYTable_All.heading('#0',text='',anchor=W)
        MYTable_All.heading("ID",text="Booking ID",anchor=CENTER)
        MYTable_All.heading("Client_FirstName",text="Clients Name",anchor=W)
        MYTable_All.heading("Client_Surname",text="Clients Surname",anchor=W)
        MYTable_All.heading("Client_Postcode",text="Postcode",anchor=W)
        MYTable_All.heading("Client_Mobile",text="Mobile",anchor=W)
        MYTable_All.heading("Service",text="Service",anchor=W)
        MYTable_All.heading("Day",text="Day",anchor=W)
        MYTable_All.heading("Month",text="Month",anchor=W)
        MYTable_All.heading("Year",text="Year",anchor=W)

        MYTable_All.tag_configure('evenrow',background="#282828",foreground="white")
        MYTable_All.tag_configure('oddrow',background="#D3D3D3")

        conn = sqlite3.connect("SGW_Database.db")
        c = conn.cursor()

        c.execute("SELECT rowid,* FROM bookings")
        records = c.fetchall()

        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                MYTable_All.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]),tags=('evenrow',))
                MYTable_All.pack()
            else:
                MYTable_All.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]),tags=('oddrow',))
            count += 1          
        conn.commit
        conn.close

        # Add Record Entry Box
        data_frame = LabelFrame(Table_All,text="Records")
        data_frame.pack(fill="x",expand="yes",padx=20)

        id_l = Label(data_frame, text="ID")
        id_l.grid(row=0,column=0,padx=8,pady=10)
        id_entry = Entry(data_frame)
        id_entry.grid(row=0,column=1,padx=8,pady=10)

        firstn_l = Label(data_frame, text="Client Name")
        firstn_l.grid(row=0,column=2,padx=8,pady=10)
        firstn_entry = Entry(data_frame)
        firstn_entry.grid(row=0,column=3,padx=8,pady=10)

        lastn = Label(data_frame, text="Surname")
        lastn.grid(row=0,column=4,padx=8,pady=10)
        lastn_entry = Entry(data_frame)
        lastn_entry.grid(row=0,column=5,padx=8,pady=10)

        postcode_l = Label(data_frame, text="Postcode")
        postcode_l.grid(row=0,column=6,padx=8,pady=10)
        postcode_entry = Entry(data_frame)
        postcode_entry.grid(row=0,column=7,padx=8,pady=10)

        mobile_l = Label(data_frame, text="Mobile")
        mobile_l.grid(row=1,column=0,padx=8,pady=10)
        mobile_entry = Entry(data_frame)
        mobile_entry.grid(row=1,column=1,padx=8,pady=10)

        service_l = Label(data_frame, text="Service")
        service_l.grid(row=1,column=2,padx=8,pady=10)
        service_entry = Entry(data_frame)
        service_entry.grid(row=1,column=3,padx=8,pady=10)

        day_l = Label(data_frame, text="Day")
        day_l.grid(row=1,column=4,padx=8,pady=10)
        day_entry = Entry(data_frame)
        day_entry.grid(row=1,column=5,padx=8,pady=10)

        month_l = Label(data_frame, text="Month")
        month_l.grid(row=1,column=6,padx=8,pady=10)
        month_entry = Entry(data_frame)
        month_entry.grid(row=1,column=7,padx=8,pady=10)

        year_l = Label(data_frame, text="Year")
        year_l.grid(row=1,column=8,padx=8,pady=10)
        year_entry = Entry(data_frame)
        year_entry.grid(row=1,column=9,padx=8,pady=10)

        def selectpress(e):
            global DBView
            # Wipe entry boxes
            id_entry.delete(0,END)
            firstn_entry.delete(0,END)
            lastn_entry.delete(0,END)
            postcode_entry.delete(0,END)
            mobile_entry.delete(0,END)
            service_entry.delete(0,END)
            day_entry.delete(0,END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)

            # Grab Record Number
            Selected = MYTable_All.focus()
            Details = MYTable_All.item(Selected,'values')

            #Insert to EntryBox
            id_entry.insert(0,Details[0])
            firstn_entry.insert(0,Details[1])
            lastn_entry.insert(0,Details[2])
            postcode_entry.insert(0,Details[3])
            mobile_entry.insert(0,Details[4])
            service_entry.insert(0,Details[5])
            day_entry.insert(0,Details[6])
            month_entry.insert(0,Details[7])
            year_entry.insert(0,Details[8])

        def clearentry():
            id_entry.delete(0,END)
            firstn_entry.delete(0,END)
            lastn_entry.delete(0,END)
            postcode_entry.delete(0,END)
            mobile_entry.delete(0,END)
            service_entry.delete(0,END)
            day_entry.delete(0,END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)


        Clear_button = Button(data_frame,text='Clear Entry Boxes',command=clearentry)
        Clear_button.grid(row=2,column=0,padx=8,pady=10)

        update_button = Button(data_frame,text='Edit Booking')
        update_button.grid(row=2,column=1,padx=8,pady=10)

        add_button = Button(data_frame,text='Add Booking')
        add_button.grid(row=2,column=2,padx=8,pady=10)

        # binding treeview
        MYTable_All.bind("<ButtonRelease-1>",selectpress)

        BackBtn = Button(DBAdd_Window,text="Back",font=('MsSeif 14 bold'),highlightbackground="#282828",highlightthickness=5,bd=0,command = Back2Select)
        BackBtn.pack(pady=10)
        DBAdd_Window.mainloop
    DB_ViewTable()
Login()

