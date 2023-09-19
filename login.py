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
level = '0'
xp = '0'

def loginUser():

    def check_login():

        global loggedIn, entered_username, level, xp
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        #connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect("user_credentials.db")
        cursor = connection.cursor()

        #create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, level INTEGER DEFAULT 1, xp INTEGER DEFAULT 0)")

        #check if the user credentials are valid
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, entered_password))
        user = cursor.fetchone()

        if user is not None:
            loggedIn = entered_username
            level = user[2]  #index 2 corresponds to the level column in the database
            xp = user[3]     #index 3 corresponds to the xp column in the database
            messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        #close the database connection
        connection.close()

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

def levelXPDisplay():
    userLevel = myFont.render("Level: " + str(level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w / infoObject.current_w + 35, 300))

    userXp = myFont.render("Experience: " + str(xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w / infoObject.current_w + 35, 400))