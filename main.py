import pygame as py
import tkinter as tk
from tkinter import messagebox
import sqlite3
import threading
#from login import *
from backButton import *
from gameOver import *

py.init()

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 35)
myFontMedium = py.font.SysFont('Comic Sans MS', 24)
myFontSmall = py.font.SysFont('Comic Sans MS', 16)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

# fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.display.set_caption("Dodge em all")

# player info

loggedIn = 'null'
level = 1
xp = 0
xpToGo = 50
xpGainMultiplier = 1.2
currency = 0

width = 35
height = 35

pos_x = infoObject.current_w / 2
pos_y = infoObject.current_h / 2

velocity = 2.5

health = 250
realHealth = 100
realHealth = str(realHealth)
realHealthNum = int(realHealth)



# storm
alpha_value = 128
transparent_surface = py.Surface((infoObject.current_w, infoObject.current_h), py.SRCALPHA)
transparent_surface.set_alpha(alpha_value)
py.draw.rect(transparent_surface, (16, 6, 48, alpha_value), transparent_surface.get_rect())  # Cover the entire screen with transparency

stormSize = 800

durability = 250
realDurability = 500
realDurability = str(realDurability)
realDurabilityNum = int(realDurability)



ticks = 0  # To keep track of ticks



def loginUser():

    def check_login():

        global loggedIn, entered_username, level, xp, xpToGo, currency
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        #connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect("user_credentials.db")
        cursor = connection.cursor()

        #create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, level INTEGER DEFAULT 1, xp INTEGER DEFAULT 0, currency INTEGER DEFAULT 0)")

        #check if the user credentials are valid
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, entered_password))
        user = cursor.fetchone()

        if user is not None:
            loggedIn = entered_username
            level = user[2]  #index 2 corresponds to the level column in the database
            xp = user[3]     #index 3 corresponds to the xp column in the database
            xpToGo = user[4]
            currency = user[5]
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

def userBigDisplay():
    usern = myFontBig.render(" " + loggedIn, False, WHITE)
    win.blit(usern, (infoObject.current_w - 300, 110))



def healthBarBurner():
    global realDurability, realDurabilityNum

    decreaseDurability = realDurabilityNum * durability / 500
    py.draw.rect(win, (125, 125, 125), (20, 100, 250, 25))
    py.draw.rect(win, (255, 140, 0), (20, 100, decreaseDurability, 25))
    durabilityDisplay = myFontSmall.render(" | 500", False, WHITE)
    realDurabilityDisplay = myFontSmall.render(str(realDurabilityNum), False, WHITE)
    burner = myFontMedium.render("Burner", False, WHITE)
    win.blit(durabilityDisplay, (45, 100))
    win.blit(realDurabilityDisplay, (21, 100))
    win.blit(burner, (21, 70))

    if realDurabilityNum <= 0:
        run = False
        gameOver()

def healthBarPlayer():
    global realHealth, realHealthNum

    decreaseHealth = realHealthNum * health / 100
    py.draw.rect(win, (125, 125, 125), (20, 40, 250, 25))
    py.draw.rect(win, (0, 255, 0), (20, 40, decreaseHealth, 25))
    healthDisplay = myFontSmall.render(" | 100", False, WHITE)
    realHealthDisplay = myFontSmall.render(str(realHealthNum), False, WHITE)
    player = myFontMedium.render("" + loggedIn, False, WHITE)
    win.blit(healthDisplay, (45, 43))
    win.blit(realHealthDisplay, (21, 43))
    win.blit(player, (21, 10))

    if realHealthNum <= 0:
        run = False
        gameOver()



def levelUp():
    global xp, xpToGo, level, loggedIn, currency

    xp = int(xp)
    xpToGo = int(xpToGo)

    if xp >= xpToGo:
        initialXP = int(xpToGo * xpGainMultiplier)
        xpToGo = round(initialXP, -1)
        xp = 0
        level += 1
        currency += 20

        # Move database update to a separate thread
        def update_database():
            try:
                connection = sqlite3.connect("user_credentials.db")
                cursor = connection.cursor()

                cursor.execute("UPDATE users SET level=?, xp=?, xpToGo=?, currency=? WHERE username=?", (level, xp, xpToGo, currency, loggedIn))

                connection.commit()
                connection.close()
            except sqlite3.Error as e:
                print("SQLite error:", e)
            except Exception as ex:
                print("Error:", ex)

        # Create a new thread for database update
        db_update_thread = threading.Thread(target=update_database)
        db_update_thread.start()



def levelXPDisplay():
    global progressionW
    userLevel = myFont.render("Level: " + str(level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w / infoObject.current_w + 35, 300))

    userXp = myFont.render("Experience: " + str(xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w / infoObject.current_w + 35, 400))

    xpLimit = myFont.render("XP To Level Up: " + str(xpToGo), False, WHITE)
    win.blit(xpLimit, (infoObject.current_w / infoObject.current_w + 35, 485))

    progress = myFontMedium.render("Progress:", False, WHITE)
    win.blit(progress, (infoObject.current_w / infoObject.current_w + 35, 565))

    progressionW = int(xp) * 250 / int(xpToGo)
    py.draw.rect(win, (125, 125, 125), (infoObject.current_w / infoObject.current_w + 35, 600, 250, 15))
    py.draw.rect(win, (0, 255, 0), (infoObject.current_w / infoObject.current_w + 35, 600, progressionW, 15))


def currencyDisplay():
    usern = myFont.render("Eddies: " + str(currency), False, WHITE)
    win.blit(usern, (infoObject.current_w - 350, 100))



progressionW = int(xp) * 250 / int(xpToGo)

def levelXPDisplayInvert():
    userLevel = myFont.render("Level: " + str(level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w - 350, 300))

    userXp = myFont.render("Experience: " + str(xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w - 350, 400))

    xpLimit = myFont.render("XP To Level Up: " + str(xpToGo), False, WHITE)
    win.blit(xpLimit, (infoObject.current_w - 350, 485))

    progress = myFontMedium.render("Progress:", False, WHITE)
    win.blit(progress, (infoObject.current_w - 350, 565))

    py.draw.rect(win, (125, 125, 125), (infoObject.current_w - 350, 600, 250, 15))
    py.draw.rect(win, (0, 255, 0), (infoObject.current_w - 350, 600, progressionW, 15))

def ingameXpBar():
    global progressionW
    progressionW = int(xp) * 250 / int(xpToGo)  # Update progressionW based on current XP and XPToGo

    py.draw.rect(win, (125, 125, 125), (infoObject.current_w / 2.3, infoObject.current_h - 20, 250, 15))
    py.draw.rect(win, (0, 255, 0), (infoObject.current_w / 2.3, infoObject.current_h - 20, progressionW, 15))

    userLevel = myFontSmall.render("Level: " + str(level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w / 2.5, infoObject.current_h - 45))

    userXp = myFontSmall.render("Experience: " + str(xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w / 2.1, infoObject.current_h - 45))

    xpLimit = myFontSmall.render("/ " + str(xpToGo), False, WHITE)
    win.blit(xpLimit, (infoObject.current_w / 1.75, infoObject.current_h - 45))



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
                    cursor.execute("SELECT xp FROM users WHERE username=?", (loggedIn))
                    current_xp = cursor.fetchone()[0]

                    cursor.execute("SELECT currency FROM users WHERE username=?", (loggedIn))
                    current_currency = cursor.fetchone()[0]

                    # Only update the database if the xp has changed
                    if current_xp != xp:
                        # Update the user's xp in the database
                        cursor.execute("UPDATE users SET xp=? WHERE username=?", (xp, loggedIn))

                        # Commit the changes and close the database connection
                        connection.commit()
                        connection.close()
                        print("XP saved successfully.")

                    if current_currency != currency:
                        cursor.execute("UPDATE users SET currency=? WHERE username=?", (currency, loggedIn))

                        connection.commit()
                        connection.close()
                        print("currency saved successfully.")

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

def test2():
    global realHealth, realHealthNum
    keys = py.key.get_pressed()

    if keys[py.K_t]:
        realHealthNum = int(realHealth)
        realHealthNum -= 1
        realHealth = str(realHealthNum)

def test3():
    global stormSize
    keys = py.key.get_pressed()

    if keys[py.K_o]:
        stormSize -= 1

def test4():
    global stormSize
    keys = py.key.get_pressed()

    if keys[py.K_i]:
        stormSize += 1

def test5():
    global realDurability, realDurabilityNum
    keys = py.key.get_pressed()

    if keys[py.K_p]:
        realDurabilityNum = int(realDurability)
        realDurabilityNum += 1
        realDurability = str(realDurabilityNum)



run = True

def startGame():
    global pos_x, pos_y, run, ticks, realHealthNum, xp, stormSize, distance, realHealth, health, realDurabilityNum, realDurability
    initialStormSize = 800  # Initial stormSize value
    
    while run:
        py.time.delay(10)
        ticks += 1  # Increment ticks

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()

        if keys[py.K_LEFT] or keys[py.K_a] and pos_x > 0:
            pos_x -= velocity

        if keys[py.K_RIGHT] or keys[py.K_d] and pos_x < infoObject.current_w - width:
            pos_x += velocity

        if keys[py.K_UP] or keys[py.K_w] and pos_y > 0:
            pos_y -= velocity

        if keys[py.K_DOWN] or keys[py.K_s] and pos_y < infoObject.current_h - height:
            pos_y += velocity

        # Calculate the distance between the player and the center of the circle
        distance = ((infoObject.current_w // 2 - pos_x) ** 2 + (infoObject.current_h // 2 - pos_y) ** 2) ** 0.5

        win.fill((16, 6, 48))

        # Draw the transparent overlay
        win.blit(transparent_surface, (0, 0))

        # Calculate the adjusted stormSize based on durability
        adjustedStormSize = initialStormSize * (realDurabilityNum / 500)

        # Draw the storm (circle) with the adjusted size
        py.draw.circle(win, (53, 120, 2), (infoObject.current_w // 2, infoObject.current_h // 2), int(adjustedStormSize))

        py.draw.rect(win, (255, 0, 255), (pos_x, pos_y, width, height))

        if ticks % 7 == 0:
            realDurabilityNum -= 1
            realDurability = str(realDurabilityNum)

        # Check if the player is outside the green circle (double the radius) and 100 ticks have passed
        if distance > adjustedStormSize and ticks % 100 == 0:
            realHealthNum -= 5
            realHealth = str(realHealthNum)

        distance = ((infoObject.current_w // 2 - pos_x) ** 2 + (infoObject.current_h // 2 - pos_y) ** 2) ** 0.5

        # Check if the player is inside the circle
        if distance < adjustedStormSize:
            if realHealthNum < 100 and ticks % 30 == 0:
                realHealthNum += 1
                realHealth = str(realHealthNum)

        if ticks % 35 == 0:
            xp += 1

        test()
        ingameXpBar()
        levelUp()
        healthBarPlayer()
        test2()
        back()
        test3()
        test4()
        healthBarBurner()
        test5()

        py.display.update()

    py.quit()

if __name__ == "__main__":
    startGame()
