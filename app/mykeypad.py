from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from recents import Recents
import time as tm
from datetime import datetime

time=tm.strftime('%H:%M:%S')

day=datetime.today().strftime('%A')

con=sqlite3.connect('recents_backup2.db')
cur=con.cursor()

class MyKeypad(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x650+600+200")
        self.title("Keypad")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(self,height=500,bg='#ebe834')
        self.bottom.pack(fill=X)
        
        self.top_img=ImageTk.PhotoImage(Image.open("phone4.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='white')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=Label(self.top,text="Keypad",font='arial 15 bold',bg='white',fg='#eb8034')
        self.heading.place(x=270,y=51)

        self.entry_number=Entry(self.bottom,font="Jersey 18 bold",width=30,justify=CENTER,relief=SUNKEN,bd=2)
        self.entry_number.place(x=115,y=35)
        
        self.b1=Button(self.bottom,text="1",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(1))
        self.b2=Button(self.bottom,text="2",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(2))
        self.b3=Button(self.bottom,text="3",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(3))
        self.b4=Button(self.bottom,text="4",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(4))
        self.b5=Button(self.bottom,text="5",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(5))
        self.b6=Button(self.bottom,text="6",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(6))
        self.b7=Button(self.bottom,text="7",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(7))
        self.b8=Button(self.bottom,text="8",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(8))
        self.b9=Button(self.bottom,text="9",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(9))
        self.b0=Button(self.bottom,text="0",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click(0))
        self.bstar=Button(self.bottom,text="*",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click("*"))
        self.bhash=Button(self.bottom,text="#",font='arial 12 bold',bg="white",padx=33,pady=10,fg="black",command=lambda: self.click("#"))
        self.call_img=ImageTk.PhotoImage(Image.open("phone3.jpg"))
        self.bcall=Button(self.bottom,image=self.call_img,bg='#ebe834',bd=0,command=self.call)
        
        self.b9.place(x=370,y=200)
        self.b8.place(x=270,y=200)
        self.b7.place(x=170,y=200)
        
        self.b6.place(x=370,y=140)
        self.b5.place(x=270,y=140)
        self.b4.place(x=170,y=140)
        
        self.b3.place(x=370,y=80)
        self.b2.place(x=270,y=80)
        self.b1.place(x=170,y=80)
        
        self.b0.place(x=270,y=260)
        self.bstar.place(x=170,y=260)
        self.bhash.place(x=370,y=260)
        self.bcall.place(x=270,y=320)
        
    def click(self,n):
        self.g=self.entry_number.get()
        self.entry_number.delete(0,END)
        self.entry_number.insert(0,str(self.g) + str(n))
        
    def call(self):
        number=self.entry_number.get()
        today=day
        current_time=time
        
        if number !="":
            response=messagebox.showerror("Call Failed","Network Error")
            try:
                query="insert into 'recents' (number, day, time) values (?,?,?)"
                cur.execute(query, (number, day, time))
                con.commit()
            except Exception as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","No number typed",icon="warning")
            
        self.entry_number.delete(0,END)






