#importing all required modules
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from CustomTkinter import customtkinter
import sqlite3
from addcontacts import AddContacts
from updatecontacts import Update
from view import View

#setting theme for our aplicaton
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#connecting with database and creating table
con=sqlite3.connect('mycontacts.db')
cur=con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS addressbook (person_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, person_name TEXT, person_surname TEXT, person_email TEXT, person_phone INTEGER, person_address TEXT)")

#using Toplevel to create new window
class MyContacts(customtkinter.CTkToplevel):
    def __init__(self):
        customtkinter.CTkToplevel.__init__(self)

        #setting size and position of app in main window
        self.geometry("650x550+300+110")
        self.title("DPS Joka Students Presents")
        self.resizable(False,False)

        #creating and resizing required images
        self.top_img=ImageTk.PhotoImage(Image.open("all/people2.png"))
        self.add_img=ImageTk.PhotoImage(Image.open("all/add3.png").resize((20,20), Image.Resampling.LANCZOS))
        self.update_img=ImageTk.PhotoImage(Image.open("all/edit1.png").resize((20,20), Image.Resampling.LANCZOS))
        self.view_img=ImageTk.PhotoImage(Image.open("all/view.png").resize((20,20), Image.Resampling.LANCZOS))
        self.delete_img=ImageTk.PhotoImage(Image.open("all/delete.png").resize((20,20), Image.Resampling.LANCZOS))

        #creating frames
        self.top=customtkinter.CTkFrame(self,height=150,width=595, corner_radius=10, border_width=5,border_color='#08111c')
        self.top.place(x=30,y=10)
        
        self.bottom=customtkinter.CTkFrame(self,height=365,width=407,border_width=5,border_color='#08111c',corner_radius=10)
        self.bottom.place(x=30,y=170)

        self.bottomright=customtkinter.CTkFrame(self,height=365,width=175,border_width=5,border_color='#08111c',corner_radius=10)
        self.bottomright.place(x=450,y=170)

        #creating heading and top image
        self.top_image_label=Label(self.top,image=self.top_img,bg='#292929')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=customtkinter.CTkLabel(self.top,text="My Contacts",text_font='arial 18 bold',bg_color='#292929',fg_color='#292929')
        self.heading.place(x=270,y=53)
        
        #creating searchbar
        self.searchbar=customtkinter.CTkEntry(self.bottom, text_font='Helvetica 10',width=350,bg_color='grey', fg_color='black',corner_radius=5, placeholder_text="Search Here")
        self.searchbar.place(x=15,y=10)

        #creating and placing listbox and scrollbar
        self.scroll=customtkinter.CTkScrollbar(self.bottom,orientation=VERTICAL,width=20,height=290,corner_radius=10,fg_color='silver',scrollbar_hover_color='#470e07',scrollbar_color='brown',highlightthickness=0)
        self.listbox=Listbox(self.bottom,width=50,height=17,font="Helvetica 10 bold",bd=0,bg='dark grey')
        self.listbox.place(x=15,y=50)
        self.scroll.configure(command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.place(x=370,y=50)

        #binding searchbar and listbox
        self.searchbar.bind("<KeyRelease>", self.check)
        self.listbox.bind("<<ListboxSelect>>", self.fillout)

        #keeping some default data in listbox
        trial=cur.execute("select * from 'addressbook'").fetchall()
        if len(trial)==0:
            con.execute("INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)",('Police',' ','kolkatapolice@gmail.com',100,"India"));
            con.commit()
            con.execute("INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)",('Fire','Brigade','kolkatafire@gmail.com',101,"India"))
            con.commit()
            con.execute("INSERT INTO addressbook (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)",('Ambulance',' ','kolkataambulance@gmail.com',102,"India"))
            con.commit()

        #showing contacts present in database
        persons=cur.execute("select * from 'addressbook'").fetchall()
        for person in persons:
            count=person[0]
            self.listbox.insert(count, str(person[0])+". "+str(person[1])+" "+str(person[2]))
            count +=person[0]

        #creating and defining functions for buttons
        self.badd=customtkinter.CTkButton(self.bottomright,text=' Add  ',width=12,text_font="Sans 14 bold",image=self.add_img,command=self.add_contacts,corner_radius=5)
        self.badd.place(x=40,y=70)
        
        self.bupdate=customtkinter.CTkButton(self.bottomright,text=' Edit  ',width=12,text_font="Sans 14 bold",image=self.update_img,command=self.update_function,corner_radius=5)
        self.bupdate.place(x=40,y=130)
        #disabling buttons if no contact is selected
        if self.listbox.curselection()==():
            self.bupdate.configure(state=DISABLED)
        
        self.bdisplay=customtkinter.CTkButton(self.bottomright,text='View  ',width=12,text_font="Sans 14 bold",image=self.view_img,command=self.view_person,corner_radius=5)
        self.bdisplay.place(x=40,y=190)
        #disabling buttons if no contact is selected
        if self.listbox.curselection()==():
            self.bdisplay.configure(state=DISABLED)
        
        self.bdelete=customtkinter.CTkButton(self.bottomright,text='Delete',width=12,text_font="Sans 14 bold",image=self.delete_img,command=self.delete_person,corner_radius=5)
        self.bdelete.place(x=40,y=250)
        #disabling buttons if no contact is selected
        if self.listbox.curselection()==():
            self.bdelete.configure(state=DISABLED)

    #funtion for adding contacts
    def add_contacts(self):
        add_page=AddContacts()
        self.destroy()

    #funtion for updating contacts
    def update_function(self):
        try:
            #recoring data of selected contact
            selected_item=self.listbox.curselection()
            person=self.listbox.get(selected_item)
            person_id=person.split(".")[0]
            
            updatepage=Update(person_id)
            self.destroy()
        except Exception as e:
                    messagebox.showinfo("Info",str(e))

    #funtion for viewing contacts
    def view_person(self):
        try:
            #recoring data of selected contact
            selected_item=self.listbox.curselection()
            person=self.listbox.get(selected_item)
            person_id=person.split(".")[0]
            
            viewpage=View(person_id)
            self.destroy()
        except Exception as e:
                    messagebox.showinfo("Info",str(e))

    #funtion for deleting contacts
    def delete_person(self):
        try:
            #selecting contact to delete
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

    #filling searchbar with name of selected contact
    def fillout(self,e):
        self.searchbar.delete(0, END)
        selected_item=self.listbox.curselection()
        person=self.listbox.get(selected_item)
        self.searchbar.insert(0, str(person.split(".")[1]))
        
        #making buttons functionable
        self.bupdate.configure(state=NORMAL)
        self.bdisplay.configure(state=NORMAL)
        self.bdelete.configure(state=NORMAL)

    #function to search persons using binding
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
            
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
