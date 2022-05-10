# cardano wallet app UI

import tkinter
from tkinter import messagebox, scrolledtext, Toplevel
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import CHECKBUTTON
import customtkinter as ctk

import os, sys
import time
import datetime as datetime
import json
import csv
import psycopg2
from PIL import Image, ImageTk

# UI theming configuration
ctk.set_appearance_mode("gray40")
ctk.set_default_color_theme("green")


# KYC
class Auth:

    # windows dimentions
    WINDOW_HEIGHT = "500"
    WINDOW_WIDTH = "480"

    # window initilization
    win = ctk.CTk()
    win.geometry(WINDOW_HEIGHT + "x" + WINDOW_WIDTH)
    win.title("Wallet")
    win.resizable(False, False)
    
    # y-axis padding
    Y_PADDING= 13

    # placing the app's logo in the welcome screen
    logo = Image.open("C:/Users/shad/Desktop/wallet/Images/wallet-icon-3.png")
    logo_image = ImageTk.PhotoImage(logo)

    welcome_logo = tkinter.Label(image=logo_image)
    welcome_logo = logo_image


    def __init__(self):
        
        # user signup / sign in authentication andverification
        self.choice = self.user_choice()


        self.choice
    
    # home
    def home(self):
        print("home page")

    
    # registering the new user
    def save_new_user(self):
        
        print("registered new user")

    # sing up pop
    def sign_up(self):
        # top levelp for the sign up
        self.signUp_window = ctk.CTkToplevel(self.win)
        self.signUp_window.geometry("400x400")
        self.signUp_window.title("New User Sign_up")

        # welcome text
        self.welcome = ctk.CTkLabel(self.signUp_window, text="Welcome to Trace")
        self.welcome.place(x=120, y=20)

        # create label on CTkToplevel window
        self.username = ctk.CTkLabel(self.signUp_window, text="username")
        self.username.place(x=50, y=80)

        # username entry
        self.new_username = ctk.CTkEntry(self.signUp_window)
        self.new_username.place(x=150, y=80)

        # create label on CTkToplevel window
        self.password = ctk.CTkLabel(self.signUp_window, text="password")
        self.password.place(x=50, y=140)

        # password entry
        self.new_password = ctk.CTkEntry(self.signUp_window, show='*')
        self.new_password.place(x=150, y=140)

        # sign up the new user
        self.signup = ctk.CTkButton(master=self.signUp_window, text="SIGN UP", command=self.save_new_user)
        self.signup.place(x=140, y=200)
    
    # sign in pop
    def sign_in(self):

        # top levelp for the sign up
        self.signIn_window = ctk.CTkToplevel(self.win)
        self.signIn_window.geometry("400x400")
        self.signIn_window.title("New User Sign_up")

        # welcome text
        self.welcome = ctk.CTkLabel(self.signIn_window, text="We miss you", fg="blue")
        self.welcome.place(x=120, y=20)

        # create label on CTkToplevel window
        self.username = ctk.CTkLabel(self.signIn_window, text="username")
        self.username.place(x=50, y=80)

        # username entry
        self._username = ctk.CTkEntry(self.signIn_window)
        self._username.place(x=150, y=80)

        # create label on CTkToplevel window
        self.password = ctk.CTkLabel(self.signIn_window, text="password")
        self.password.place(x=50, y=140)

        # password entry
        self.user_password = ctk.CTkEntry(self.signIn_window, show='*')
        self.user_password.place(x=150, y=140)

        # sign up the new user
        self.signIn = ctk.CTkButton(master=self.signIn_window, text="SIGN UP", command=self.home)
        self.signIn.place(x=140, y=200)

    # sign up and sign in prompts
    def user_choice(self):

        # welcome text
        self.welcome = ctk.CTkLabel(self.win, text="Welcome to Trace")
        self.welcome.place(x=180, y=100)

        # sign up prompt
        self.signup = ctk.CTkButton(master=self.win, text="SIGN UP", command=self.sign_up)
        self.signup.place(x=180, y=200)

        # sign in prompt
        self.signin = ctk.CTkButton(master=self.win, text="SIGN IN", command=self.sign_in)
        self.signin.place(x=180, y=250)



    # initilizing the runner
    def run(self):
        self.win.mainloop()


# running the app
if __name__ == "__main__":
    auth = Auth()
    auth.run()