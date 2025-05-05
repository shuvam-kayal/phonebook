#importing all required modules
from tkinter import*
from PIL import ImageTk,Image
from CustomTkinter import customtkinter
import sqlite3
from tkinter import messagebox

#setting theme for our aplicaton
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#connecting with database and creating table
con=sqlite3.connect('mycontacts.db')
cur=con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS addressbook (person_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, person_name TEXT, person_surname TEXT, person_email TEXT, person_phone INTEGER, person_address TEXT)")

#using Toplevel to create new window
class AddContacts(customtkinter.CTkToplevel):
    def __init__(self):
        customtkinter.CTkToplevel.__init__(self)

        #setting size and position of app in main window
        self.geometry("650x650+300+35")
        self.title("DPS Joka Students Presents")
        self.resizable(False,False)

        #creating and resizing required images
        self.top_img=ImageTk.PhotoImage(Image.open("all/person1.png"))
        self.add_person_img=ImageTk.PhotoImage(Image.open("all/add_person.png").resize((20,20), Image.Resampling.LANCZOS))
        
        #creating frames
        self.top=customtkinter.CTkFrame(self,height=145,corner_radius=10, border_width=5,border_color='#08111c')
        self.top.pack(fill=X,padx=10,pady=7)
        
        self.bottom=customtkinter.CTkFrame(self,height=490,corner_radius=10, border_width=5,border_color='#08111c')
        self.bottom.pack(fill=X,padx=10,pady=7)

        #creating heading and top image
        self.top_image_label=Label(self.top,image=self.top_img,bg='#292929')
        self.top_image_label.place(x=150,y=20)

        self.heading=customtkinter.CTkLabel(self.top,text="Add New Contact",text_font='arial 18 bold',fg_color='#292929')
        self.heading.place(x=270,y=53)

        #creating and placing required entry boxes, labels and text boxes
        self.label_name=customtkinter.CTkLabel(self.bottom,text="    Name    ",text_font="arial 15 bold",fg_color="#383838",corner_radius=10)
        self.label_name.place(x=45,y=45)
        self.entry_name=customtkinter.CTkEntry(self.bottom,width=375,height=30,border_width=4,text_font='Helvetica 10',border_color='#1a1919')
        self.entry_name.place(x=200,y=45)
        
        self.label_surname=customtkinter.CTkLabel(self.bottom,text="  Surname ",text_font="arial 15 bold",fg_color="#383838",corner_radius=10)
        self.label_surname.place(x=45,y=95)
        self.entry_surname=customtkinter.CTkEntry(self.bottom,width=375,height=30,border_width=4,text_font='Helvetica 10',border_color='#1a1919')
        self.entry_surname.place(x=200,y=95)
        
        self.label_email=customtkinter.CTkLabel(self.bottom,text="    Email    ",text_font="arial 15 bold",fg_color="#383838",corner_radius=10)
        self.label_email.place(x=45,y=145)
        self.entry_email=customtkinter.CTkEntry(self.bottom,width=375,border_width=4,text_font='Helvetica 10',border_color='#1a1919')
        self.entry_email.place(x=200,y=145)
        
        self.label_phone=customtkinter.CTkLabel(self.bottom,text="Phone No.",text_font="arial 15 bold",fg_color="#383838",corner_radius=10)
        self.label_phone.place(x=45,y=195)
        self.entry_phone=customtkinter.CTkEntry(self.bottom,width=375,border_width=4,text_font='Helvetica 10',border_color='#1a1919')
        self.entry_phone.place(x=200,y=195)
        
        self.label_address=customtkinter.CTkLabel(self.bottom,text="  Address  ",text_font="arial 15 bold",fg_color="#383838",corner_radius=10)
        self.label_address.place(x=45,y=245)
        self.entry_address=Text(self.bottom,width=51,height=8,highlightthickness=4,highlightcolor='#1a1919',font='Helvetica 10',fg="#d0d0d0",bg='#292929')
        self.entry_address.config(highlightbackground='#1a1919')
        self.entry_address.place(x=200,y=245)

        #creating button to add all data
        self.button=customtkinter.CTkButton(self.bottom,text=" Add ",text_font="Helvetica 15",image=self.add_person_img ,command=self.add_contacts,corner_radius=5)
        self.button.place(x=280,y=420)

    #function to add all data
    def add_contacts(self):
        #taking data from entry boxes
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.entry_address.get("1.0", "end-1c")

        #adding data to database
        if name and surname and email and phone and address !="":
            try:
                query="INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("Success","Contact Added")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error",str(e))
        else:
            #error message if all fields are not filled
            messagebox.showerror("Error","Fill all fields",icon="warning")
            
        
        
        
        
        
        
