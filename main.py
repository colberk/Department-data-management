from tkinter import *
from PIL import Image,ImageTk
import student as s
import staff as st
import library as lib
import exam as ex
import department as dep

class main: #Class university is the main window of the application
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

    

 
if(__name__=='__main__'):
    window= Tk()
    std=main(window)
    mainloop()