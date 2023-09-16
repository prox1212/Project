import tkinter as tk
from tkinter import messagebox
import sqlite3

def registerUser():
#function to validate login credentials from the database

    # def check_login():
    #     global loggedIn, entered_username
    #     entered_username = username_entry.get()
    #     entered_password = password_entry.get()

    #     #connect to the database (or create it if it doesn't exist)
    #     connection = sqlite3.connect("user_credentials.db")
    #     cursor = connection.cursor()

    #     #create the table if it doesn't exist
    #     cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

    #     #check if the user credentials are valid
    #     cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, entered_password))
    #     user = cursor.fetchone()

    #     #close the database connection
    #     connection.close()

    #     if user is not None:
    #         messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    #         loggedIn = entered_username

    #     else:
    #         messagebox.showerror("Login Failed", "Invalid username or password.")

    #function to register a new user and store their information in the database
    def register_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        #if both fields are empty, show an error message and return without writing to the database
        if not new_username and not new_password:
            messagebox.showerror("Registration Failed", "Both Username and Password fields are empty.")
            return

        #connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect("user_credentials.db")
        cursor = connection.cursor()

        #create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        #check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        else:
            #insert the new user's information into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            connection.commit()
            connection.close()
            messagebox.showinfo("Registration Successful", "Account created successfully!")

            #clear the registration entry fields after successful registration
            new_username_entry.delete(0, tk.END)
            new_password_entry.delete(0, tk.END)

    #create the main window
    root = tk.Tk()
    root.title("Login and Registration Form")

    # #username label and entry field
    # username_label = tk.Label(root, text="Username:")
    # username_label.pack()
    # username_entry = tk.Entry(root)
    # username_entry.pack()

    # #password label and entry field
    # password_label = tk.Label(root, text="Password:")
    # password_label.pack()
    # password_entry = tk.Entry(root, show="*")
    # password_entry.pack()

    # #login button
    # login_button = tk.Button(root, text="Login", command=check_login)
    # login_button.pack()

    #registration Section
    register_label = tk.Label(root, text="--- Register ---")
    register_label.pack()

    #new username label and entry field
    new_username_label = tk.Label(root, text="New Username:")
    new_username_label.pack()
    new_username_entry = tk.Entry(root)
    new_username_entry.pack()

    #new password label and entry field
    new_password_label = tk.Label(root, text="New Password:")
    new_password_label.pack()
    new_password_entry = tk.Entry(root, show="*")
    new_password_entry.pack()

    #register button
    register_button = tk.Button(root, text="Register", command=register_user)
    register_button.pack()

    #run the main loop
    root.mainloop()