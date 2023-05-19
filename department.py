from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


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
        
        self.buttomuni=Button(self.universityFrame,command=self.openUniversityWindow,font=('tahoma',10,'bold'),text='Department Management',bg='#1a8488',fg='white',padx=10,pady=10)
        self.buttomuni.pack()

    def openUniversityWindow(self):
        self.master = Toplevel()
        self.master.title('Deapartment Data Management')
        self.master.geometry("1200x600+50+50")
        