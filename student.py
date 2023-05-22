from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc

class student:
    def __init__(self,cf):
        self.centerFrame=cf
        self.studentframe=Frame(self.centerFrame,padx=10,pady=10)
        self.studentframe.grid(row=0,column=1,sticky='senw',ipady=5)
        self.img2=Image.open('C:\memoire\studenicon1.png')
        self.img2.thumbnail((200,200))
        self.new_img2=ImageTk.PhotoImage(self.img2)
        self.imgstudent=Label(self.studentframe,image=self.new_img2,padx=10,pady=10)
        self.imgstudent.pack()
        self.buttomstdn=Button(self.studentframe,command=self.openstudentwindow,font=('Helvetica',10,'bold'),text='Student Management',bg='#1a8488',fg='white',padx=10,pady=10)
        
        self.buttomstdn.pack()

    def openstudentwindow(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.geometry("1200x650+50+50")
        self.master.iconbitmap('mortarboard.ico')

        #######   TOP FRAME   #######
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='STUDENT DATA MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()
        


        #######   LEFT FRAME   #######
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #################   LABELS #######################
        self.FirstName=Label(self.frameleft,text='First name:',fg='#4F4F4F',font=('tahoma',9))
        self.FirstName.place(x=10,y=30,width=100,height=40)
        
        self.LastName = Label(self.frameleft, text='Last Name:',fg='#4F4F4F',font=('tahoma',9))
        self.LastName.place(x=10,y=80,width=100,height=40)
        
        self.RegistrationN = Label(self.frameleft, text='Regestration N°:',fg='#4F4F4F',font=('tahoma',9))
        self.RegistrationN.place(x=10,y=130,width=100,height=40)
        
        self.Email = Label(self.frameleft, text='Email:',fg='#4F4F4F',font=('tahoma',9))
        self.Email.place(x=10,y=180,width=100,height=40)
        
        self.PhoneNum = Label(self.frameleft,text='Phone Number:',fg='#4F4F4F',font=('tahoma',9))
        self.PhoneNum.place(x=10,y=230,width=100,height=40)
        
        self.Level = Label(self.frameleft,text='Level:',fg='#4F4F4F',font=('tahoma',9))
        self.Level.place(x=10,y=300,width=100,height=40)

        self.Speciality = Label(self.frameleft,text='Speciality:',fg='#4F4F4F',font=('tahoma',9))
        self.Speciality.place(x=10,y=350,width=100,height=40)
        
        self.Group = Label(self.frameleft,text='Group:',fg='#4F4F4F',font=('tahoma',9))
        self.Group.place(x=10,y=400,width=100,height=40)
        
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.registration = StringVar()
        self.phoneNum = StringVar()
        self.level = StringVar()
        self.speciality = StringVar()
        self.group = StringVar()



        #################   ENTRIES #######################

        self.FirstNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.firstname)
        self.FirstNameEntry.place(x=120,y=30,width=200,height=40)
        
        self.LastNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.lastname)
        self.LastNameEntry.place(x=120,y=80,width=200,height=40)
        
        self.RNentry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.registration)
        self.RNentry.place(x=120,y=130,width=200,height=40)
        
        self.EmailEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.email)
        self.EmailEntry.place(x=120,y=180,width=200,height=40)
        
        self.PhoneNumEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.phoneNum)
        self.PhoneNumEntry.place(x=120,y=230,width=200,height=40)

        self.LevelEntry = ttk.Combobox(self.frameleft, values=["L1","L2","L3","M1","M2","Phd"],state='readonly',textvariable=self.level)
        self.LevelEntry.place(x=120, y=300, width=200, height=40)

        self.SpecialityEntry = ttk.Combobox(self.frameleft, values=["S1","S2","S3"],state='readonly',textvariable=self.speciality)
        self.SpecialityEntry.place(x=120, y=350, width=200, height=40)

        self.GroupEntry = ttk.Combobox(self.frameleft,values=["1","2","3"],state='readonly',textvariable=self.group)
        self.GroupEntry.place(x=120,y=400,width=200,height=40)



        #################   BUTTONS #######################

        self.buttonAdd=Button(self.frameleft,text="ADD",command=self.add,font=('tahoma',10))
        self.buttonAdd.place(x=20,y=500,width=60,height=60)
        
        self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.update,font=('tahoma',10))
        self.buttonUpdate.place(x=100, y=500,width=60,height=60)
        
        self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.delete,font=('tahoma',10))
        self.buttonDelete.place(x=180, y=500,width=60,height=60)
        
        self.buttonRead = Button(self.frameleft,  text="SHOW",command=self.read, font=('tahoma', 10))
        self.buttonRead.place(x=260, y=500, width=60, height=60)
        
        self.buttonReset = Button(self.frameleft, text="RESET",command=self.reset, font=('tahoma', 10))
        self.buttonReset.place(x=340, y=500, width=60, height=60)


        #################   RIGHT FRAME #######################
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5)


        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=10)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        
        self.buttonsearch = Button(self.framerighttop, text='Search', fg='#4F4F4F',command=self.search, font=('tahoma', 12, 'bold'),width=20)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)
        
        self.buttonselect = Entry(self.framerighttop,fg='#4F4F4F',font=('tahoma', 12, 'bold'),width=10)
        self.buttonselect.grid(row=0, column=2, sticky='snew',  pady=10, padx=10)
        
        self.buttonselect = Button(self.framerighttop, text='Select', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=20)
        self.buttonselect.grid(row=0, column=3, sticky='nsew', pady=10, padx=10)


        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)
        


        self.framerighttop.pack(fill=X)

        
        #################  TREE FRAME VIEW  #######################
        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("Firstname","Lastname","Regestration N°","Email","Phone Number","Level","Speciality","Group"),show='headings',height=15,yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

    
        self.table.heading("Firstname", text="First Name")
        self.table.heading("Lastname", text="Last Name")
        self.table.heading("Regestration N°", text="Regestration N°")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone Number", text="Phone Number")
        self.table.heading("Level", text="Level")
        self.table.heading("Speciality", text="Speciality")
        self.table.heading("Group", text="Group")

        self.table.column("Firstname", anchor=W,width= 70)
        self.table.column("Lastname",anchor=W,width= 70)
        self.table.column("Regestration N°",anchor=W,width= 120)
        self.table.column("Email",anchor=W, width= 200)
        self.table.column("Phone Number",anchor=W,width= 120)
        self.table.column("Level",anchor=W,width=50)
        self.table.column("Speciality",anchor=W,width=70)
        self.table.column("Group",anchor=W,width=50)
        self.read()
        self.table.bind("<ButtonRelease>",self.show)
    
    
    
    #################   BUTTON FONCtIONS #######################

    ### ADD FONTION ###

    def add(self):
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into student(firstname,lastname,registrationnumber,email,phonenumber,level,speciality,groupe) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        if (len(self.firstname.get())==0 
            or len(self.lastname.get())==0 
            or len(self.registration.get())==0 
            or len(self.email.get())==0 
            or len(self.phoneNum.get())==0 
            or len(self.level.get())==0 
            or len(self.speciality.get())==0 
            or len(self.group.get())==0 ) :
            mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent=self.master)

        else:
            val=(self.firstname.get(),self.lastname.get(),self.registration.get(),self.email.get(),self.phoneNum.get(),self.level.get(),self.speciality.get(),self.group.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            self.read()
            self.reset()
        
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            



    ### READ FONTION ###
    def read(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from student"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[2],values=res)
            mydb.commit()
        mydb.close()


    ### SHOW FONTION ###
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.firstname.set(val[0])
        self.lastname.set(val[1])
        self.registration.set(val[2])
        self.email.set(val[3])
        self.phoneNum.set(val[4])
        self.level.set(val[5])
        self.speciality.set(val[6])
        self.group.set(val[7])


    ### RESET FONTION ###
    def reset(self):
        self.FirstNameEntry.delete(0,'end')
        self.LastNameEntry.delete(0,'end')
        self.RNentry.delete(0,'end')
        self.EmailEntry.delete(0,'end')
        self.PhoneNumEntry.delete(0,'end')
        self.LevelEntry.set("")
        self.SpecialityEntry.set("")
        self.GroupEntry.set("")

        

    



    ### DELETE FONTION ###
    def delete(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from student where registrationnumber="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this student deleted',parent=self.master)
        self.read()
        self.reset()


    ### UPDATE FONTION ###
    def update(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update student set firstname=%s,lastname=%s, registrationnumber=%s, email=%s, phonenumber=%s, level=%s, speciality=%s, groupe=%s where registrationnumber=%s")
        val=(self.firstname.get(),self.lastname.get(),self.registration.get(),self.email.get(),self.phoneNum.get(),self.level.get(),self.speciality.get(),self.group.get(),self.iid)
        print(self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        self.read()
        self.reset()
        mb.showinfo('update','this student\'s data is updated',parent=self.master)


    ### SEARCH FONTION ###
    def search(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from student where registrationnumber="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        #print(myresults)
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()
    
    
    