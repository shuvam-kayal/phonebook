#importing all required modules
from tkinter import*
from tkinter import messagebox
from CustomTkinter import customtkinter
from PIL import ImageTk,Image
import sqlite3
from recents import Recents
import time as tm
from datetime import datetime

#setting theme for our aplicaton
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#using day and current time
time=tm.strftime('%H:%M:%S')
day=datetime.today().strftime('%A')

#connecting with database and creating table
con=sqlite3.connect('myrecents.db')
cur=con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS recents (number_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, number INTEGER, day TEXT, time INTEGER)")

#using Toplevel to create new window
class MyKeypad(customtkinter.CTkToplevel):
    def __init__(self):
        customtkinter.CTkToplevel.__init__(self)

        #setting size and position of app in main window
        self.geometry("650x550+300+110")
        self.title("DPS Joka Students Presents")
        self.resizable(False,False)

        #creating frames
        self.top=customtkinter.CTkFrame(self,height=130,width=600, corner_radius=10, border_width=5,border_color='#08111c')
        self.top.pack(pady=10)
        
        self.bottom=customtkinter.CTkFrame(self,height=450,width=600,border_width=5,border_color='#08111c')
        self.bottom.pack(pady=10)

        #creating and resizing required images
        self.top_img=ImageTk.PhotoImage(Image.open("all/phone4.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='#292929')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=customtkinter.CTkLabel(self.top,text="Keypad",text_font='arial 18 bold',bg_color='#292929',fg_color='#292929')
        self.heading.place(x=270,y=51)

        #creating and binding entry box to type numbers
        self.entry_number=customtkinter.CTkEntry(self.bottom,text_font="Jersey 18 bold",width=400,justify=CENTER,relief=SUNKEN,border_width=2)
        self.entry_number.place(x=115,y=35)
        self.entry_number.bind("<KeyRelease>", self.check)

        #placing, creating all required buttons and their functions
        self.b1=customtkinter.CTkButton(self.bottom,text="1",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(1))
        self.b2=customtkinter.CTkButton(self.bottom,text="2",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(2))
        self.b3=customtkinter.CTkButton(self.bottom,text="3",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(3))
        self.b4=customtkinter.CTkButton(self.bottom,text="4",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(4))
        self.b5=customtkinter.CTkButton(self.bottom,text="5",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(5))
        self.b6=customtkinter.CTkButton(self.bottom,text="6",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(6))
        self.b7=customtkinter.CTkButton(self.bottom,text="7",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(7))
        self.b8=customtkinter.CTkButton(self.bottom,text="8",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(8))
        self.b9=customtkinter.CTkButton(self.bottom,text="9",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(9))
        self.b0=customtkinter.CTkButton(self.bottom,text="0",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click(0))
        self.bstar=customtkinter.CTkButton(self.bottom,text="*",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click("*"))
        self.bhash=customtkinter.CTkButton(self.bottom,text="#",text_font='arial 12 bold',bg_color="#292929",width=80,hover_color='#0d0d0d',fg_color="#8B4000",command=lambda: self.click("#"))
        self.call_img=ImageTk.PhotoImage(Image.open("all/call1.png").resize((25,25), Image.Resampling.LANCZOS))
        self.bcall=customtkinter.CTkButton(self.bottom,image=self.call_img,hover_color='brown',text_font='arial 18 bold',text='Call',width=100,border_width=0,command=self.call)
        if self.entry_number.get()=='':
            self.bcall.configure(state=DISABLED)        #keeping call button disables if no number is typed
        
        self.b9.place(x=370,y=210)
        self.b8.place(x=270,y=210)
        self.b7.place(x=170,y=210)
        
        self.b6.place(x=370,y=150)
        self.b5.place(x=270,y=150)
        self.b4.place(x=170,y=150)
        
        self.b3.place(x=370,y=90)
        self.b2.place(x=270,y=90)
        self.b1.place(x=170,y=90)
        
        self.b0.place(x=270,y=270)
        self.bstar.place(x=170,y=270)
        self.bhash.place(x=370,y=270)
        self.bcall.place(x=263,y=330)

    #funtion for clicking buttons
    def click(self,n):
        self.g=self.entry_number.get()
        self.entry_number.delete(0,END)
        self.entry_number.insert(0,str(self.g) + str(n))
        self.bcall.configure(state=NORMAL)
        
    #function for call button
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

    #function for disabling and enabling buttons if something is typed in entry box
    def check(self,e):
        typed=self.entry_number.get()
        if typed=='':
            self.bcall.configure(state=DISABLED)
        else:
            self.bcall.configure(state=NORMAL)






