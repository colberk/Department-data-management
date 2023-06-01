import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc
from tkcalendar import DateEntry
import datetime


class exam:
    def __init__(self,bf):
        self.buttomFrame=bf
        self.examFrame=Frame(self.buttomFrame,padx=100,pady=10)
        
        self.examFrame.grid(row=1,column=1,sticky='senw',ipady=5)
        self.img4=Image.open('C:\memoire\exam.png')
        self.img4.thumbnail((200,200))
        self.new_img4=ImageTk.PhotoImage(self.img4)
        self.imgstaff=Label(self.examFrame,image=self.new_img4,padx=10,pady=10)
        self.imgstaff.pack()
        
        self.buttomex=Button(self.examFrame,command=self.openExamWindow,font=('tahoma',10,'bold'),text='Exam Management',bg='#1a8488',fg='white',padx=10,pady=10)
        self.buttomex.pack()

    def openExamWindow(self):
        self.master = Toplevel()
        self.master.title('Exam Management')
        self.master.geometry("1200x650+50+50")
        self.master.iconbitmap('mortarboard.ico')
        self.master.resizable(False, False)


        ############################   TOP FRAME   ############################
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='EXAM DATA MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()
    
        ######################     LEFT FRAME     #######################
        self.frameleft = Frame(self.master, width=400,bg='#d9d9d8')
        self.frameleft.pack(side=LEFT, fill=BOTH)

        ####################   LABELS    ######################
        self.Title=Label(self.frameleft,text='DATA MANUPILATION SECTION',fg='#4F4F4F',bg='#d9d9d8',font=('tahoma',12,'bold'))
        self.Title.place(x=50,y=10,width=310,height=40)

        self.SpecialityLabel = Label(self.frameleft, text='Speciality:', fg='#4F4F4F', bg='#d9d9d8',font=('tahoma', 9))
        self.SpecialityLabel.place(x=15, y=50, width=120, height=40)

        self.LevelLabel = Label(self.frameleft, text='Level:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.LevelLabel.place(x=15, y=100, width=120, height=40)

        self.GroupLabel = Label(self.frameleft, text='Group:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.GroupLabel.place(x=15, y=150, width=120, height=40)
        
        self.ClassroomLabel = Label(self.frameleft, text='Classroom:', fg='#4F4F4F', bg='#d9d9d8',font=('tahoma', 9))
        self.ClassroomLabel.place(x=10, y=200, width=120, height=40)

        self.ModuleLabel = Label(self.frameleft, text='Module:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.ModuleLabel.place(x=10, y=250, width=120, height=40)
        
        self.ProfLabel = Label(self.frameleft, text='Teachers(guards):', fg='#4F4F4F', bg='#d9d9d8',font=('tahoma', 9))
        self.ProfLabel.place(x=10, y=300, width=120, height=40)

        self.ResProfLabel = Label(self.frameleft, text='Responsible professor:', fg='#4F4F4F', bg='#d9d9d8',font=('tahoma', 9))
        self.ResProfLabel.place(x=10, y=350, width=120, height=40)
        
        self.DateLabel = Label(self.frameleft, text='Date:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.DateLabel.place(x=15, y=400, width=120, height=40)
        
        self.TimeLabel = Label(self.frameleft, text='Time:', fg='#4F4F4F',bg='#d9d9d8', font=('tahoma', 9))
        self.TimeLabel.place(x=15, y=450, width=120, height=40)


        self.speciality = StringVar()
        self.level = StringVar()
        self.group = StringVar()
        self.classroom = StringVar()
        self.module = StringVar()
        self.prof = StringVar()
        self.resposibleprof = StringVar()
        self.date = StringVar()
        self.time = StringVar()


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

        mycursor1=mydb.cursor()
        sql1="SELECT CONCAT(firstname,' ', lastname) FROM staff where job = 'Professor' OR job= 'Professor-grade1' OR  job='Professor-grade2'"
        mycursor1.execute(sql1)
        staffvalues=mycursor1.fetchall()
        staffvalues=list(set(staffvalues))
        staffvalues = [str(element).replace("(", "").replace(")", "").replace("'", "").replace(",", "") for element in staffvalues]
        
        



        ####################   ENTRIES    ######################
        self.SpecialityEntry = ttk.Combobox(self.frameleft, values=specialityvalues,state='readonly', textvariable=self.speciality)
        self.SpecialityEntry.place(x=170, y=50, width=200, height=40)

        self.LevelEntry = ttk.Combobox(self.frameleft, values=["L1","L2","L3","M1","M2","Phd"],state='readonly', textvariable=self.level)
        self.LevelEntry.place(x=170, y=100, width=200, height=40)

        self.GroupEntry = ttk.Combobox(self.frameleft,values=["1","2","3"],state='readonly', textvariable=self.group)
        self.GroupEntry.place(x=170, y=150, width=200, height=40)
        
        self.ClassroomEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.classroom)
        self.ClassroomEntry.place(x=170, y=200, width=200, height=40)

        self.ModuleEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.module)
        self.ModuleEntry.place(x=170, y=250, width=200, height=40)
        
        self.ProfEntry = ttk.Combobox(self.frameleft, values=staffvalues,state='readonly', textvariable=self.prof)
        self.ProfEntry.place(x=170, y=300, width=200, height=40)

        self.ResProfEntry = ttk.Combobox(self.frameleft, values=staffvalues,state='readonly', textvariable=self.resposibleprof)
        self.ResProfEntry.place(x=170, y=350, width=200, height=40)
        
        self.DateEntry = DateEntry(self.frameleft ,textvariable=self.date, date_pattern="yyyy-mm-dd",mindate=datetime.date.today())
        self.DateEntry.place(x=170, y=400,width=200,height=40)
        
        self.TimeEntry = ttk.Combobox(self.frameleft, values=["", "8:00", "9:00", "10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"],
                                      state='readonly', textvariable=self.time)
        self.TimeEntry.place(x=170, y=450, width=200,height=30)


        mydb.commit()
        mydb.close()



        ####################   BUTTONS    ######################
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




        ############################# RIGHT FRAME #############################
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)


        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5)

        self.searchexam = StringVar()

        self.SearchExam = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.SearchExam.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop, text='Search', fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################## FRAME TREE VIEW ##################

        self.frameView = Frame(self.frameright, bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar = Scrollbar(self.frameView, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameView,
                                  columns=("ID","Speciality","Level","GroupeName","ClassRoom","Module","Guadrs","Responsible Professor","Date","Time"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("Speciality", text="Speciality")
        self.table.heading("Level", text="Level")
        self.table.heading("GroupeName", text="GroupeName")
        self.table.heading("ClassRoom", text="ClassRoom")
        self.table.heading("Module", text="Module")
        self.table.heading("Guadrs", text="Guadrs")
        self.table.heading("Responsible Professor", text="Responsible Professor")
        self.table.heading("Date", text="Date")
        self.table.heading("Time", text="Time")

        self.table.column("ID", anchor=W, width=7)
        self.table.column("Speciality", anchor=W,width=100)
        self.table.column("Level", anchor=W,width=50)
        self.table.column("GroupeName", anchor=W,width=50)
        self.table.column("ClassRoom", anchor=W,width=100)
        self.table.column("Module", anchor=W,width=100)
        self.table.column("Guadrs", anchor=W,width=100)
        self.table.column("Responsible Professor", anchor=W,width=100)
        self.table.column("Date", anchor=W,width=100)
        self.table.column("Time", anchor=W,width=100)
        self.read()
        self.table.bind("<ButtonRelease-1>", self.show)
        self.reset()

    def add(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = "insert into exam(speciality,level,groupex,classroom,module,professor,responsibleprof,date,time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            if (len(self.speciality.get())==0 or len(self.level.get()) == 0 or len(self.group.get()) == 0 or len(self.classroom.get()) == 0 or len(self.module.get()) == 0 or len(self.prof.get()) == 0 or len(self.resposibleprof.get()) == 0 or len(self.date.get()) == 0 or len(self.time.get()) == 0):
                mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent = self.master)
            else:
                val = (self.speciality.get(),self.level.get(),self.group.get(), self.classroom.get(), self.module.get(), self.prof.get(), self.resposibleprof.get(),self.date.get(),self.time.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mydb.close()
                mb.showinfo('Successfully added', 'Data inserted Successfully', parent=self.master)
                self.reset()
                self.read()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()
        

    def read(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = "select * from exam"
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('', 'end', iid=res[0], values=res)
                mydb.commit()
            mydb.close()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()

    def show(self, ev):
        self.iid = self.table.focus()
        alldata = self.table.item(self.iid)
        val = alldata['values']
        self.speciality.set(val[1])
        self.level.set(val[2])
        self.group.set(val[3])
        self.classroom.set(val[4])
        self.module.set(val[5])
        self.prof.set(val[6])
        self.resposibleprof.set(val[7])
        self.date.set(val[8])
        self.time.set(val[9])

    def reset(self):
        self.SpecialityEntry.delete(0, 'end')
        self.LevelEntry.delete(0, 'end')
        self.GroupEntry.delete(0, 'end')
        self.ClassroomEntry.delete(0, 'end')
        self.ProfEntry.delete(0, 'end')
        self.ResProfEntry.delete(0, 'end')
        self.ModuleEntry.delete(0, 'end')
        self.DateEntry.delete(0,END)
        self.TimeEntry.set("")
        self.SearchExam.delete(0,'end')

    def delete(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = ("delete from exam where id="+ self.iid)
            mycursor.execute(sql)
            mydb.commit()
            mb.showinfo('Delete', 'Data deleted successfully', parent=self.master)
            self.read()
            self.reset()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()

    def update(self):
        try:
            if (len(self.speciality.get())==0 or len(self.level.get()) == 0 or len(self.group.get()) == 0 or len(self.classroom.get()) == 0 or len(self.module.get()) == 0 or len(self.prof.get()) == 0 or len(self.resposibleprof.get()) == 0 or len(self.date.get()) == 0 or len(self.time.get()) == 0):
                mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent = self.master)
            else:
                mydb = mc.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='university'
                )
                mycursor = mydb.cursor()
                sql = ("update exam set speciality=%s,level=%s,groupex=%s,classroom=%s,module=%s,professor=%s,responsibleprof=%s,date=%s,time=%s where id=%s")
                val = (self.speciality.get(),self.level.get(),self.group.get(), self.classroom.get(), self.module.get(),self.prof.get(),self.resposibleprof.get(), self.date.get(), self.time.get(),self.iid)
                mycursor.execute(sql, val)
                mydb.commit()
                mb.showinfo('update', 'Data updated successfully', parent=self.master)
                self.read()
                self.reset()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()

    def search(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            print(self.searchexam.get())
            sql = ("select * from exam where id=" + self.searchexam.get())
            mycursor.execute(sql)
            myresults = mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            # print(myresults)
            self.table.insert('', 'end', iid=myresults[0], values=myresults)
            mydb.commit()
            mydb.close()
        except:
            mb.showerror('Login Failed','Connection failed, please check your server connection')
            self.master.destroy()