from tkinter import *
from PIL import Image,ImageTk
import student as s
import staff as st
import library as lib
import exam as ex
import department as dep
import mysql.connector as mc
import tkinter.messagebox as mb

class main: #Class university is the main window of the application after loging in
    def __init__(self,window):
     self.master=window
     self.master.title("Department Managment System")
     self.width=self.master.winfo_screenwidth()
     self.height=self.master.winfo_screenheight()
     self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))   
     self.master.state('zoomed')


     
     #######   TOP FRAME   #######
     self.topframe=Frame(self.master,bg='#1a8488',height=100)
     self.topframe.pack(fill=X)
     self.sms=Label(self.topframe,text='DEPARTMENT DATA MANAGEMENT',bg='#1a8488',fg='white',font=('tahoma',30,'bold'),pady=50)
     self.sms.pack()
     

     #######   CNETER FRAME   #######
     self.centerframe=Frame(self.master,bg='white')
     self.centerframe.pack(fill=X)
     self.centerframe.grid_columnconfigure(0,weight=1)
     self.centerframe.grid_columnconfigure(1,weight=1)
     self.centerframe.grid_columnconfigure(2,weight=1)


     #######   BUTTOM FRAME   #######
     self.buttomframe=Frame(self.master,height=200)
     self.buttomframe.pack(fill=X)
     self.buttomframe.grid_columnconfigure(0,weight=1)
     self.buttomframe.grid_columnconfigure(1,weight=1)



  
     # university frame
     depa = dep.Department(self.centerframe)

     # student frame
     std = s.student(self.centerframe)

     # stafft frame
     stdw = st.staff(self.centerframe)

     # library frame
     li = lib.library(self.buttomframe)
     
     # exam
     exa = ex.exam(self.buttomframe)


class Login:
    def __init__(self, window):
        self.master = window
        self.master.title("Login Window")
        self.master.geometry("450x400+450+150")
        
        self.img6 = Image.open('login.png')
        self.img6.thumbnail((200, 200))
        self.new_img6 = ImageTk.PhotoImage(self.img6)
        self.imglogin = Label(self.master, image=self.new_img6)
        self.imglogin.pack()
        
        self.frameLogin = Frame(self.master)
        self.frameLogin.pack()
        
        self.labelUser = Label(self.frameLogin, text='Username', pady=10, padx=10, font=('tahoma', 10, 'bold'))
        self.labelUser.grid(row=0, column=0)
       
        self.labelPass = Label(self.frameLogin, text='Password', pady=10, padx=10, font=('tahoma', 10, 'bold'))
        self.labelPass.grid(row=1, column=0)
        
        self.username = Entry(self.frameLogin, font=('tahoma', 10, 'bold'))
        self.username.grid(row=0, column=1, pady=10, padx=10)
        
        self.password = Entry(self.frameLogin, font=('tahoma', 10, 'bold'), show="*")
        self.password.grid(row=1, column=1, pady=10, padx=10)
        
        self.LoginButton = Button(self.frameLogin, command=self.login, text='Login', font=('tahoma', 10, 'bold'),
                                  bg='#1b9ea4', fg='white', cursor='cross')
        self.LoginButton.grid(row=2, column=0, columnspan=2, sticky='snew', pady=40, padx=50)

    def login(self):
            try:
                mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
                )
            

                mycursor = mydb.cursor()
                sql = "select * from loginadmin where Username='" + self.username.get() + "' and Password='" + self.password.get() + "'"
                mycursor.execute(sql)
                res = mycursor.fetchone()
                if (res == None):
                    mb.showerror('Failed Login', 'Invalid Username or Password ! please Try again')
                else:
                    self.master.destroy()
                    window =Tk()
                    window.iconbitmap('mortarboard.ico')
                    win=main(window)
                    mainloop()
            except:
                mb.showerror('Login Failed','Connection failed, please check your server connection')

    

 
if(__name__=='__main__'):
    window= Tk()
    window.iconbitmap('mortarboard.ico')
    log=Login(window)
    mainloop()