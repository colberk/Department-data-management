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
        self.master.iconbitmap('mortarboard.ico')
        self.master.resizable(False, False)


        ############################   TOP FRAME   ############################
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='lIBRARY MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()
        
        ##############################     LEFT FRAME   ##############################
        self.frameleft = Frame(self.master, width=400,bg='#d9d9d8')
        self.frameleft.pack(side=LEFT, fill=BOTH)

        ###################   LABELS   #####################
        self.Title=Label(self.frameleft,text='DATA MANUPILATION SECTION',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',12,'bold'))
        self.Title.place(x=50,y=10,width=310,height=40)

        self.RegistrationN=Label(self.frameleft,text='Registration N°:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.RegistrationN.place(x=15,y=50,width=120,height=40)
        
        self.PhoneNumber = Label(self.frameleft, text='Phone Number:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.PhoneNumber.place(x=10, y=100, width=120, height=40)
        
        self.BookID = Label(self.frameleft, text='Book Name:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.BookID.place(x=10, y=150, width=120, height=40)

        self.BookName = Label(self.frameleft, text='Book ID:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.BookName.place(x=10, y=200, width=120, height=40)
        
        self.DeliveryDate = Label(self.frameleft, text='Delivery Date:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.DeliveryDate.place(x=15, y=280, width=120, height=40)
        
        self.ReturnDate = Label(self.frameleft, text='Return Date:', fg='#4F4F4F', bg='#d9d9d8',font=('tahoma', 9))
        self.ReturnDate.place(x=15, y=330, width=120, height=40)
        
        self.registrationN=StringVar()
        self.phonenumber = StringVar()
        self.bookid = StringVar()
        self.bookname = StringVar()
        self.deliverydate=StringVar()
        self.returndate = StringVar()

        ###################   ENTRIES   #####################
        self.RegistrationNEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',9),textvariable=self.registrationN)
        self.RegistrationNEntry.place(x=170,y=50,width=200,height=40)
        
        self.PhoneNumberEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.phonenumber)
        self.PhoneNumberEntry.place(x=170, y=100, width=200, height=40)
        
        self.BookNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.bookname)
        self.BookNameEntry.place(x=170, y=150, width=200, height=40)

        self.BookIDEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.bookid)
        self.BookIDEntry.place(x=170, y=200, width=200, height=40)
        
        self.DeliveryDateEntry=DateEntry(self.frameleft ,textvariable=self.deliverydate, date_pattern="yyyy-mm-dd",mindate=datetime.date.today())
        self.DeliveryDateEntry.place(x=170, y=280,width=200,height=40)
        
        self.ReturnDateEntry = DateEntry(self.frameleft ,textvariable=self.returndate, date_pattern="yyyy-mm-dd")
        self.ReturnDateEntry.place(x=170, y=330, width=200, height=40)


        ###################   BUTTONS   #####################
        self.buttonAdd=Button(self.frameleft,text="ADD",command=self.add,font=('tahoma',10))
        self.buttonAdd.place(x=10,y=430,width=60,height=40)
        
        self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.update,font=('tahoma',10))
        self.buttonUpdate.place(x=90, y=430,width=60,height=40)
        
        self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.delete,font=('tahoma',10))
        self.buttonDelete.place(x=170, y=430,width=60,height=40)
        
        self.buttonRead = Button(self.frameleft,  text="SHOW",command=self.read, font=('tahoma', 10))
        self.buttonRead.place(x=250, y=430, width=60, height=40)
        
        self.buttonReset = Button(self.frameleft, text="RESET",command=self.reset, font=('tahoma', 10))
        self.buttonReset.place(x=330, y=430, width=60, height=40)






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


        #################   BUTTOM RIGHT FRAME   #######################
        self.framerightbuttom=Frame(self.frameright,height=200,pady=5,padx=5)
        self.framerightbuttom.pack(fill=X)

        #################   LABELS #######################
        self.DeliverySelect = Label(self.framerightbuttom,text="Delivery date:",fg='#4F4F4F',font=('tahoma',9))
        self.DeliverySelect.place(x=150, y=20, width=100, height=40)

        self.ReturnSelect = Label(self.framerightbuttom,text="return date:",fg='#4F4F4F',font=('tahoma',9))
        self.ReturnSelect.place(x=250, y=20, width=100, height=40)

        


        self.deliveryselect=StringVar()
        self.returnselect=StringVar()
        


        #################   ENTRIES #######################
        self.DeliverySelect = DateEntry(self.framerightbuttom ,textvariable=self.deliveryselect, date_pattern="yyyy-mm-dd")
        self.DeliverySelect.place(x=150, y=80, width=100, height=40)

        self.ReturnSelect = DateEntry(self.framerightbuttom,textvariable=self.returnselect, date_pattern="yyyy-mm-dd")
        self.ReturnSelect.place(x=250, y=80, width=100, height=40)

        self.buttonselect = Button(self.framerightbuttom,command=self.filter, text='Filter', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=20)
        self.buttonselect.place(x=450,y=80,width=200,height=40)

        self.reset()


    
    #################   BUTTON FONCTIONS #######################

    ###### ADD FONTION ######
    def add(self):
        try:
            mydb=mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor=mydb.cursor()
            sql="insert into library(registrationnumber,phonenumber,bookname,bookid,deliverydate,returndate) values (%s,%s,%s,%s,%s,%s)"
            if (len(self.registrationN.get())==0 or len(self.phonenumber.get())==0 or len(self.bookname.get())==0 or len(self.bookid.get())==0 or len(self.deliverydate.get())==0 or  len(self.returndate.get())==0 ) :
                mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent=self.master)
            else:
                val=(self.registrationN.get(),self.phonenumber.get(),self.bookname.get(),self.bookid.get(),self.deliverydate.get(),self.returndate.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mydb.close()
                mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
                self.reset()
                self.read()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


        


    ###### READ FONTION ######
    def read(self):
        try:
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
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()

    ###### SHOW FONTION ######
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.registrationN.set(val[1])
        self.phonenumber.set(val[2])
        self.bookname.set(val[3])
        self.bookid.set(val[4])
        self.deliverydate.set(val[5])
        self.returndate.set(val[6])

    ###### RESET FONTION ######
    def reset(self):
        self.RegistrationNEntry.delete(0, 'end')
        self.PhoneNumberEntry.delete(0, 'end')
        self.BookNameEntry.delete(0, 'end')
        self.BookIDEntry.delete(0, 'end')
        self.DeliveryDateEntry.delete(0,END)
        self.ReturnDateEntry.delete(0,END)
        self.ReturnSelect.delete(0,END)
        self.DeliverySelect.delete(0,END)
        self.SeachBook.delete(0,'end')

    ###### DELETE FONTION ######
    def delete(self):
        try:
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
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()

    ###### UPDATE FONTION ######
    def update(self):
        try:
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
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


    ###### SEARCH FONTION ######
    def search(self):
        try:
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
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()

    ### FILTER FONTION ###
    def filter(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        if (len(self.deliveryselect.get())==0 and len(self.returnselect.get())==0 ) :
            mb.showerror('Error', 'Data missing, please, make sure to fill the delivery date job or the return date to filter',parent=self.master)
        
        elif(len(self.deliveryselect.get())==0):
            sql = ("select * from library where returndate='"+self.returnselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[0],values=res)
                mydb.commit()
            mydb.close()
        elif(len(self.returnselect.get())==0):
            sql = ("select * from library where deliverydate='"+self.deliveryselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[0],values=res)
                mydb.commit()
            mydb.close()

        else:
            sql = ("select * from library where deliverydate='"+self.deliveryselect.get()+"' AND returndate='"+self.returnselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[0],values=res)
                mydb.commit()
            mydb.close()