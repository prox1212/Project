import pygame as py
from main import *
from instructions import *
from register import *
from leaderboard import *
#from login import *
from vars import *

py.init()

#fullscreen
infoObject = py.display.Info()

py.display.set_caption("Fight the Storm")

#<MENU>
buttonWidth = 300
buttonHeight = 80

#get button edges
play_edges = Edges(infoObject.current_w / 2.4, infoObject.current_w / 2.4 + buttonWidth, infoObject.current_h / 3.3 + buttonHeight, infoObject.current_h / 3.3)
instructions_edges = Edges(infoObject.current_w / 2.4, infoObject.current_w / 2.4 + buttonWidth, infoObject.current_h / 2.5 + buttonHeight, infoObject.current_h / 2.5)
login_edges = Edges(infoObject.current_w / 2.4, infoObject.current_w / 2.4 + buttonWidth, infoObject.current_h / 2 + buttonHeight, infoObject.current_h / 2)
register_edges = Edges(infoObject.current_w / 2.4, infoObject.current_w / 2.4 + buttonWidth, infoObject.current_h / 1.62 + buttonHeight, infoObject.current_h / 1.66)
leaderboard_edges = Edges(infoObject.current_w / 2.4, infoObject.current_w / 2.4 + buttonWidth, infoObject.current_h / 1.3 + buttonHeight, infoObject.current_h / 1.3)
custom_edges = Edges(infoObject.current_w / 1.3, infoObject.current_w / 1.3 + buttonWidth, infoObject.current_h / 2 + buttonHeight, infoObject.current_h / 2)
difficulty_edges = Edges(infoObject.current_w / 1.3, infoObject.current_w / 1.3 + buttonWidth, infoObject.current_h / 2.45 + buttonHeight, infoObject.current_h / 2.45)
#</MENU>

# <ITEM SHOP>
colourButtonWidth = 75
colourButtonHeight = 75

#get button edges
purple_edges = Edges(150, 150 + colourButtonWidth, 70 + colourButtonHeight, 70)
red_edges = Edges(260, 260 + colourButtonWidth, 70 + colourButtonHeight, 70)
white_edges = Edges(370, 370 + colourButtonWidth, 70 + colourButtonHeight, 70)
orange_edges = Edges(480, 480 + colourButtonWidth, 70 + colourButtonHeight, 70)

# </TIEM SHOP>

def loginUser():

    def check_login():

        global entered_username

        entered_username = username_entry.get()
        entered_password = password_entry.get()

        hashed_password = hashlib.sha256(entered_password.encode('utf-8')).hexdigest()

        #connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect("user_credentials.db")
        cursor = connection.cursor()

        #create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, level INTEGER DEFAULT 1, xp INTEGER DEFAULT 0, xpToGo INTEGER DEFAULT 50, currency INTEGER DEFAULT 0, isAdmin INTEGER DEFAULT 0, red INTEGER DEFAULT 0, white INTEGER DEFAULT 0, orange INTEGER DEFAULT 0)")

        #check if the user credentials are valid
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, hashed_password))
        user = cursor.fetchone()

        if user is not None:
            variables.loggedIn = entered_username
            variables.level = user[2]  #index that corresponds to the column in the database
            variables.xp = user[3]
            variables.xpToGo = user[4]
            variables.currency = user[5]
            variables.isAdmin = user[6]
            variables.red = user[7]
            variables.white = user[8]
            variables.orange = user[9]
            messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        #close the database connection
        connection.close()

    root = tk.CTk()

    root.title("Login Form")
    root.geometry("500x350")

    frame = tk.CTkFrame(master=root)
    frame.pack(padx = 60, pady = 20, fill = "both", expand = True)

    register_label = tk.CTkLabel(master=frame, text="Login")
    register_label.pack(padx = 10, pady = 12)

    #username label and entry field
    username_label = tk.CTkLabel(master=frame, text="Username:")
    username_label.pack()
    username_entry = tk.CTkEntry(master=frame, placeholder_text="Username")
    username_entry.pack(padx = 10, pady = 12)

    #password label and entry field
    password_label = tk.CTkLabel(master=frame, text="Password:")
    password_label.pack()
    password_entry = tk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    password_entry.pack(padx = 10, pady = 12)

    #login button
    login_button = tk.CTkButton(master=frame, text="Login", command=check_login)
    login_button.pack(padx = 10, pady = 12)

    root.mainloop()

run = True
def colourChange():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        variables.win.fill((16, 6, 48))

        currencyDisplay()
        userDisplay()

        #display current colour
        py.draw.rect(variables.win, (variables.colour), (30, 70, colourButtonWidth, colourButtonHeight))
        customise = variables.myFontMedium.render("Current", False, WHITE)
        variables.win.blit(customise, (30, 30))

        #check if colour is owned
        if variables.red != 1:
            customise = variables.myFont.render("50 E", False, WHITE)
            variables.win.blit(customise, (265, 30))

        if variables.white != 1:
            customise = variables.myFont.render("100 E", False, WHITE)
            variables.win.blit(customise, (375, 30))

        if variables.orange != 1:
            customise = variables.myFont.render("200 E", False, WHITE)
            variables.win.blit(customise, (485, 30))

        #draw buttons
        py.draw.rect(variables.win, (255, 0, 255), (150, 70, colourButtonWidth, colourButtonHeight))
        py.draw.rect(variables.win, (255, 0, 0), (260, 70, colourButtonWidth, colourButtonHeight))
        py.draw.rect(variables.win, (255, 255, 255), (370, 70, colourButtonWidth, colourButtonHeight))
        py.draw.rect(variables.win, (232, 160, 16), (480, 70, colourButtonWidth, colourButtonHeight))

        #set colour to default
        if py.mouse.get_pressed()[0]:
            if purple_edges.left <= mousePos[0] <= purple_edges.right and purple_edges.top <= mousePos[1] <= purple_edges.bottom:
                print("purple button clicked")
                variables.colour = 255, 0, 255

        #purchase colour
        #checks whether colour is owned then checks if user has sufficient funds and if so give colour and take funds
        if py.mouse.get_pressed()[0]:
            if red_edges.left <= mousePos[0] <= red_edges.right and red_edges.top <= mousePos[1] <= red_edges.bottom:
                print("Red button clicked")
                if variables.red != 1:
                    if variables.currency >= 50:
                        variables.colour = (255, 0, 0)
                        variables.red = 1
                        variables.currency -= 50
                        time.sleep(0.5)
                        purchase()

                #if player already owns the colour then equip it
                else:
                    variables.colour = 255, 0, 0

        if py.mouse.get_pressed()[0]:
            if white_edges.left <= mousePos[0] <= white_edges.right and white_edges.top <= mousePos[1] <= white_edges.bottom:
                print("White button clicked")
                if variables.white != 1:
                    if variables.currency >= 100:
                        variables.colour = (255, 255, 255)
                        variables.white = 1
                        variables.currency -= 100
                        time.sleep(0.5)
                        purchase()

                else:
                    variables.colour = 255, 255, 255

        if py.mouse.get_pressed()[0]:
            if orange_edges.left <= mousePos[0] <= orange_edges.right and white_edges.top <= mousePos[1] <= orange_edges.bottom:
                print("Orange button clicked")
                if variables.orange != 1:
                    if variables.currency >= 100:
                        variables.colour = (232, 160, 16)
                        variables.orange = 1
                        variables.currency -= 200
                        time.sleep(0.5)
                        purchase()

                else:
                    variables.colour = 232, 160, 16

        back()

        py.display.update()

    py.quit()

def difficulty():
    global run

    #find button edges
    easy_edges = Edges(150, 450, 375, 300)
    medium_edges = Edges(150, 450, 485, 410)
    hard_edges = Edges(150, 450, 595, 520)

    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        variables.win.fill((16, 6, 48))

        #draw buttons
        py.draw.rect(variables.win, (0, 0, 255), (easy_edges.left, easy_edges.top, easy_edges.size()[0], easy_edges.size()[1]))
        easy = variables.myFont.render("Easy", False, WHITE)
        variables.win.blit(easy, (255, 305))

        py.draw.rect(variables.win, (0, 0, 255), (medium_edges.left, medium_edges.top, medium_edges.size()[0], medium_edges.size()[1]))
        medium = variables.myFont.render("Medium", False, WHITE)
        variables.win.blit(medium, (225, 420))

        py.draw.rect(variables.win, (0, 0, 255), (hard_edges.left, hard_edges.top, hard_edges.size()[0], hard_edges.size()[1]))
        hard = variables.myFont.render("Hard", False, WHITE)
        variables.win.blit(hard, (255, 525))

        displayDifficulty = variables.myFont.render("Difficulty: " + variables.setDifficulty, False, WHITE)
        variables.win.blit(displayDifficulty, (25, 30))

        #when buttons are pressed, update difficulty
        if py.mouse.get_pressed()[0]:
            if easy_edges.left <= mousePos[0] <= easy_edges.right and easy_edges.top <= mousePos[1] <= easy_edges.bottom:
                variables.burnerStrength = variables.easyStrength
                variables.powerLevelTickRate = variables.easyPowerTick
                print("Easy button clicked, burnerStrength = ", variables.burnerStrength, "powerLevelTick = ", variables.powerLevelTickRate)
                variables.setDifficulty = "Easy"

        if py.mouse.get_pressed()[0]:
            if medium_edges.left <= mousePos[0] <= medium_edges.right and medium_edges.top <= mousePos[1] <= medium_edges.bottom:
                variables.burnerStrength = variables.medStrength
                variables.powerLevelTickRate = variables.medPowerTick
                print("Medium button clicked, burnerStrength = ", variables.burnerStrength, "powerLevelTick = ", variables.powerLevelTickRate)
                variables.setDifficulty = "Medium"

        if py.mouse.get_pressed()[0]:
            if hard_edges.left <= mousePos[0] <= hard_edges.right and hard_edges.top <= mousePos[1] <= hard_edges.bottom:
                variables.burnerStrength = variables.hardStrength
                variables.powerLevelTickRate = variables.hardPowerTick
                print("Hard button clicked, burnerStrength = ", variables.burnerStrength, "powerLevelTick = ", variables.powerLevelTickRate)
                variables.setDifficulty = "Hard"

        back()

        py.display.update()

    py.quit()

def save():
    mousePos = py.mouse.get_pos()

    save_edges = Edges(35, 235, 205, 135)

    py.draw.rect(variables.win, (255, 0, 0), (save_edges.left, save_edges.top, 200, 70))
    save = variables.myFontBig.render("Save", False, WHITE)
    variables.win.blit(save, (save_edges.left + 45, save_edges.top - 5))

    if py.mouse.get_pressed()[0]:
        if save_edges.left <= mousePos[0] <= save_edges.right and save_edges.top <= mousePos[1] <= save_edges.bottom:
            print("Save button clicked")
            if variables.loggedIn != 'nul':
                try:
                    #connect to the database
                    connection = sqlite3.connect("user_credentials.db")
                    cursor = connection.cursor()

                    #get the users current xp from the database
                    cursor.execute("SELECT xp FROM users WHERE username=?", (variables.loggedIn,))
                    current_xp = cursor.fetchone()[0]

                    cursor.execute("SELECT currency FROM users WHERE username=?", (variables.loggedIn,))
                    current_currency = cursor.fetchone()[0]

                    #only update the database if the xp has changed
                    if current_xp != variables.xp:
                        # Update the user's xp in the database
                        cursor.execute("UPDATE users SET xp=? WHERE username=?", (variables.xp, variables.loggedIn))

                        #commit the changes and close the database connection
                        connection.commit()
                        connection.close()
                        print("XP saved successfully.")

                    if current_currency != variables.currency:
                        cursor.execute("UPDATE users SET currency=? WHERE username=?", (variables.currency, variables.loggedIn))

                        connection.commit()
                        connection.close()
                        print("currency saved successfully.")

                    else:
                        print("XP is unchanged. No update needed.")
                except sqlite3.Error as e:
                    print("SQLite error:", e)
                except Exception as ex:
                    print("Error:", ex)


def purchase():
    if variables.loggedIn != 'nul':
        try:
            #connect to the database
            connection = sqlite3.connect("user_credentials.db")
            cursor = connection.cursor()

            #get the users current xp from the database
            cursor.execute("SELECT xp FROM users WHERE username=?", (variables.loggedIn,))
            current_xp = cursor.fetchone()[0]

            cursor.execute("SELECT currency FROM users WHERE username=?", (variables.loggedIn,))
            current_currency = cursor.fetchone()[0]

            cursor.execute("SELECT red FROM users WHERE username=?", (variables.loggedIn,))
            notRed = cursor.fetchone()[0]

            cursor.execute("SELECT white FROM users WHERE username=?", (variables.loggedIn,))
            notWhite = cursor.fetchone()[0]

            cursor.execute("SELECT orange FROM users WHERE username=?", (variables.loggedIn,))
            notOrange = cursor.fetchone()[0]

            #only update the database if the xp has changed
            if current_xp != variables.xp:
                #update the users xp in the database
                cursor.execute("UPDATE users SET xp=? WHERE username=?", (variables.xp, variables.loggedIn))
                print("XP saved successfully.")

            if current_currency != variables.currency:
                cursor.execute("UPDATE users SET currency=? WHERE username=?", (variables.currency, variables.loggedIn))
                print("currency saved successfully.")

            if notRed != variables.red:
                cursor.execute("UPDATE users SET red=? WHERE username=?", (variables.red, variables.loggedIn))
                print("purchase saved successfully.")

            if notWhite != variables.white:
                cursor.execute("UPDATE users SET white=? WHERE username=?", (variables.white, variables.loggedIn))
                print("purchase saved successfully.")

            if notOrange != variables.orange:
                cursor.execute("UPDATE users SET orange=? WHERE username=?", (variables.orange, variables.loggedIn))
                print("purchase saved successfully.")

            #commit the changes and close the database connection
            connection.commit()
            connection.close()
            
        except sqlite3.Error as e:
            print("SQLite error:", e)
        except Exception as ex:
            print("Error:", ex)


def levelXPDisplay():
    userLevel = variables.myFontMedium.render("Level: " + str(variables.level), False, WHITE)
    variables.win.blit(userLevel, (infoObject.current_w / infoObject.current_w + 35, 300))

    userXp = variables.myFontMedium.render("Experience: " + str(variables.xp), False, WHITE)
    variables.win.blit(userXp, (infoObject.current_w / infoObject.current_w + 35, 400))

    xpLimit = variables.myFontMedium.render("XP To Level Up: " + str(variables.xpToGo), False, WHITE)
    variables.win.blit(xpLimit, (infoObject.current_w / infoObject.current_w + 35, 485))

    progress = variables.myFont.render("Progress:", False, WHITE)
    variables.win.blit(progress, (infoObject.current_w / infoObject.current_w + 35, 565))

    progressionW = int(variables.xp) * 250 / int(variables.xpToGo)
    py.draw.rect(variables.win, (125, 125, 125), (infoObject.current_w / infoObject.current_w + 35, 600, 250, 15))
    py.draw.rect(variables.win, (0, 255, 0), (infoObject.current_w / infoObject.current_w + 35, 600, progressionW, 15))

def currencyDisplay():
    usern = variables.myFontMedium.render("Eddies: " + str(variables.currency), False, WHITE)
    variables.win.blit(usern, (infoObject.current_w - 350, 100))

run = True
def exit():
    global run

    mousePos = py.mouse.get_pos()

    exit_edges = Edges(infoObject.current_w / infoObject.current_w + 35, infoObject.current_w / infoObject.current_w + 35 + 200, infoObject.current_h / infoObject.current_w + 35 + 70, infoObject.current_h / infoObject.current_h + 35)

    py.draw.rect(variables.win, (255, 0, 0), (infoObject.current_w / infoObject.current_w + 35, infoObject.current_h / infoObject.current_h + 35, 200, 70))
    back = variables.myFontBig.render("Exit", False, WHITE)
    variables.win.blit(back, (infoObject.current_w / infoObject.current_w + 80, infoObject.current_h / infoObject.current_h + 35))

    if py.mouse.get_pressed()[0]:
        if exit_edges.left <= mousePos[0] <= exit_edges.right and exit_edges.top <= mousePos[1] <= exit_edges.bottom:

            run = False

def menu():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        variables.win.fill((16, 6, 48))

        py.draw.rect(variables.win, (125, 125, 125), (infoObject.current_w / 4, infoObject.current_h / 12.5, 930, buttonHeight))
        title = variables.myFontBig.render("Fight the Storm", False, WHITE)
        variables.win.blit(title, (infoObject.current_w / 2.5, infoObject.current_h / 12))

        py.draw.rect(variables.win, (variables.BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 3.3, buttonWidth, buttonHeight))
        play = variables.myFontMedium.render("Play", False, WHITE)
        variables.win.blit(play, (infoObject.current_w / 2.1, infoObject.current_h / 3.15))

        py.draw.rect(variables.win, (variables.BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 2.5, buttonWidth, buttonHeight))
        instructions = variables.myFontMedium.render("How To Play", False, WHITE)
        variables.win.blit(instructions, (infoObject.current_w / 2.25, infoObject.current_h / 2.43))
        
        py.draw.rect(variables.win, (variables.BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 2, buttonWidth, buttonHeight))
        login = variables.myFontMedium.render("Login", False, WHITE)
        variables.win.blit(login, (infoObject.current_w / 2.14, infoObject.current_h / 1.95))

        py.draw.rect(variables.win, (variables.BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 1.66, buttonWidth, buttonHeight))
        register = variables.myFontMedium.render("Register", False, WHITE)
        variables.win.blit(register, (infoObject.current_w / 2.2, infoObject.current_h / 1.63))

        py.draw.rect(variables.win, (255, 0, 255), (infoObject.current_w / 2.4, infoObject.current_h / 1.3, buttonWidth, buttonHeight))
        register = variables.myFontMedium.render("Leaderboard", False, WHITE)
        variables.win.blit(register, (infoObject.current_w / 2.28, infoObject.current_h / 1.28))
        
        py.draw.rect(variables.win, (112, 112, 112), (infoObject.current_w / 1.3, infoObject.current_h / 2, buttonWidth, buttonHeight))
        customise = variables.myFontMedium.render("Cosmetics", False, WHITE)
        variables.win.blit(customise, (infoObject.current_w / 1.25, infoObject.current_h / 1.95))

        py.draw.rect(variables.win, (112, 112, 112), (infoObject.current_w / 1.3, infoObject.current_h / 2.45, buttonWidth, buttonHeight))
        customise = variables.myFontMedium.render("Difficulty", False, WHITE)
        variables.win.blit(customise, (infoObject.current_w / 1.25, infoObject.current_h / 2.4))

        admin()

        if py.mouse.get_pressed()[0]:
            if play_edges.left <= mousePos[0] <= play_edges.right and play_edges.top <= mousePos[1] <= play_edges.bottom:
                print("Play button clicked")
                startGame()

        if py.mouse.get_pressed()[0]:
            if instructions_edges.left <= mousePos[0] <= instructions_edges.right and instructions_edges.top <= mousePos[1] <= instructions_edges.bottom:
                print("Instructions button clicked")
                instruction()

        if py.mouse.get_pressed()[0]:
            if register_edges.left <= mousePos[0] <= register_edges.right and register_edges.top <= mousePos[1] <= register_edges.bottom:
                print("Register button clicked")
                registerUser()

        if py.mouse.get_pressed()[0]:
            if login_edges.left <= mousePos[0] <= login_edges.right and login_edges.top <= mousePos[1] <= login_edges.bottom:
                print("Login button clicked")
                loginUser()

        if py.mouse.get_pressed()[0]:
            if leaderboard_edges.left <= mousePos[0] <= leaderboard_edges.right and leaderboard_edges.top <= mousePos[1] <= leaderboard_edges.bottom:
                print("Leaderboard button clicked")
                leaderboard()
                run = False

        if py.mouse.get_pressed()[0]:
            if custom_edges.left <= mousePos[0] <= custom_edges.right and custom_edges.top <= mousePos[1] <= custom_edges.bottom:
                print("Custom button clicked")
                colourChange()

        if py.mouse.get_pressed()[0]:
            if difficulty_edges.left <= mousePos[0] <= difficulty_edges.right and difficulty_edges.top <= mousePos[1] <= difficulty_edges.bottom:
                print("Difficulty button clicked")
                difficulty()

        py.draw.rect(variables.win, (64, 64, 64), (infoObject.current_w / infoObject.current_w + 15, 250, 400, 600))

        userDisplay()
        levelXPDisplay()
        levelUp()
        save()
        exit()
        currencyDisplay()

        py.display.update()

    py.quit()

def userDisplay():
    usern = variables.myFont.render("Logged in as: " + variables.loggedIn, False, WHITE)
    win.blit(usern, (infoObject.current_w - 350, 35))

menu()