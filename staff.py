from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc
import pyperclip


class staff:
    def __init__(self,cf):
        self.centerFrame=cf
        self.staffFrame=Frame(self.centerFrame,padx=10,pady=10)
        
        self.staffFrame.grid(row=0,column=2,sticky='senw',ipady=5)
        self.img3=Image.open('C:\memoire\staff.png')
        self.img3.thumbnail((200,200))
        self.new_img3=ImageTk.PhotoImage(self.img3)
        self.imgstaff=Label(self.staffFrame,image=self.new_img3,padx=10,pady=10)
        self.imgstaff.pack()
        
        self.buttomstf=Button(self.staffFrame,command=self.openStaffWindow,font=('tahoma',10,'bold'),text='Staff Management',bg='#1a8488',fg='white',padx=10,pady=10)
        self.buttomstf.pack()

    def openStaffWindow(self):
        self.master = Toplevel()
        self.master.title('Staff Management')
        self.master.geometry("1200x600+50+50")
        self.master.iconbitmap('mortarboard.ico')
        self.master.resizable(False, False)


        ############################   TOP FRAME   ############################
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='STAFF DATA MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()

        #############################   LEFT FRAME   #############################
        self.frameleft = Frame(self.master, width=400,bg='#d9d9d8')
        self.frameleft.pack(side=LEFT, fill=BOTH)

        ###################    LABELS   #######################
        self.Title=Label(self.frameleft,text='DATA MANUPILATION SECTION',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',12,'bold'))
        self.Title.place(x=50,y=10,width=310,height=40)

        self.FirstName=Label(self.frameleft,text='Firstname:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.FirstName.place(x=10,y=50,width=100,height=40)
        
        self.LastName = Label(self.frameleft, text='Lastname:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.LastName.place(x=10,y=100,width=100,height=40)
        
        self.IDN = Label(self.frameleft, text='IDCard N°:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.IDN.place(x=10,y=150,width=100,height=40)
        
        self.Email = Label(self.frameleft, text='Email:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.Email.place(x=10,y=200,width=100,height=40)
        
        self.PhoneNumber = Label(self.frameleft, text='Phone:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9 ))
        self.PhoneNumber.place(x=10, y=250, width=100, height=40)
        
        self.MainJob= Label(self.frameleft, text='Main Job:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9 ))
        self.MainJob.place(x=10, y=300, width=100, height=40)
        
        self.SecJob= Label(self.frameleft, text='Secondary Job:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9 ))
        self.SecJob.place(x=10, y=350, width=100, height=40)

        self.firstname=StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.idn = StringVar()
        self.phonenumber=StringVar()
        self.mainjob=StringVar()
        self.secjob = StringVar()
        self.searchstaff= StringVar()

        ###################    ENTRIES   #######################
        self.FirstNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.firstname)
        self.FirstNameEntry.place(x=120,y=50,width=200,height=40)
        
        self.LastNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.lastname)
        self.LastNameEntry.place(x=120,y=100,width=200,height=40)
        
        self.IDNentry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.idn)
        self.IDNentry.place(x=120,y=150,width=200,height=40)
        
        self.EmailEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.email)
        self.EmailEntry.place(x=120,y=200,width=200,height=40)
        
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12,), textvariable=self.phonenumber)
        self.PhoneEntry.place(x=120, y=250, width=200, height=40)
        
        self.MainJobEntry = ttk.Combobox(self.frameleft, values=["Professor","Professor-grade1","Professor-grade2","Employee"],state='readonly',textvariable=self.mainjob)
        self.MainJobEntry.place(x=120, y=300, width=200, height=40)
        
        self.SecJobEntry = ttk.Combobox(self.frameleft, values=["None","Job1","Job2","Job3"],state='readonly',textvariable=self.secjob)
        self.SecJobEntry.place(x=120, y=350, width=200, height=40)

         

        ###################    BUTTONS   #######################

        self.buttonAdd=Button(self.frameleft,text="ADD",command=self.add,font=('tahoma',10))
        self.buttonAdd.place(x=10,y=450,width=60,height=40)
        
        self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.update,font=('tahoma',10))
        self.buttonUpdate.place(x=90, y=450,width=60,height=40)
        
        self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.delete,font=('tahoma',10))
        self.buttonDelete.place(x=170, y=450,width=60,height=40)
        
        self.buttonRead = Button(self.frameleft,  text="SHOW",command=self.read, font=('tahoma', 10))
        self.buttonRead.place(x=250, y=450, width=60, height=40)
        
        self.buttonReset = Button(self.frameleft, text="RESET",command=self.reset, font=('tahoma', 10))
        self.buttonReset.place(x=330, y=450, width=60, height=40)






        #############################   RIGHT FRAME   #############################


        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)
        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5)

        ###################    TOP RIGHT FRAME   #######################
        self.searchstaffentry = Entry(self.framerighttop , fg='#4F4F4F' , font=('tahoma', 12, 'bold'),width=110,textvariable=self.searchstaff)
        self.searchstaffentry.grid(row=0, column=0 , sticky='nsew' , pady=10, padx=10)
        
        self.buttonsearch = Button(self.framerighttop,command=self.search, text='Search', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        

        self.framerighttop.pack(fill=X)

        ###################    FRAME TREE VIEW   #######################

        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","Firstname","Lastname","IDCardN","Email","PhoneNumber","MainJob","SecJob"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("Firstname", text="Firstname")
        self.table.heading("Lastname", text="Lastname")
        self.table.heading("IDCardN", text="IDCard N°")
        self.table.heading("Email", text="Email")
        self.table.heading("PhoneNumber", text="Phone Number")
        self.table.heading("MainJob", text="Main Job")
        self.table.heading("SecJob", text="Secondary Job")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("Firstname", anchor=W,width=80)
        self.table.column("Lastname",anchor=W,width=80)
        self.table.column("IDCardN",anchor=W,width=100)
        self.table.column("Email",anchor=W,width=160)
        self.table.column("PhoneNumber", anchor=W, width=80)
        self.table.column("MainJob", anchor=W,width=120)
        self.table.column("SecJob", anchor=W,width=120)
        self.read()
        self.table.bind("<ButtonRelease>",self.show)


        #################   BUTTOM RIGHT FRAME   #######################
        self.framerightbuttom=Frame(self.frameright,height=500,pady=5,padx=5)
        self.framerightbuttom.pack(fill=X)

        #################   LABELS #######################
        self.MainJobSelect = Label(self.framerightbuttom,text="Main Job:",fg='#4F4F4F',font=('tahoma',9))
        self.MainJobSelect.place(x=150, y=20, width=100, height=40)

        self.SecJobSelect = Label(self.framerightbuttom,text="Secondary job:",fg='#4F4F4F',font=('tahoma',9))
        self.SecJobSelect.place(x=250, y=20, width=100, height=40)

        self.CopySelect = Label(self.framerightbuttom, text="COPY:" , fg='#4F4F4F',font=('tahoma',9))
        self.CopySelect.place(x=200 , y=200 , width=100, height=40 )

        


        self.mainjobselect=StringVar()
        self.secjobselect=StringVar()
        


        #################   ENTRIES #######################
        self.MainJobEntrySelect = ttk.Combobox(self.framerightbuttom, values=["Professor","Professor-grade1","Professor-grade2","Employee"],state='readonly',textvariable=self.mainjobselect)
        self.MainJobEntrySelect.place(x=150, y=80, width=100, height=40)

        self.SecJobEntrySelect = ttk.Combobox(self.framerightbuttom,  values=["None","Job1","Job2","Job3"],state='readonly',textvariable=self.secjobselect)
        self.SecJobEntrySelect.place(x=250, y=80, width=100, height=40)

        self.buttonselect = Button(self.framerightbuttom,command=self.filter, text='Filter', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=20)
        self.buttonselect.place(x=450,y=80,width=200,height=40)

        self.CopyEmailsSelect =Button(self.framerightbuttom , command=self.copyEmails , text="Emails" ,fg='#4F4F4F', font=('tahoma', 9),width=20 )
        self.CopyEmailsSelect.place(x=300 , y=200 , width=100, height=30 )

        self.CopyNumbersSelect =Button(self.framerightbuttom , command=self.copyNumbers , text="Phone Numbers" ,fg='#4F4F4F', font=('tahoma', 9),width=20 )
        self.CopyNumbersSelect.place(x=400 , y=200 , width=100, height=30 )

    
    
    ############# BUTTONS FONCTIONS #################

    #### ADD FONCTION  ####
    def add(self):
        try:
            mydb=mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor=mydb.cursor()
            sql="insert into staff(firstname,lastname,IDcardnumber,email,phonenumber,job,secondaryjob) values (%s,%s,%s,%s,%s,%s,%s)"
            if (len(self.firstname.get())==0 or len(self.lastname.get())==0 or len(self.idn.get())==0  or len(self.email.get())==0 or len(self.phonenumber.get())==0 or len(self.mainjob.get())==0 or len(self.secjob.get())==0) :
                mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent=self.master)
            else:
                val=(self.firstname.get(),self.lastname.get(),self.idn.get(),self.email.get(),self.phonenumber.get(),self.mainjob.get(),self.secjob.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mydb.close()
                mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
                self.read()
                self.reset()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()  
            

    #### READ FONCTION  ####

    def read(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor=mydb.cursor()
            sql="select * from staff"
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

    #### SHOW FONCTION  ####
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.firstname.set(val[1])
        self.lastname.set(val[2])
        self.idn.set(val[3])
        self.email.set(val[4])
        self.phonenumber.set(val[5])
        self.mainjob.set(val[6])
        self.secjob.set(val[7])

    #### RESET FONCTION  ####
    def reset(self):
        self.FirstNameEntry.delete(0,'end')
        self.LastNameEntry.delete(0,'end')
        self.IDNentry.delete(0,'end')
        self.EmailEntry.delete(0,'end')
        self.PhoneEntry.delete(0,'end')
        self.MainJobEntry.set("")
        self.SecJobEntry.set("")
        self.searchstaffentry.delete(0,'end')


    #### DELETE FONCTION  ####
    def delete(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = ("delete from staff where id="+self.iid)
            mycursor.execute(sql)
            mydb.commit()
            mb.showinfo('Delete','this membre is deleted',parent=self.master)
            self.read()
            self.reset()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


    #### UPDATE FONCTION  ####
    def update(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = ("update staff set firstname=%s, lastname=%s, IDcardnumber=%s, email=%s, phonenumber=%s, job=%s, secondaryjob=%s where id=%s")
            val=(self.firstname.get(),self.lastname.get(),self.idn.get(),self.email.get(),self.phonenumber.get(),self.mainjob.get(),self.secjob.get(),self.iid)
            mycursor.execute(sql,val)
            mydb.commit()
            self.read()
            self.reset()
            mb.showinfo('update','this membre is updated',parent=self.master)
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()
        

    #### SEARCH FONCTION  ####
    def search(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            print(self.searchstaff.get())
            sql = ("select * from staff where id="+self.searchstaff.get())
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
        if (len(self.mainjobselect.get())==0 and len(self.secjobselect.get())==0 ) :
            mb.showerror('Error', 'Data missing, please, make sure to fill the main job or the secondary job to filter',parent=self.master)
        
        elif(len(self.mainjobselect.get())==0):
            sql = ("select * from staff where secondaryjob='"+self.secjobselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[0],values=res)
                mydb.commit()
            mydb.close()
        elif(len(self.secjobselect.get())==0):
            sql = ("select * from staff where job='"+self.mainjobselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[0],values=res)
                mydb.commit()
            mydb.close()

        else:
            sql = ("select * from staff where job='"+self.mainjobselect.get()+"' AND secondaryjob='"+self.secjobselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[0],values=res)
                mydb.commit()
            mydb.close()

    def copyEmails(self):
        # Get selected column index
        column_index = 4

        # Get the values of the selected column
        column_values = [self.table.set(item, column_index) for item in self.table.get_children()]

        # Concatenate column values into a single string
        column_string = "\n".join(column_values)

        # Copy column values to clipboard
        pyperclip.copy(column_string)
        
        mb.showinfo('Successfully copied', 'Emails copied to clipboard',parent=self.master)


    def copyNumbers(self):
        # Get selected column index
        column_index = 5

        # Get the values of the selected column
        column_values = [self.table.set(item, column_index) for item in self.table.get_children()]

        # Concatenate column values into a single string
        column_string = "\n".join(column_values)

        # Copy column values to clipboard
        pyperclip.copy(column_string)
        
        mb.showinfo('Successfully copied', 'Phone Numbers copied to clipboard',parent=self.master)
