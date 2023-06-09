from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc
import pyperclip

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
        self.master.resizable(False, False)

        #######   TOP FRAME   #######
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='STUDENT DATA MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()
        


        #######   LEFT FRAME   #######
        self.frameleft = Frame(self.master, width=400,bg='#d9d9d8')
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #################   LABELS #######################
        self.Title=Label(self.frameleft,text='DATA MANUPILATION SECTION',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',12,'bold'))
        self.Title.place(x=50,y=10,width=310,height=40)

        self.FirstName=Label(self.frameleft,text='First name:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.FirstName.place(x=10,y=50,width=100,height=40)
        
        self.LastName = Label(self.frameleft, text='Last Name:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.LastName.place(x=10,y=100,width=100,height=40)
        
        self.RegistrationN = Label(self.frameleft, text='Regestration N°:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.RegistrationN.place(x=10,y=150,width=100,height=40)
        
        self.Email = Label(self.frameleft, text='Email:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.Email.place(x=10,y=200,width=100,height=40)
        
        self.PhoneNum = Label(self.frameleft,text='Phone Number:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.PhoneNum.place(x=10,y=250,width=100,height=40)
        
        self.Level = Label(self.frameleft,text='Level:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.Level.place(x=10,y=320,width=100,height=40)

        self.Speciality = Label(self.frameleft,text='Speciality:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.Speciality.place(x=10,y=370,width=100,height=40)
        
        self.Group = Label(self.frameleft,text='Group:',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',9))
        self.Group.place(x=10,y=420,width=100,height=40)
        
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.registration = StringVar()
        self.phoneNum = StringVar()
        self.level = StringVar()
        self.speciality = StringVar()
        self.group = StringVar()

        mydb=mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
        )
        mycursor=mydb.cursor()
        sql="SELECT specialityname FROM speciality"
        mycursor.execute(sql)
        specialityvalues=mycursor.fetchall()
        specialityvalues=list(set(specialityvalues))
        specialityvalues = [str(element).replace("(", "").replace(")", "").replace("'", "").replace(",", "") for element in specialityvalues]






        #################   ENTRIES #######################

        self.FirstNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.firstname)
        self.FirstNameEntry.place(x=120,y=50,width=200,height=40)
        
        self.LastNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.lastname)
        self.LastNameEntry.place(x=120,y=100,width=200,height=40)
        
        self.RNentry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.registration)
        self.RNentry.place(x=120,y=150,width=200,height=40)
        
        self.EmailEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.email)
        self.EmailEntry.place(x=120,y=200,width=200,height=40)
        
        self.PhoneNumEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.phoneNum)
        self.PhoneNumEntry.place(x=120,y=250,width=200,height=40)

        self.LevelEntry = ttk.Combobox(self.frameleft, values=["L1","L2","L3","M1","M2","Phd"],state='readonly',textvariable=self.level)
        self.LevelEntry.place(x=120, y=320, width=200, height=40)

        self.SpecialityEntry = ttk.Combobox(self.frameleft, values=specialityvalues,state='readonly',textvariable=self.speciality)
        self.SpecialityEntry.place(x=120, y=370, width=200, height=40)

        self.GroupEntry = ttk.Combobox(self.frameleft,values=["1","2","3"],state='readonly',textvariable=self.group)
        self.GroupEntry.place(x=120,y=420,width=200,height=40)


        mydb.commit()
        mydb.close()



        #################   BUTTONS #######################

        self.buttonAdd=Button(self.frameleft,text="ADD",command=self.add,font=('tahoma',10))
        self.buttonAdd.place(x=10,y=500,width=60,height=40)
        
        self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.update,font=('tahoma',10))
        self.buttonUpdate.place(x=90, y=500,width=60,height=40)
        
        self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.delete,font=('tahoma',10))
        self.buttonDelete.place(x=170, y=500,width=60,height=40)
        
        self.buttonRead = Button(self.frameleft,  text="SHOW",command=self.read, font=('tahoma', 10))
        self.buttonRead.place(x=250, y=500, width=60, height=40)
        
        self.buttonReset = Button(self.frameleft, text="RESET",command=self.reset, font=('tahoma', 10))
        self.buttonReset.place(x=330, y=500, width=60, height=40)


        #################   RIGHT FRAME #######################
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5)


        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        
        self.buttonsearch = Button(self.framerighttop, text='Search', fg='#4F4F4F',command=self.search, font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)
        


        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)
        


        self.framerighttop.pack(fill=X)


        

        
        #################  TREE FRAME VIEW  #######################
        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("Firstname","Lastname","Regestration N°","Email","Phone Number","Level","Speciality","Group"),show='headings',yscrollcommand=self.scrollbar.set)
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


        #################   BUTTOM RIGHT FRAME   #######################

        self.framerightbuttom=Frame(self.frameright,height=500,pady=5,padx=5)
        self.framerightbuttom.pack(fill=X)

        #################   LABELS #######################
        self.LevelSelect = Label(self.framerightbuttom,text="Level:",fg='#4F4F4F',font=('tahoma',9))
        self.LevelSelect.place(x=150, y=20, width=100, height=40)

        self.SpecialitySelect = Label(self.framerightbuttom,text="Speciality:",fg='#4F4F4F',font=('tahoma',9))
        self.SpecialitySelect.place(x=250, y=20, width=100, height=40)

        self.GroupSelect = Label(self.framerightbuttom,text="Group:",fg='#4F4F4F',font=('tahoma',9))
        self.GroupSelect.place(x=350,y=20,width=100,height=40)

        self.CopySelect = Label(self.framerightbuttom, text="COPY:" , fg='#4F4F4F',font=('tahoma',9))
        self.CopySelect.place(x=200 , y=200 , width=100, height=40 )


        self.levelselect=StringVar()
        self.specialityselect=StringVar()
        self.groupselect=StringVar()


        #################   ENTRIES #######################
        self.LevelEntrySelect = ttk.Combobox(self.framerightbuttom, values=["L1","L2","L3","M1","M2","Phd"],state='readonly',textvariable=self.levelselect)
        self.LevelEntrySelect.place(x=150, y=80, width=100, height=40)

        self.SpecialityEntrySelect = ttk.Combobox(self.framerightbuttom, values=specialityvalues,state='readonly',textvariable=self.specialityselect)
        self.SpecialityEntrySelect.place(x=250, y=80, width=100, height=40)

        self.GroupEntrySelect = ttk.Combobox(self.framerightbuttom,values=["1","2","3"],state='readonly',textvariable=self.groupselect)
        self.GroupEntrySelect.place(x=350,y=80,width=100,height=40)

        self.buttonselect = Button(self.framerightbuttom,command=self.filter, text='Filter', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=20)
        self.buttonselect.place(x=500,y=80,width=200,height=40)

        self.CopyEmailsSelect =Button(self.framerightbuttom , command=self.copyEmails , text="Emails" ,fg='#4F4F4F', font=('tahoma', 9),width=20 )
        self.CopyEmailsSelect.place(x=300 , y=200 , width=100, height=30 )

        self.CopyNumbersSelect =Button(self.framerightbuttom , command=self.copyNumbers , text="Phone Numbers" ,fg='#4F4F4F', font=('tahoma', 9),width=20 )
        self.CopyNumbersSelect.place(x=400 , y=200 , width=100, height=30 )

        self.CopyRegNSelect =Button(self.framerightbuttom , command=self.copyRegistrationNumbers , text="Resitration N°" ,fg='#4F4F4F', font=('tahoma', 9),width=20 )
        self.CopyRegNSelect.place(x=500 , y=200 , width=100, height=30 )
    
    
    
    #################   BUTTON FONCTIONS #######################

    ### ADD FONTION ###

    def add(self):
        #try:
            mydb=mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor=mydb.cursor()
            sql="insert into student(firstname,lastname,registrationnumber,email,phonenumber,level,speciality,groupe) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            count = self.countgroup()
            countr=self.countRegNum()
            countp=self.countphone()
            
            if (len(self.firstname.get())==0 
                or len(self.lastname.get())==0 
                or len(self.registration.get())==0 
                or len(self.email.get())==0 
                or len(self.phoneNum.get())==0 
                or len(self.level.get())==0 
                or len(self.speciality.get())==0 
                or len(self.group.get())==0 ) :
                mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent=self.master)

            elif(countr!=0):
                mb.showerror('Error', 'This registration number is included in the database already.',parent=self.master)
            elif(count<int(self.group.get())):
                mb.showerror('Error', 'Group does not exist, please, make sure to select an available group.',parent=self.master)
            elif(countp!=0):
                mb.showerror('Error', 'This phone number is used already.',parent=self.master)

            else:
                val=(self.firstname.get(),self.lastname.get(),self.registration.get(),self.email.get(),self.phoneNum.get(),self.level.get(),self.speciality.get(),self.group.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mydb.close()
                self.read()
                self.reset()
            
                mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            """except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()"""
            



    ### READ FONTION ###
    def read(self):
        try:
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
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


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
        self.SpecialityEntrySelect.set("")
        self.LevelEntrySelect.set("")
        self.GroupEntrySelect.set("")
        self.searchstudent.delete(0,'end')

        

    



    ### DELETE FONTION ###
    def delete(self):
        try:
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
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


    ### UPDATE FONTION ###
    def update(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
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
                sql = ("update student set firstname=%s,lastname=%s, registrationnumber=%s, email=%s, phonenumber=%s, level=%s, speciality=%s, groupe=%s where registrationnumber=%s")
                val=(self.firstname.get(),self.lastname.get(),self.registration.get(),self.email.get(),self.phoneNum.get(),self.level.get(),self.speciality.get(),self.group.get(),self.iid)
                mycursor.execute(sql,val)
                mydb.commit()
                self.read()
                self.reset()
                mb.showinfo('update','this student\'s data is updated',parent=self.master)
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


    ### SEARCH FONTION ###
    def search(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        if (len(self.searchstudent.get())==0 ) :
            mb.showerror('Error', 'Data missing, please, make sure to fill the information in the search bar',parent=self.master)
        else:
            sql = ("select * from student where registrationnumber="+self.searchstudent.get())
            mycursor.execute(sql)
            myresults = mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert('', 'end', iid=myresults[0], values=myresults)
            mydb.commit()
            mydb.close()

    
     ### FILTER FONTION ###
    def filter(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        if (len(self.levelselect.get())==0 and len(self.specialityselect.get())==0 ) :
            mb.showerror('Error', 'Data missing, please, make sure to fill at least the level or speciality to filter',parent=self.master)
        
        elif(len(self.groupselect.get())==0 and len(self.specialityselect.get())==0):
            sql = ("select * from student where level='"+self.levelselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[2],values=res)
                mydb.commit()
            mydb.close()
        elif(len(self.groupselect.get())==0 and len(self.levelselect.get())==0):
            sql = ("select * from student where speciality='"+self.specialityselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[2],values=res)
                mydb.commit()
            mydb.close()
        elif(len(self.groupselect.get())==0):
            sql = ("select * from student where level='"+self.levelselect.get()+"' AND speciality='"+self.specialityselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[2],values=res)
                mydb.commit()
            mydb.close()
        elif(len(self.levelselect.get())==0):
            sql = ("select * from student where speciality='"+self.specialityselect.get()+"' AND groupe='"+self.groupselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[2],values=res)
                mydb.commit()
            mydb.close()
        elif(len(self.specialityselect.get())==0):
            sql = ("select * from student where level='"+self.levelselect.get()+"' AND groupe='"+self.groupselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[2],values=res)
                mydb.commit()
            mydb.close()

        else:
            sql = ("select * from student where level='"+self.levelselect.get()+"' AND speciality='"+self.specialityselect.get()+"' AND groupe='"+self.groupselect.get()+"'")
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('','end',iid=res[2],values=res)
                mydb.commit()
            mydb.close()




    def copyEmails(self):
        # Get selected column index
        column_index = 3

        # Get the values of the selected column
        column_values = [self.table.set(item, column_index) for item in self.table.get_children()]

        # Concatenate column values into a single string
        column_string = "\n".join(column_values)

        # Copy column values to clipboard
        pyperclip.copy(column_string)
        
        mb.showinfo('Successfully copied', 'Emails copied to clipboard',parent=self.master)


    def copyNumbers(self):
        # Get selected column index
        column_index = 4

        # Get the values of the selected column
        column_values = [self.table.set(item, column_index) for item in self.table.get_children()]

        # Concatenate column values into a single string
        column_string = "\n".join(column_values)

        # Copy column values to clipboard
        pyperclip.copy(column_string)
        
        mb.showinfo('Successfully copied', 'Phone Numbers copied to clipboard',parent=self.master)

    def copyRegistrationNumbers(self):
        # Get selected column index
        column_index = 2

        # Get the values of the selected column
        column_values = [self.table.set(item, column_index) for item in self.table.get_children()]

        # Concatenate column values into a single string
        column_string = "\n".join(column_values)

        # Copy column values to clipboard
        pyperclip.copy(column_string)
        
        mb.showinfo('Successfully copied', 'Registration numbers copied to clipboard',parent=self.master)

    def countgroup(self):
        mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )

        cursor = mydb.cursor()

        query = "SELECT numberofgroups FROM speciality WHERE specialityname=%s AND level=%s" 
        val=(self.speciality.get(),self.level.get())
        cursor.execute(query,val)

        try:
            result = cursor.fetchone()
            if result:
                count = result[0]
                return count
            else:
                return 0
        except Exception:
            return 0
        finally:
            cursor.close()
            mydb.close()
    def countphone(self):
        mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )

        cursor = mydb.cursor()

        query = ("SELECT COUNT(registrationnumber) FROM student WHERE phonenumber="+self.phoneNum.get()) 
        cursor.execute(query)

        try:
            result = cursor.fetchone()
            if result:
                count = result[0]
                return count
            else:
                return 0
        except Exception:
            return 0
        finally:
            cursor.close()
            mydb.close()
    
    def countRegNum(self):
        mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )

        cursor = mydb.cursor()

        query = ("SELECT COUNT(registrationnumber) FROM student WHERE registrationnumber="+self.registration.get()) 
        cursor.execute(query)

        try:
            result = cursor.fetchone()
            if result:
                count = result[0]
                return count
            else:
                return 0
        except Exception:
            return 0
        finally:
            cursor.close()
            mydb.close()

    
