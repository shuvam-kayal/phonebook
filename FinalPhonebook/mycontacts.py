from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from addcontacts import AddContacts
from updatecontacts import Update
from view import View

con=sqlite3.connect('mycontacts.db')
cur=con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS addressbook (person_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, person_name TEXT, person_surname TEXT, person_email TEXT, person_phone INTEGER, person_address TEXT)")


class MyContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x650+600+200")
        self.title("My Contacts")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(self,height=500,bg='#ebe834')
        self.bottom.pack(fill=X)
        
        self.top_img=ImageTk.PhotoImage(Image.open("people2.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='white')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=Label(self.top,text="My Contacts",font='arial 15 bold',bg='white',fg='#eb8034')
        self.heading.place(x=270,y=53)
        
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        
        self.searchbar=Entry(self.bottom, font='Helvetica 10',width=50,bg='#036ffc')
        self.searchbar.grid(row=0,column=0,padx=(40,0))
        
        self.searchbar.bind("<KeyRelease>", self.check)
        
        self.listbox=Listbox(self.bottom,width=50,height=27,font="Helvetica 10 bold",bg='#03c6fc')
        self.listbox.grid(row=1,column=0,padx=(40,0),pady=(2,0),sticky=N+S)
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=1,column=1,sticky=N+S,padx=(0,47))
        
        self.listbox.bind("<<ListboxSelect>>", self.fillout)
        
        trial=cur.execute("select * from 'addressbook'").fetchall()
        if len(trial)==0:
            con.execute("INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)",('Police',' ','kolkatapolice@gmail.com',100,"India"));
            con.commit()
            con.execute("INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)",('Fire','Brigade','kolkatafire@gmail.com',101,"India"))
            con.commit()
            con.execute("INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)",('Ambulance',' ','kolkataambulance@gmail.com',102,"India"))
            con.commit()
            
        persons=cur.execute("select * from 'addressbook'").fetchall()
        for person in persons:
            count=person[0]
            self.listbox.insert(count, str(person[0])+". "+str(person[1])+" "+str(person[2]))
            count +=person[0]

        badd=Button(self.bottom,text='Add',width=12,font="Sans 14 bold",command=self.add_contacts)
        badd.grid(row=1,column=2,padx=(10,50),pady=90,sticky=N)
        
        bupdate=Button(self.bottom,text='Update',width=12,font="Sans 14 bold",command=self.update_function)
        bupdate.grid(row=1,column=2,padx=(10,50),pady=140,sticky=N)
        
        bdisplay=Button(self.bottom,text='View',width=12,font="Sans 14 bold",command=self.view_person)
        bdisplay.grid(row=1,column=2,padx=(10,50),pady=190,sticky=N)
        
        bdelete=Button(self.bottom,text='Delete',width=12,font="Sans 14 bold",command=self.delete_person)
        bdelete.grid(row=1,column=2,padx=(10,50),pady=240,sticky=N)
        
    def add_contacts(self):
        add_page=AddContacts()
        self.destroy()
        
    def update_function(self):
        try:
            selected_item=self.listbox.curselection()
            person=self.listbox.get(selected_item)
            person_id=person.split(".")[0]
            
            updatepage=Update(person_id)
            self.destroy()
        except:
            messagebox.showerror("Error","No Contact Selected")
        
    def view_person(self):
        try:
            selected_item=self.listbox.curselection()
            person=self.listbox.get(selected_item)
            person_id=person.split(".")[0]
            
            viewpage=View(person_id)
            self.destroy()
        except:
            messagebox.showerror("Error","No Contact Selected")
            
    def delete_person(self):
        try:
            selected_item=self.listbox.curselection()
            person=self.listbox.get(selected_item)
            person_id=person.split(".")[0]
            
            query="delete from addressbook where person_id = {}".format(person_id)
            answer=messagebox.askquestion("Warning","Do you really want to delete"+str(person.split(".")[1]))
            if answer=='yes':
                try:
                    cur.execute(query)
                    con.commit()
                    self.destroy()
                    
                except Exception as e:
                    messagebox.showinfo("Info",str(e))
        except:
            messagebox.showerror("Error","No Contact Selected")
            
    def fillout(self,e):
        self.searchbar.delete(0, END)
        selected_item=self.listbox.curselection()
        person=self.listbox.get(selected_item)
        self.searchbar.insert(0, str(person.split(".")[1]))
        
    def check(self,e):
        typed=self.searchbar.get()
        if typed=='':
            self.listbox.delete(0, END)
            persons=cur.execute("select * from 'addressbook'").fetchall()
            for person in persons:
                count=person[0]
                self.listbox.insert(count, str(person[0])+". "+str(person[1])+" "+str(person[2]))
                count +=person[0]
        else:
            self.listbox.delete(0, END)
            peoples=cur.execute("SELECT * FROM addressbook WHERE person_name LIKE ?", ('%' + str(typed) + '%',))
            for people in peoples:
                record=people[0]
                self.listbox.insert(record, str(people[0])+". "+str(people[1])+" "+str(people[2]))
                record +=people[0]
            
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        