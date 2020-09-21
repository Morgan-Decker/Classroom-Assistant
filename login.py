#Thank you to likegeeks for the Tkinter basics
from tkinter import *
import time
import sys
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        load = Image.open("cover.jpg")
        render = ImageTk.PhotoImage(load)
        pic = Label(self, image=render)
        pic.image = render
        pic.place(x=100, y=0)
        
        text = Label(self, text="Hello! Press \"Log in\" to scan your QR code")
        text.pack()
        #Title of master wigit
        self.master.title("LOGIN")
        #Takes full space of the wigit window
        self.pack(fill=BOTH, expand=1)
        #Creating a menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        #create a drop_menu object
        drop_menu = Menu(menu)

        #adds command to menu, calling it exit
        drop_menu.add_command(label="Exit", command=self.client_exit)

        #add "drop_menu" to our menu
        menu.add_cascade(label="Options", menu=drop_menu)

        
        #Creating a button instance
        button_login = Button(self, text="Login", command=self.login)
        #placing the button on the window
        button_login.place(x=0, y=0)
    def login(self):
        login_menu.destroy()
        return "This is to end the login program"
        
        
    def client_exit(self):
        exit()

login_menu = Tk()
#size of window
login_menu.geometry("400x300")

app = Window(login_menu)
login_menu.mainloop()
