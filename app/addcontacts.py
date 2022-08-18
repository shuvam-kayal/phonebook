from tkinter import*
from PIL import ImageTk,Image
import sqlite3

con=sqlite3.connect('database_backup.db')
cur=con.cursor()

class AddContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x650+600+200")
        self.title("Add New Contact")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(self,height=500,bg='#34eb99')
        self.bottom.pack(fill=X)
        
        self.top_img=ImageTk.PhotoImage(Image.open("person1.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='white')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=Label(self.top,text="Add New Contact",font='arial 15 bold',bg='white',fg='#eb8034')
        self.heading.place(x=270,y=53)
        
        self.label_name=Label(self.bottom,text="    Name    ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_name.place(x=45,y=45)
        self.entry_name=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=170,y=47)
        
        self.label_surname=Label(self.bottom,text="  Surname ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_surname.place(x=45,y=95)
        self.entry_surname=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_surname.insert(0,"Enter Surame")
        self.entry_surname.place(x=170,y=97)
        
        self.label_email=Label(self.bottom,text="    Email    ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_email.place(x=45,y=145)
        self.entry_email=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_email.insert(0,"Enter Email")
        self.entry_email.place(x=170,y=147)
        
        self.label_phone=Label(self.bottom,text="Phone No.",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_phone.place(x=45,y=195)
        self.entry_phone=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_phone.insert(0,"Enter Phone No.")
        self.entry_phone.place(x=170,y=197)
        
        self.label_address=Label(self.bottom,text="  Address  ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_address.place(x=45,y=245)
        self.entry_address=Text(self.bottom,width=40,height=10,bd=4,font='Helvetica 10')
        self.entry_address.insert(1.0,"Enter Address")
        self.entry_address.place(x=170,y=247)
        
        button=Button(self.bottom,text="Add",font="Helvetica 15",bg="#4b42f5",command=self.add_contacts)
        button.place(x=295,y=430)
        
    def add_contacts(self):
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.entry_address.get(1.0,'end-1c')
        
        
        if name and surname and email and phone and address !="":
            try:
                query="insert into 'addressbook' (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("Success","Contact Added")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","Fill all fields",icon="warning")
            
        
        
        
        
        
        