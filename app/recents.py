from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image

con=sqlite3.connect('recents_backup2.db')
cur=con.cursor()

class Recents(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x650+600+200")
        self.title("Recents")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(self,height=500,bg='#15c235')
        self.bottom.pack(fill=X)
        
        self.top_img=ImageTk.PhotoImage(Image.open("recents_img.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='white')
        self.top_image_label.place(x=150,y=20)
        
        self.heading=Label(self.top,text="Recents",font='arial 15 bold',bg='white',fg='#eb8034')
        self.heading.place(x=270,y=51)
        
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        
        self.listbox=Listbox(self.bottom,width=50,height=27,font="Helvetica 10 bold")
        self.listbox.grid(row=0,column=0,padx=(40,0),sticky=N+S)
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=1,sticky=N+S)
        
        bdelete=Button(self.bottom,text='Delete',width=12,font="Sans 12 bold",command=self.delete_person)
        bdelete.grid(row=0,column=2,padx=50,pady=240,sticky=N)
        
        numbers=cur.execute("select * from 'recents'").fetchall()
        count=0
        for number in numbers:
            self.listbox.insert(count, str(number[0])+". "+str(number[1])+"  , "+str(number[2]+"  , "+str(number[3])))
            count +=1
            
    def delete_person(self):
        try:
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
        
        
        
        
        
        
        