#importing all required modules
from tkinter import*
from PIL import ImageTk,Image
from CustomTkinter import customtkinter

#setting theme for our aplicaton
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#using Toplevel to create new window
class About(customtkinter.CTkToplevel):
    def __init__(self):
        customtkinter.CTkToplevel.__init__(self)

        #setting size and position of app in main window
        self.geometry("650x550+300+110")
        self.title("DPS Joka Students Presents")
        self.resizable(False,False)

        #creating and resizing required images
        self.top_img=ImageTk.PhotoImage(Image.open("all/question.png").resize((100,100), Image.Resampling.LANCZOS))

        #creating frames
        self.top=customtkinter.CTkFrame(self,height=130,width=600, corner_radius=10, border_width=5,border_color='#08111c')
        self.top.pack(pady=10)
        
        self.bottom=customtkinter.CTkFrame(self,height=450,width=600,border_width=5,border_color='#08111c')
        self.bottom.pack(pady=10)

        #creating heading and top image
        self.top_image_label=Label(self.top,image=self.top_img,bg='#292929')
        self.top_image_label.place(x=130,y=18)

        self.heading=customtkinter.CTkLabel(self.top,text="About Us",text_font='arial 18 bold',fg_color='#292929')
        self.heading.place(x=230,y=50)

        #placing, creating label and writing inormation about us
        self.text=customtkinter.CTkLabel(self.bottom,text_font='arial 14 bold',text='Hey this is About Us page'
                        '\n This application is made for educational purpose.'
                        '\n It is made by the students of'
                        '\n Delhi Public School, Joka.'
                        '\n The creators are'
                        '\n Priyangshu Saha, Shuvam Kayal, Sivanch Shivam Singh,'
                        '\n Hitanshu Chocharia, and Angshumoy Nandi.'
                        '\n along with our teacher Kushal Kumar Roy Sir'
                        '\n who guided us and gave us this golden opportunity.'
                        '\n In this assignment we learnt many new functions such as'
                        '\n working with Tkinter, Classes, as well as many widgets.'
                        '\n Thank You.'
                        )
        self.text.place(x=35,y=50)
        
        
        

        
        
        
        
