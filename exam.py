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
        self.master.geometry("1200x500+50+50")


        ############################   TOP FRAME   ############################
        self.topframe=Frame(self.master,bg='#105356',height=10)
        self.topframe.pack(fill=X)
        self.sms=Label(self.topframe,text='EXAM DATA MANAGEMENT',bg='#105356',fg='white',font=('tahoma',12,'bold'),pady=5)
        self.sms.pack()
    
        ######################     LEFT FRAME     #######################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)

        ####################   LABELS    ######################
        self.GroupLabel = Label(self.frameleft, text='Group:', fg='#4F4F4F', font=('tahoma', 9))
        self.GroupLabel.place(x=15, y=30, width=120, height=40)
        
        self.ClassroomLabel = Label(self.frameleft, text='Classroom:', fg='#4F4F4F', font=('tahoma', 9))
        self.ClassroomLabel.place(x=10, y=80, width=120, height=40)

        self.ModuleLabel = Label(self.frameleft, text='Module:', fg='#4F4F4F', font=('tahoma', 9))
        self.ModuleLabel.place(x=10, y=130, width=120, height=40)
        
        self.ProfLabel = Label(self.frameleft, text='Teacher:', fg='#4F4F4F', font=('tahoma', 9))
        self.ProfLabel.place(x=10, y=180, width=120, height=40)
        
        self.DateLabel = Label(self.frameleft, text='Date:', fg='#4F4F4F', font=('tahoma', 9))
        self.DateLabel.place(x=15, y=230, width=120, height=40)
        
        self.TimeLabel = Label(self.frameleft, text='Time:', fg='#4F4F4F', font=('tahoma', 9))
        self.TimeLabel.place(x=15, y=280, width=120, height=40)

        self.group = StringVar()
        self.classroom = StringVar()
        self.module = StringVar()
        self.prof = StringVar()
        self.date = StringVar()
        self.time = StringVar()



        ####################   ENTRIES    ######################
        self.GroupEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.group)
        self.GroupEntry.place(x=170, y=30, width=200, height=40)
        
        self.ClassroomEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.classroom)
        self.ClassroomEntry.place(x=170, y=80, width=200, height=40)

        self.ModuleEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.module)
        self.ModuleEntry.place(x=170, y=130, width=200, height=40)
        
        self.ProfEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 9), textvariable=self.prof)
        self.ProfEntry.place(x=170, y=180, width=200, height=40)
        
        self.DateEntry = DateEntry(self.frameleft ,textvariable=self.date, date_pattern="yyyy-mm-dd",mindate=datetime.date.today())
        self.DateEntry.place(x=170, y=230,width=200,height=40)
        
        self.TimeEntry = ttk.Combobox(self.frameleft, values=["", "8:00", "9:00", "10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"],
                                      state='readonly', textvariable=self.time)
        self.TimeEntry.place(x=170, y=280, width=200,height=30)



        ####################   BUTTONS    ######################
        self.buttonAdd = Button(self.frameleft, text="ADD",command=self.add,  font=('tahoma', 10))
        self.buttonAdd.place(x=20, y=350, width=60, height=60)
        
        self.buttonUpdate = Button(self.frameleft,  text="UPDATE",command=self.update, font=('tahoma', 10))
        self.buttonUpdate.place(x=100, y=350, width=60, height=60)
        
        self.buttonDelete = Button(self.frameleft, text="DELETE",command=self.delete, font=('tahoma', 10))
        self.buttonDelete.place(x=180, y=350, width=60, height=60)
        
        self.buttonRead = Button(self.frameleft, text="SHOW",command=self.read, font=('tahoma', 10))
        self.buttonRead.place(x=260, y=350, width=60, height=60)
        
        self.buttonReset = Button(self.frameleft, text="RESET",command=self.reset, font=('tahoma', 10))
        self.buttonReset.place(x=340, y=350, width=60, height=60)




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
                                  columns=("ID","GroupeName","ClassRoom","Module","Professor","Date","Time"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("GroupeName", text="GroupeName")
        self.table.heading("ClassRoom", text="ClassRoom")
        self.table.heading("Module", text="Module")
        self.table.heading("Professor", text="Professor")
        self.table.heading("Date", text="Date")
        self.table.heading("Time", text="Time")

        self.table.column("ID", anchor=W, width=7)
        self.table.column("GroupeName", anchor=W,width=100)
        self.table.column("ClassRoom", anchor=W,width=100)
        self.table.column("Module", anchor=W,width=100)
        self.table.column("Professor", anchor=W,width=100)
        self.table.column("Date", anchor=W,width=100)
        self.table.column("Time", anchor=W)
        self.read()
        self.table.bind("<ButtonRelease-1>", self.show)

    def add(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = "insert into exam(groupex,classroom,module,professor,date,time) values (%s,%s,%s,%s,%s,%s)"
        if (len(self.group.get()) == 0 or len(self.classroom.get()) == 0 or len(self.module.get()) == 0 or len(self.prof.get()) == 0 or len(self.date.get()) == 0 or len(self.time.get()) == 0):
            mb.showerror('Error', 'Data missing, please, make sure to fill all the information needed.',parent = self.master)
        else:
            val = (self.group.get(), self.classroom.get(), self.module.get(), self.prof.get(),self.date.get(),self.time.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully', parent=self.master)
            self.reset()
            self.read()

    def read(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = "select * from Exam"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('', 'end', iid=res[0], values=res)
            mydb.commit()
        mydb.close()

    def show(self, ev):
        self.iid = self.table.focus()
        alldata = self.table.item(self.iid)
        val = alldata['values']
        self.group.set(val[1])
        self.classroom.set(val[2])
        self.module.set(val[3])
        self.prof.set(val[4])
        self.date.set(val[5])
        self.time.set(val[6])

    def reset(self):
        self.GroupEntry.delete(0, 'end')
        self.ClassroomEntry.delete(0, 'end')
        self.ProfEntry.delete(0, 'end')
        self.ModuleEntry.delete(0, 'end')
        self.DeliveryDateEntry.selection_clear()
        self.TimeEntry.set("")

    def delete(self):
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

    def update(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update exam set groupex=%s,classroom=%s,module=%s,professor=%s,date=%s,time=%s where id=%s")
        val = (self.group.get(), self.classroom.get(), self.module.get(),self.prof.get(), self.date.get(), self.time.get(),self.iid)
        mycursor.execute(sql, val)
        mydb.commit()
        mb.showinfo('update', 'Data updated successfully', parent=self.master)
        self.read()
        self.reset()

    def search(self):
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