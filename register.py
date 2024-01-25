import tkinter
from tkinter import messagebox
import customtkinter as tk
import sqlite3
import hashlib

def registerUser():

    #function to register a new user and store their information in the database
    def register_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        hashed_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()

        #if both fields are empty, show an error message and return without writing to the database
        if not new_username or not new_password:
            messagebox.showerror("Registration Failed", "Username and Password fields are empty.")
            return

        #connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect("user_credentials.db")
        cursor = connection.cursor()

        #create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, level INTEGER DEFAULT 1, xp INTEGER DEFAULT 0, "
                       "xpToGo INTEGER DEFAULT 50, currency INTEGER DEFAULT 0, isAdmin INTEGER DEFAULT 0, red INTEGER DEFAULT 0, white "
                       "INTEGER DEFAULT 0, orange INTEGER DEFAULT 0)")

        #check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        else:
            #insert the new user's information into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, hashed_password))
            connection.commit()
            connection.close()
            messagebox.showinfo("Registration Successful", "Account created successfully!")

            #clear the registration entry fields after successful registration
            new_username_entry.delete(0, tk.END)
            new_password_entry.delete(0, tk.END)

    #create the main window
    root = tk.CTk()
    root.title("Registration Form")
    root.geometry("500x350")

    frame = tk.CTkFrame(master=root)
    frame.pack(padx = 60, pady = 20, fill = "both", expand = True)

    #registration Section
    register_label = tk.CTkLabel(master=frame, text="Register")
    register_label.pack(padx = 10, pady = 12)

    #new username label and entry field
    new_username_label = tk.CTkLabel(master=frame, text="New Username:")
    new_username_label.pack()
    new_username_entry = tk.CTkEntry(master=frame, placeholder_text="Username")
    new_username_entry.pack(padx = 10, pady = 12)

    #new password label and entry field
    new_password_label = tk.CTkLabel(master=frame, text="New Password:")
    new_password_label.pack()
    new_password_entry = tk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    new_password_entry.pack(padx = 10, pady = 12)

    #register button
    register_button = tk.CTkButton(master=frame, text="Register", command=register_user)
    register_button.pack(padx = 10, pady = 12)

    #run the main loop
    root.mainloop()