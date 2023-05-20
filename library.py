from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
import tkinter.messagebox as mb
import mysql.connector as mc
from tkcalendar import DateEntry
import datetime


class library:
    def __init__(self,bf):
        self.libraryFrame = Frame(bf, pady=10, padx=100)
        self.libraryFrame.grid(row=1, column=0, sticky='senw')
        self.img4 = Image.open('library.png')
        self.img4.thumbnail((200, 200))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.libraryFrame, image=self.new_img4, padx=10, pady=10)
        self.imgLibrary.pack()

        self.buttonLibrary = Button(self.libraryFrame, command=self.openlibrarywindow, font=('tahoma', 10, 'bold'),text='Library Management', bg='#1a8488', fg='white', padx=10, pady=10)
        self.buttonLibrary.pack()



    def openlibrarywindow(self):

        self.master = Toplevel()
        self.master.title('Library Management')
        self.master.geometry("1200x600+50+50")
        
        ##############################     LEFT FRAME   ##############################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)

        ###################   LABELS   #####################
        self.RegistrationN=Label(self.frameleft,text='Student\'s Registration N°:',fg='#4F4F4F',font=('tahoma',9))
        self.RegistrationN.place(x=15,y=20,width=120,height=40)
        
        self.PhoneNumber = Label(self.frameleft, text='Phone Number:', fg='#4F4F4F', font=('tahoma', 9))
        self.PhoneNumber.place(x=10, y=70, width=120, height=40)
        
        self.BookID = Label(self.frameleft, text='Book Name:', fg='#4F4F4F', font=('tahoma', 9))
        self.BookID.place(x=10, y=120, width=120, height=40)

        self.BookName = Label(self.frameleft, text='Book ID:', fg='#4F4F4F', font=('tahoma', 9))
        self.BookName.place(x=10, y=170, width=120, height=40)
        
        self.DeliveryDate = Label(self.frameleft, text='Delivery Date:', fg='#4F4F4F', font=('tahoma', 9))
        self.DeliveryDate.place(x=15, y=250, width=120, height=40)
        
        self.ReturnDate = Label(self.frameleft, text='Return Date:', fg='#4F4F4F', font=('tahoma', 9))
        self.ReturnDate.place(x=15, y=300, width=120, height=40)
        
        self.registrationN=StringVar()
        self.phonenumber = StringVar()
        self.bookid = StringVar()
        self.bookname = StringVar()
        self.deliverydate=StringVar()
        self.returndate = StringVar()

        ###################   ENTRIES   #####################
        self.RegistrationNEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',9),textvariable=self.registrationN)
        self.RegistrationNEntry.place(x=170,y=20,width=200,height=40)
        
        self.PhoneNumberEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.phonenumber)
        self.PhoneNumberEntry.place(x=170, y=70, width=200, height=40)
        
        self.BookNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.bookname)
        self.BookNameEntry.place(x=170, y=120, width=200, height=40)

        self.BookIDEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.bookid)
        self.BookIDEntry.place(x=170, y=170, width=200, height=40)
        
        self.DeliveryDateEntry=DateEntry(self.frameleft ,textvariable=self.deliverydate, date_pattern="yyyy-mm-dd",mindate=datetime.date.today())
        self.DeliveryDateEntry.place(x=170, y=250,width=200,height=40)
        
        self.ReturnDateEntry = DateEntry(self.frameleft ,textvariable=self.returndate, date_pattern="yyyy-mm-dd")
        self.ReturnDateEntry.place(x=170, y=300, width=200, height=40)


        ###################   BUTTONS   #####################
        self.buttonAdd=Button(self.frameleft,command=self.add, text="ADD", font=('tahoma',10))
        self.buttonAdd.place(x=20,y=450,width=60,height=60)
        
        self.buttonUpdate = Button(self.frameleft,command=self.update, text="UPDATE",font=('tahoma',10))
        self.buttonUpdate.place(x=100, y=450,width=60,height=60)
        
        self.buttonDelete = Button(self.frameleft,command=self.delete, text="DELETE",font=('tahoma',10))
        self.buttonDelete.place(x=180, y=450,width=60,height=60)
        
        self.buttonRead = Button(self.frameleft,command=self.read,  text="SHOW", font=('tahoma', 10))
        self.buttonRead.place(x=260, y=450, width=60, height=60)
        
        self.buttonReset = Button(self.frameleft,command=self.reset, text="RESET", font=('tahoma', 10))
        self.buttonReset.place(x=340, y=450, width=60, height=60)






        ##############################     RIGHT FRAME   ##############################
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)


        ##################### TOP RIGHT FRAME ###################

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5)

        self.searchbook=StringVar()


        self.SeachBook = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=110,textvariable=self.searchbook)
        self.SeachBook.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.ButtonSearch = Button(self.framerighttop,command=self.search, text='Search', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=50)
        self.ButtonSearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ##################### FRAME TREE VIEW ###################

        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","RegistartionN","PhoneNumber","BookName","BookID","DeliveryDate","ReturnDate"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("RegistartionN",text="Registraion N°")
        self.table.heading("PhoneNumber", text="Phone Number")
        self.table.heading("BookName", text="Book Name")
        self.table.heading("BookID", text="Book ID")
        self.table.heading("DeliveryDate", text="Delivery Date")
        self.table.heading("ReturnDate", text="Return Date")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("RegistartionN", anchor=W,width=120)
        self.table.column("PhoneNumber",anchor=W,width=120)
        self.table.column("BookName", anchor=W,width=120)
        self.table.column("BookID",anchor=W,width=120)
        self.table.column("DeliveryDate",anchor=W,width=120)
        self.table.column("ReturnDate",anchor=W,width=120)
        self.read()
        self.table.bind("<ButtonRelease>",self.show)


    
    #################   BUTTON FONCTIONS #######################

    ###### ADD FONTION ######
    def add(self):
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into library(registrationnumber,phonenumber,bookname,bookid,deliverydate,returndate) values (%s,%s,%s,%s,%s,%s)"
        if (len(self.registrationN.get())==0 or len(self.phonenumber.get())==0 or len(self.bookname.get())==0 or len(self.bookid.get())==0 or len(self.deliverydate.get())==0 or  len(self.returndate.get())==0 ) :
            mb.showerror('Error', 'all data should be required',parent=self.master)
        else:
            val=(self.registrationN.get(),self.phonenumber.get(),self.bookname.get(),self.bookid.get(),self.deliverydate.get(),self.returndate.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.reset()
            self.read()


    ###### READ FONTION ######
    def read(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from library"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[0],values=res)
            mydb.commit()
        mydb.close()

    ###### SHOW FONTION ######
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.registrationN.set(val[1])
        self.phonenumber.set(val[2])
        self.bookname.set(val[3])
        self.bookid.set(val[3])
        self.deliverydate.set(val[5])
        self.returndate.set(val[6])

    ###### RESET FONTION ######
    def reset(self):
        self.RegistrationNEntry.delete(0, 'end')
        self.PhoneNumberEntry.delete(0, 'end')
        self.BookNameEntry.delete(0, 'end')
        self.BookIDEntry.delete(0, 'end')
        self.DeliveryDateEntry.selection_clear()
        self.ReturnDateEntry.selection_clear()

    ###### DELETE FONTION ######
    def delete(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from library where id="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this DATA is deleted',parent=self.master)
        self.read()
        self.reset()

    ###### UPDATE FONTION ######
    def update(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update library set registrationnumber=%s,phonenumber=%s,bookname=%s,bookid=%s,deliverydate=%s,returndate=%s where id=%s")
        val=(self.registrationN.get(),self.phonenumber.get(),self.bookname.get(),self.bookid.get(),self.deliverydate.get(),self.returndate.get(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update','this DATA is updated',parent=self.master)
        self.read()
        self.reset()


    ###### SEARCH FONTION ######
    def search(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from library where id="+self.searchbook.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        #print(myresults)
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()
