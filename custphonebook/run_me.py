#importing all required modules
from tkinter import*
from PIL import ImageTk,Image
import datetime
from CustomTkinter import customtkinter
from mykeypad import MyKeypad
from mycontacts import MyContacts
from addcontacts import AddContacts
from aboutus import About
from recents import Recents

#using today's date
date=datetime.datetime.now().date()
date=str(date)

#setting theme for our aplicaton
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#using class for runing our application
class Application(object):
    def __init__(self,master):
        self.master=master
        
        #creating and resizing required images
        self.about_img=ImageTk.PhotoImage(Image.open("all/about.png").resize((25,25), Image.Resampling.LANCZOS))
        self.call_img=ImageTk.PhotoImage(Image.open("all/call.png").resize((25,25), Image.Resampling.LANCZOS))
        self.recents_img=ImageTk.PhotoImage(Image.open("all/recents.png").resize((25,25), Image.Resampling.LANCZOS))
        self.contacts_img=ImageTk.PhotoImage(Image.open("all/contacts.png").resize((25,25), Image.Resampling.LANCZOS))
        self.top_img=ImageTk.PhotoImage(Image.open("all/phonebook1.png"))

        #creating frames
        self.top=customtkinter.CTkFrame(master,height=130,width=600, corner_radius=10, border_width=5,border_color='#08111c')
        self.top.pack(pady=10)
        
        self.bottom=customtkinter.CTkFrame(master,height=450,width=600,border_width=5,border_color='#08111c')
        self.bottom.pack(pady=10)
        
        #creating heading and top image
        self.top_image_label=Label(self.top,image=self.top_img,bg='#292929')
        self.top_image_label.place(x=130,y=20)
        
        self.heading=customtkinter.CTkLabel(self.top,text="My PhoneBook",text_font='arial 18 bold',fg_color='#292929')
        self.heading.place(x=230,y=50)

        #placing today's date
        self.date_lbl=customtkinter.CTkLabel(self.top,text="Today's Date: "+date,text_font='arial 12 bold',fg_color='#292929')
        self.date_lbl.place(x=400,y=95)

        #creating and placing buttons
        self.contactsbutton=customtkinter.CTkButton(self.bottom,text='My Contacts',text_font='arial 14 bold',height=20,image=self.contacts_img,command=self.my_contacts,corner_radius=5)
        self.contactsbutton.place(x=350,y=100)

        self.aboutbutton=customtkinter.CTkButton(self.bottom,text='About Us ',text_font='arial 17 bold',height=10,image=self.about_img,command=self.about_us,corner_radius=5)
        self.aboutbutton.place(x=350,y=210)
        
        self.keypadbutton=customtkinter.CTkButton(self.bottom,text=' Keypad  ',text_font='arial 17 bold',height=10,image=self.call_img,command=self.keypad,corner_radius=5)
        self.keypadbutton.place(x=145,y=100)
        
        self.recentsbutton=customtkinter.CTkButton(self.bottom,text='Recents ',text_font='arial 17 bold',height=10,image=self.recents_img,command=self.recents,corner_radius=5)
        self.recentsbutton.place(x=145,y=210)

    #setting modules
    def my_contacts(self):
        people=MyContacts()
        
    def about_us(self):
        aboutpage=About()
        
    def keypad(self):
        keypadpage=MyKeypad()
        
    def recents(self):
        recentspage=Recents()

#defining main function
def main():
    root=customtkinter.CTk()
    app=Application(root)
    #setting size and position of app in main window
    root.geometry("650x550+300+110")
    root.resizable(False,False)
    root.title("DPS Joka Students Presents")
    root.mainloop()
    
if __name__=='__main__':
    main()





