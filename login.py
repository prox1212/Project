import tkinter as tk
from tkinter import messagebox
import sqlite3
import pygame as py

py.init()

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 35)
myFontSmall = py.font.SysFont('Comic Sans MS', 16)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

WHITE = (255, 255, 255)

loggedIn = 'null'
level = '0'
xp = '0'
xpToGo = '50'
progressionW = '0'

def loginUser():

    def check_login():

        global loggedIn, entered_username, level, xp, xpToGo
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
            xpToGo = user[4]
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

def levelUp():
    global xp, xpToGo, level, loggedIn

    # Convert xp and xpToGo to integers
    xp = int(xp)
    xpToGo = int(xpToGo)

    if xp >= xpToGo:
        xpToGo = int(xpToGo * 1.25)
        xp = 0
        level += 1

        try:
            # Connect to the database
            connection = sqlite3.connect("user_credentials.db")
            cursor = connection.cursor()

            # Update the user's level and xp in the database
            cursor.execute("UPDATE users SET level=?, xp=?, xpToGo=? WHERE username=?", (level, xp, xpToGo, loggedIn))

            # Commit the changes and close the database connection
            connection.commit()
            connection.close()
        except sqlite3.Error as e:
            print("SQLite error:", e)
        except Exception as ex:
            print("Error:", ex)

def levelXPDisplay():
    global progressionW
    userLevel = myFont.render("Level: " + str(level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w / infoObject.current_w + 35, 300))

    userXp = myFont.render("Experience: " + str(xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w / infoObject.current_w + 35, 400))

    xpLimit = myFont.render("/ " + str(xpToGo), False, WHITE)
    win.blit(xpLimit, (infoObject.current_w / infoObject.current_w + 35, 445))

    progressionW = int(xp) * 250 / int(xpToGo)
    py.draw.rect(win, (125, 125, 125), (infoObject.current_w / infoObject.current_w + 35, 550, 250, 15))
    py.draw.rect(win, (0, 255, 0), (infoObject.current_w / infoObject.current_w + 35, 550, progressionW, 15))

def ingameXpBar():
    progressionW2 = int(xp) * 250 / int(xpToGo)
    py.draw.rect(win, (125, 125, 125), (infoObject.current_w / infoObject.current_w + 35, infoObject.current_h - 20, 250, 15))
    py.draw.rect(win, (0, 255, 0), (infoObject.current_w / infoObject.current_w + 35, infoObject.current_h - 20, progressionW2, 15))

    userLevel = myFontSmall.render("Level: " + str(level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w / infoObject.current_w + 15, infoObject.current_h - 45))

    userXp = myFontSmall.render("Experience: " + str(xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w / infoObject.current_w + 95, infoObject.current_h - 45))

    xpLimit = myFontSmall.render("/ " + str(xpToGo), False, WHITE)
    win.blit(xpLimit, (infoObject.current_w / infoObject.current_w + 240, infoObject.current_h - 45))

def save():
    global loggedIn, level, xp, xpToGo

    mousePos = py.mouse.get_pos()

    saveTop = infoObject.current_h / infoObject.current_h + 150
    saveLeft = infoObject.current_w / infoObject.current_w + 35
    saveBottom = infoObject.current_h / infoObject.current_w + 35 + 70
    saveRight = infoObject.current_w / infoObject.current_w + 35 + 200

    py.draw.rect(win, (255, 0, 0), (infoObject.current_w / infoObject.current_w + 35, infoObject.current_h / infoObject.current_h + 150, 200, 70))
    save = myFontBig.render("Save", False, WHITE)
    win.blit(save, (infoObject.current_w / infoObject.current_w + 80, infoObject.current_h / infoObject.current_h + 150))

    if py.mouse.get_pressed()[0]:
        if saveLeft <= mousePos[0] <= saveRight and saveTop <= mousePos[1] <= saveBottom:
            if loggedIn != 'null':
                try:
                    # Connect to the database
                    connection = sqlite3.connect("user_credentials.db")
                    cursor = connection.cursor()

                    # Get the user's current xp from the database
                    cursor.execute("SELECT xp FROM users WHERE username=?", (loggedIn,))
                    current_xp = cursor.fetchone()[0]

                    # Only update the database if the xp has changed
                    if current_xp != xp:
                        # Update the user's xp in the database
                        cursor.execute("UPDATE users SET xp=? WHERE username=?", (xp, loggedIn))

                        # Commit the changes and close the database connection
                        connection.commit()
                        connection.close()
                        print("XP saved successfully.")
                    else:
                        print("XP is unchanged. No update needed.")
                except sqlite3.Error as e:
                    print("SQLite error:", e)
                except Exception as ex:
                    print("Error:", ex)

def test():
    global xp
    keys = py.key.get_pressed()

    if keys[py.K_r]:
        xp += 1