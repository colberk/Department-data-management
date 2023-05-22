from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc


class Department:
    def __init__(self,cf):
        self.centerFrame=cf
        self.universityFrame=Frame(self.centerFrame,padx=10,pady=10)
        
        self.universityFrame.grid(row=0,column=0,sticky='senw',ipady=5)
        self.img = Image.open('department.png')
        self.img.thumbnail((200,200))
        self.new_img=ImageTk.PhotoImage(self.img)
        self.imguniv=Label(self.universityFrame,image=self.new_img,padx=10,pady=10)
        self.imguniv.pack()
        
        self.buttomuni=Button(self.universityFrame,command=self.openUniversityWindow,font=('tahoma',10,'bold'),text='Specialities And Groups',bg='#1a8488',fg='white',padx=10,pady=10)
        self.buttomuni.pack()

    def openUniversityWindow(self):
        self.master = Toplevel()
        self.master.title('Specialties And Groups')
        self.master.geometry("1200x500+50+50")
        self.master.iconbitmap('mortarboard.ico')

        #######   TOP FRAME   #######
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='SPECIALITIES AND GROUPS MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()
        


        #######   LEFT FRAME   #######
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)

        #################   LABELS #######################
        self.SpecialityName=Label(self.frameleft,text='Speciality\'s Name:',fg='#4F4F4F',font=('tahoma',9))
        self.SpecialityName.place(x=10,y=80,width=100,height=40)
        
        self.Level = Label(self.frameleft, text='Level:',fg='#4F4F4F',font=('tahoma',9))
        self.Level.place(x=10,y=130,width=100,height=40)
        
        self.NumberGroup = Label(self.frameleft, text='Number of groups:',fg='#4F4F4F',font=('tahoma',9))
        self.NumberGroup.place(x=10,y=180,width=100,height=40)
        
        
        
        self.specialityname = StringVar()
        self.level = StringVar()
        self.numbergroup = StringVar()



        #################   ENTRIES #######################

        self.SpecialityNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12),textvariable=self.specialityname)
        self.SpecialityNameEntry.place(x=120,y=80,width=200,height=40)
        
        self.LevelEntry = ttk.Combobox(self.frameleft, values=["L1","L2","L3","M1","M2"],state='readonly',textvariable=self.level)
        self.LevelEntry.place(x=120,y=130,width=200,height=40)
        
        self.NumberGroupsEntry = ttk.Combobox(self.frameleft,values=["1","2","3","4","5","6","7","8","9","10"],state='readonly',textvariable=self.numbergroup)
        self.NumberGroupsEntry.place(x=120,y=180,width=200,height=40)



        #################   BUTTONS #######################

        self.buttonAdd=Button(self.frameleft,text="ADD",command=self.add,font=('tahoma',10))
        self.buttonAdd.place(x=20,y=350,width=60,height=60)
        
        self.buttonUpdate = Button(self.frameleft, text="UPDATE",command=self.update,font=('tahoma',10))
        self.buttonUpdate.place(x=100, y=350,width=60,height=60)
        
        self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.delete,font=('tahoma',10))
        self.buttonDelete.place(x=180, y=350,width=60,height=60)
        
        self.buttonRead = Button(self.frameleft,  text="SHOW",command=self.read, font=('tahoma', 10))
        self.buttonRead.place(x=260, y=350, width=60, height=60)
        
        self.buttonReset = Button(self.frameleft, text="RESET",command=self.reset, font=('tahoma', 10))
        self.buttonReset.place(x=340, y=350, width=60, height=60)


        #################   RIGHT FRAME #######################
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5)

        self.searchspeciality = StringVar()


        self.SearchSpeciality = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=10,textvariable=self.searchspeciality)
        self.SearchSpeciality.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        
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
        self.table=ttk.Treeview(self.frameView,columns=("ID","Speciality Name","Level","Number Of Groups"),show='headings', yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

    
        self.table.heading("ID", text="ID")
        self.table.heading("Speciality Name", text="Speciality Name")
        self.table.heading("Level", text="Level")
        self.table.heading("Number Of Groups", text="Number Of Groups")

        self.table.column("ID", anchor=W,width= 20)
        self.table.column("Speciality Name",anchor=W,width= 200)
        self.table.column("Level",anchor=W,width=200)
        self.table.column("Number Of Groups",anchor=W,width= 200)

        self.read()
        self.table.bind("<ButtonRelease>",self.show)
    
    
    
    #################   BUTTON FONCtIONS #######################

    ### ADD FONTION ###

    def add(self):
        try:
            mydb=mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor=mydb.cursor()
            sql="insert into speciality(specialityname,level,numberofgroups) values (%s,%s,%s)"

            if (len(self.specialityname.get())==0 or len(self.level.get())==0 or len(self.numbergroup.get())==0) :
                mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent=self.master)

            else:
                val=(self.specialityname.get(),self.level.get(),self.numbergroup.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mydb.close()
                self.read()
                self.reset()
            
                mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
        except:
                mb.showerror('Login Failed','Connection failed, please check your server connection')
            



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
            sql="select * from speciality"
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


    ### SHOW FONTION ###
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.specialityname.set(val[1])
        self.level.set(val[2])
        self.numbergroup.set(val[3])


    ### RESET FONTION ###
    def reset(self):
        self.SpecialityNameEntry.delete(0,'end')
        self.LevelEntry.set("")
        self.NumberGroupsEntry.set("")


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
            sql = ("delete from speciality where id="+self.iid)
            mycursor.execute(sql)
            mydb.commit()
            mb.showinfo('Delete','Date deleted successfully',parent=self.master)
            self.read()
            self.reset()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')


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
            sql = ("update speciality set specialityname=%s,level=%s, numberofgroups=%s where id=%s")
            val=(self.specialityname.get(),self.level.get(),self.numbergroup.get(),self.iid)
            print(self.iid)
            mycursor.execute(sql,val)
            mydb.commit()
            self.read()
            self.reset()
            mb.showinfo('update','Date updated successfully',parent=self.master)
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()


    ### SEARCH FONTION ###
    def search(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = ("select * from speciality where id="+self.searchspeciality.get())
            mycursor.execute(sql)
            myresults = mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert('', 'end', iid=myresults[0], values=myresults)
            mydb.commit()
            mydb.close()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()
    
    