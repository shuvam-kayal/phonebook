from tkinter import*
from PIL import ImageTk,Image
import sqlite3

con=sqlite3.connect('database_backup.db')
cur=con.cursor()

class Update(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        
        self.geometry("650x650+600+200")
        self.title("Update Contact")
        self.resizable(False,False)
        
        query="select * from 'addressbook' where person_id='{}'".format(person_id)
        result=cur.execute(query).fetchone()
        self.person_id=person_id
        person_name=result[1]
        person_surname=result[2]
        person_email=result[3]
        person_phone=result[4]
        person_address=result[5]
        
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(self,height=500,bg='#34eb99')
        self.bottom.pack(fill=X)
        
        self.top_img=ImageTk.PhotoImage(Image.open("person1.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='white')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=Label(self.top,text="Update Contact",font='arial 15 bold',bg='white',fg='#eb8034')
        self.heading.place(x=270,y=53)
        
        self.label_name=Label(self.bottom,text="    Name    ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_name.place(x=45,y=45)
        self.entry_name=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_name.insert(0,person_name)
        self.entry_name.place(x=170,y=47)
        
        self.label_surname=Label(self.bottom,text="  Surname ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_surname.place(x=45,y=95)
        self.entry_surname=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_surname.insert(0,person_surname)
        self.entry_surname.place(x=170,y=97)
        
        self.label_email=Label(self.bottom,text="    Email    ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_email.place(x=45,y=145)
        self.entry_email=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_email.insert(0,person_email)
        self.entry_email.place(x=170,y=147)
        
        self.label_phone=Label(self.bottom,text="Phone No.",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_phone.place(x=45,y=195)
        self.entry_phone=Entry(self.bottom,width=40,bd=4,font='Helvetica 10')
        self.entry_phone.insert(0,person_phone)
        self.entry_phone.place(x=170,y=197)
        
        self.label_address=Label(self.bottom,text="  Address  ",font="arial 15 bold",fg="white",bg="#eb8034")
        self.label_address.place(x=45,y=245)
        self.entry_address=Text(self.bottom,width=40,height=10,bd=4,font='Helvetica 10')
        self.entry_address.insert(1.0,person_address)
        self.entry_address.place(x=170,y=247)
        
        button=Button(self.bottom,text="Update",font="Helvetica 15",bg="#4b42f5",command=self.update_contacts)
        button.place(x=295,y=430)
        
    def update_contacts(self):
        id=self.person_id
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.entry_address.get(1.0,'end-1c')
        query="update addressbook set person_name = '{}', person_surname = '{}', person_email = '{}', person_phone = '{}', person_address = '{}' where person_id = {}".format(name,surname,email,phone,address,id)
        
        try:
           cur.execute(query)
           con.commit()
           messagebox.showinfo("Success","Contact Updated")
           self.destroy()
        except EXCEPTION as e:
            print(e)
        

        
        
        
        