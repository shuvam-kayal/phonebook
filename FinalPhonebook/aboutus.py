from tkinter import*
from PIL import ImageTk,Image


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("550x550+550+200")
        self.title("About Us")
        self.resizable(False,False)
    
        self.top=Frame(self,height=550,width=550,bg='#eb4634')
        self.top.pack(fill=BOTH)
        
        self.text=Label(self.top,bg='#eb4634',font='arial 10 bold',text="Hey this is About Us page"
                        '\n This application is made for educational purpose.'
                        '\n This application is made by the students of'
                        '\n Delhi Public School, Joka.'
                        '\n The creators are'
                        '\n Priyangshu Saha, Shuvam Kayal, Sivanch Shivam Singh,'
                        '\n Hitanshu Chocharia, and Angshumoy Nandi.'
                        '\n along with our teacher Kushal Kumar Roy Sir who gave us this golden opportunity.'
                        '\n In this assignment we learnt many new functions such as'
                        '\n working with Tkinter, Classes, as well as many widget.'
                        '\n Thank You.'
                        )
        self.text.place(x=10,y=150)
        
        
        

        
        
        
        