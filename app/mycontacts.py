from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from addcontacts import AddContacts
from updatecontacts import Update
from view import View

con=sqlite3.connect('database_backup.db')
cur=con.cursor()

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
        
        self.listbox=Listbox(self.bottom,width=50,height=27,font="Helvetica 10 bold")
        self.listbox.grid(row=0,column=0,padx=(40,0),sticky=N+S)
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=1,sticky=N+S)
        
        persons=cur.execute("select * from 'addressbook'").fetchall()
        count=0
        for person in persons:
            self.listbox.insert(count, str(person[0])+". "+str(person[1])+" "+str(person[2]))
            count +=1
        
        badd=Button(self.bottom,text='Add',width=12,font="Sans 14 bold",command=self.add_contacts)
        badd.grid(row=0,column=2,padx=50,pady=90,sticky=N)
        
        bupdate=Button(self.bottom,text='Update',width=12,font="Sans 14 bold",command=self.update_function)
        bupdate.grid(row=0,column=2,padx=50,pady=140,sticky=N)
        
        bdisplay=Button(self.bottom,text='View',width=12,font="Sans 14 bold",command=self.view_person)
        bdisplay.grid(row=0,column=2,padx=50,pady=190,sticky=N)
        
        bdelete=Button(self.bottom,text='Delete',width=12,font="Sans 14 bold",command=self.delete_person)
        bdelete.grid(row=0,column=2,padx=50,pady=240,sticky=N)
        
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
                    con.commit
                    messagebox.showinfo("Success","Deleted")
                    self.destroy()
                    
                except Exception as e:
                    messagebox.showinfo("Info",str(e))
        except:
            messagebox.showerror("Error","No Contact Selected")
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        