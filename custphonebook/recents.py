#importing all required modules
from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image
from CustomTkinter import customtkinter

#setting theme for our aplicaton
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#connecting with database and creating table
con=sqlite3.connect('myrecents.db')
cur=con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS recents (number_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, number INTEGER, day TEXT, time INTEGER)")

#using Toplevel to create new window
class Recents(customtkinter.CTkToplevel):
    def __init__(self):
        customtkinter.CTkToplevel.__init__(self)

        #setting size and position of app in main window
        self.geometry("650x550+300+110")
        self.title("DPS Joka Students Presents")
        self.resizable(False,False)

        #creating and resizing required images
        self.top_img=ImageTk.PhotoImage(Image.open("all/recents2.png").resize((100,100), Image.Resampling.LANCZOS))
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
        
        self.heading=customtkinter.CTkLabel(self.top,text="Recents",text_font='arial 18 bold',bg_color='#292929',fg_color='#292929')
        self.heading.place(x=270,y=57)

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
        self.listbox.bind("<<ListboxSelect>>", self.fillout)
        self.searchbar.bind("<KeyRelease>", self.check)

        #creating and defining functions for buttons
        self.bdelete=customtkinter.CTkButton(self.bottomright,text='Delete',width=12,text_font="Sans 16 bold",image=self.delete_img,command=self.delete_person,corner_radius=5)
        self.bdelete.place(x=40,y=170)
        #disabling buttons if no number is selected
        if self.listbox.curselection()==():
            self.bdelete.configure(state=DISABLED)

        #showing reviously made calls
        numbers=cur.execute("select * from 'recents'").fetchall()
        count=0
        for number in numbers:
            self.listbox.insert(count, str(number[0])+". "+str(number[1])+"  , "+str(number[2]+"  , "+str(number[3])))
            count +=1

    #funtion for deleting contacts
    def delete_person(self):
        try:
            #selecting contact to delete
            selected_item=self.listbox.curselection()
            number=self.listbox.get(selected_item)
            number_id=number.split(".")[0]
            
            query="delete from recents where number_id = {}".format(number_id)
            answer=messagebox.askquestion("Warning","Do you really want to delete")
            if answer=='yes':
                try:
                    cur.execute(query)
                    con.commit
                    messagebox.showinfo("Success","Deleted")
                    self.destroy()
                    
                except Exception as e:
                    messagebox.showinfo("Info",str(e))
        except:
            messagebox.showerror("Error","No number selected")

    #making buttons functionable
    def fillout(self,e):
        self.bdelete.configure(state=NORMAL)

    #function to search persons using binding
    def check(self,e):
        typed=self.searchbar.get()
        if typed=='':
            self.listbox.delete(0, END)
            numbers=cur.execute("select * from 'recents'").fetchall()
            for number in numbers:
                count=number[0]
                self.listbox.insert(count, str(number[0])+". "+str(number[1])+" "+str(number[2]))
                count +=number[0]
        else:
            self.listbox.delete(0, END)
            numbers=cur.execute("SELECT * FROM recents WHERE number LIKE ?", ('%' + str(typed) + '%',))
            for number in numbers:
                record=number[0]
                self.listbox.insert(record, str(number[0])+". "+str(number[1])+" "+str(number[2]))
                record +=number[0]
        
        
        
        
        
        
        
