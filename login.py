import tkinter as tk
from tkinter import messagebox
import sqlite3
import pygame as py

py.init()

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 35)

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

WHITE = (255, 255, 255)

loggedIn = 'null'

def loginUser():

    def check_login():

        global loggedIn, entered_username
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        #connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect("user_credentials.db")
        cursor = connection.cursor()

        #create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        #check if the user credentials are valid
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, entered_password))
        user = cursor.fetchone()

        #close the database connection
        connection.close()

        if user is not None:
            messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
            loggedIn = entered_username

        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    root = tk.Tk()

    root.title("Login and Registration Form")

    #username label and entry field
    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    #password label and entry field
    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    #login button
    login_button = tk.Button(root, text="Login", command=check_login)
    login_button.pack()

    root.mainloop()

def userDisplay():
    usern = myFont.render("Logged in as: " + loggedIn, False, WHITE)
    win.blit(usern, (infoObject.current_w - 350, 35))