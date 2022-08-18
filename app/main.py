from tkinter import*
from PIL import ImageTk,Image
import datetime
from mykeypad import MyKeypad
from mycontacts import MyContacts
from addcontacts import AddContacts
from aboutus import About
from recents import Recents


date=datetime.datetime.now().date()
date=str(date)


class Application(object):
    def __init__(self,master):
        self.master=master
        
        self.top=Frame(master,height=150,bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(master,height=500,bg='#4b42f5')
        self.bottom.pack(fill=X)
        
        self.top_img=ImageTk.PhotoImage(Image.open("phonebook1.png"))
        self.top_image_label=Label(self.top,image=self.top_img,bg='white')
        self.top_image_label.place(x=130,y=20)
        
        self.heading=Label(self.top,text="My PhoneBook",font='arial 15 bold',bg='white',fg='#eb8034')
        self.heading.place(x=230,y=50)
        
        self.date_lbl=Label(self.top,text="Today's Date: "+date,font='arial 12 bold',bg='white',fg='#eb8034')
        self.date_lbl.place(x=450,y=120)
        
        self.viewbutton=Button(self.bottom,text='My Contacts',font='arial 15 bold',fg='#4b42f5',command=self.my_contacts)
        self.viewbutton.place(x=365,y=70)
        
        self.addbutton=Button(self.bottom,text=' Add Contact',font='arial 15 bold',fg='#4b42f5',command=self.addcontactsfunction)
        self.addbutton.place(x=365,y=140)
        
        self.aboutbutton=Button(self.bottom,text='   About Us  ',font='arial 15 bold',fg='#4b42f5',command=self.about_us)
        self.aboutbutton.place(x=265,y=210)
        
        self.keypadbutton=Button(self.bottom,text='    Keypad   ',font='arial 15 bold',fg='#4b42f5',command=self.keypad)
        self.keypadbutton.place(x=160,y=70)
        
        self.recentsbutton=Button(self.bottom,text='    Recents  ',font='arial 15 bold',fg='#4b42f5',command=self.recents)
        self.recentsbutton.place(x=160,y=140)
        
    def my_contacts(self):
        people=MyContacts()
        
    def addcontactsfunction(self):
        addpeoplewindow=AddContacts()
        
    def about_us(self):
        aboutpage=About()
        
    def keypad(self):
        keypadpage=MyKeypad()
        
    def recents(self):
        recentspage=Recents()

def main():
    root=Tk()
    app=Application(root)
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()
    
if __name__=='__main__':
    main()





