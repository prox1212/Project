from lib2to3.pgen2.token import LEFTSHIFT
import pygame as py
import pygame.time
import random
import time
import tkinter as tk
from tkinter import messagebox
import customtkinter as tk
import sqlite3
import threading
import hashlib
#from login import *
from backButton import *
from vars import *

py.init()

py.font.init()

py.display.set_caption("Fight the Storm")

ticks = 0  #to keep track of ticks

clock = py.time.Clock()
desiredFps = 165

# Player data
width = 35
height = 35

pos_x = infoObject.current_w / 2
pos_y = infoObject.current_h / 2

velocity = 3

health = 250
realHealth = 100
realHealth = str(realHealth)
realHealthNum = int(realHealth)

hit_multiple_4 = False

# Storm
alpha_value = 128
transparent_surface = py.Surface((infoObject.current_w, infoObject.current_h), py.SRCALPHA)
transparent_surface.set_alpha(alpha_value)
py.draw.rect(transparent_surface, (16, 6, 48, alpha_value), transparent_surface.get_rect())  # Cover the entire screen with transparency

stormSize = 800

durability = 250
realDurability = 500
realDurability = str(realDurability)
realDurabilityNum = int(realDurability)

# <MATERIALS>
woodFlag = True
wood2Flag = True
coalFlag = True
brickFlag = True

woodX = random.randint(5, 1800)
woodY = random.randint(5, 1000)

wood2X = random.randint(5, 1800)
wood2Y = random.randint(5, 1000)

coalX = random.randint(5, 1800)
coalY = random.randint(5, 1000)

brickX = random.randint(5, 1800)
brickY = random.randint(5, 1000)

woodPNG = py.image.load(r'Assets/planks.png')
imageWood = py.transform.scale(woodPNG, (50, 50))

coalPNG = py.image.load(r'Assets/coal.png')
imageCoal = py.transform.scale(coalPNG, (50, 50))

brickPNG = py.image.load(r'Assets/brick.png')
imageBrick = py.transform.scale(brickPNG, (50, 50))

last_wood_addition_time = 0
last_coal_addition_time = 0
last_brick_addition_time = 0

# </MATERIALS>

class Player:

    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def handle_input(self):
        keys = py.key.get_pressed()

        if keys[py.K_LEFT] or keys[py.K_a] and self.x > 0:
            self.x -= self.velocity

        if keys[py.K_RIGHT] or keys[py.K_d] and self.x > 0:
            self.x += self.velocity

        if keys[py.K_UP] or keys[py.K_w] and self.y > 0:
            self.y -= self.velocity
        
        if keys[py.K_DOWN] or keys[py.K_s] and self.y > 0:
            self.y += self.velocity

    def update_position(self):
         global pos_x, pos_y
         pos_x = self.x
         pos_y = self.y

    def draw(self):
        # Draw the player on the screen
        py.draw.rect(win, (variables.colour), (self.x, self.y, self.width, self.height))

    def woodCounter(self):
        count = variables.myFont.render("Wood: " + str(variables.woodCount), False, WHITE)
        win.blit(count, (infoObject.current_w - 150, 45))

    def coalCounter(self):
        count = variables.myFont.render("Coal: " + str(variables.coalCount), False, WHITE)
        win.blit(count, (infoObject.current_w - 150, 70))

    def brickCounter(self):
        count = variables.myFont.render("Brick: " + str(variables.brickCount), False, WHITE)
        win.blit(count, (infoObject.current_w - 150, 95))

    def healthBarPlayer():
        global realHealth, realHealthNum, realDurabilityNum, over, woodFlag, wood2Flag, coalFlag, brickFlag

        decreaseHealth = realHealthNum * health / 100
        py.draw.rect(win, (125, 125, 125), (20, 40, 250, 25))
        py.draw.rect(win, (0, 255, 0), (20, 40, decreaseHealth, 25))
        healthDisplay = variables.myFontSmall.render(" | 100", False, WHITE)
        realHealthDisplay = variables.myFontSmall.render(str(realHealthNum), False, WHITE)
        player = variables.myFont.render("" + variables.loggedIn, False, WHITE)
        win.blit(healthDisplay, (45, 43))
        win.blit(realHealthDisplay, (21, 43))
        win.blit(player, (21, 10))

        if realHealthNum <= 0:
            over = True
            woodFlag = False
            wood2Flag = False
            coalFlag = False
            brickFlag = False
            variables.coalCount = 0
            variables.woodCount = 0
            variables.brickCount = 0
            variables.powerLevel = 1
            if variables.setDifficulty == "Easy":
                variables.burnerStrength = variables.easyStrength
                variables.powerLevelTickRate = variables.easyPowerTick

            if variables.setDifficulty == "Medium":
                variables.burnerStrength = variables.medStrength
                variables.powerLevelTickRate = variables.medPowerTick

            if variables.setDifficulty == "Hard":
                variables.burnerStrength = variables.hardStrength
                variables.powerLevelTickRate = variables.medPowerTick
            gameOver()

class PlayerEdges:
    def __init__(self, playerTop, playerLeft, playerBottom, playerRight):
        self.playerTop = playerTop
        self.playerLeft = playerLeft
        self.playerBottom = playerBottom
        self.playerRight = playerRight

    def playerSize(self):
        return (self.playerTop, self.playerLeft, self.playerBottom, self.playerRight)
    
run = True
def startGame():
    global pos_x, pos_y, run, ticks, realHealthNum, stormSize, distance, realHealth, health, realDurabilityNum, realDurability, woodFlag
    global woodX, woodY, wood2Flag, brickFlag, wood2X, wood2Y, last_wood_addition_time, last_coal_addition_time, last_brick_addition_time, coalFlag
    global coalX, coalY, brickX, brickY
    global previous_ticks, fps

    initialStormSize = 800  #initial stormSize value
    
    while run:
        py.time.delay(10)
        ticks += 1  #increment ticks
        #woodSpawnRate += 1
        current_time = pygame.time.get_ticks()

        #clock.tick(desiredFps)
        fps = int(clock.get_fps())

        previous_ticks = current_time

        time_since_last_wood_addition = current_time - last_wood_addition_time
        time_since_last_coal_addition = current_time - last_coal_addition_time
        time_since_last_brick_addition = current_time - last_brick_addition_time

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()

        player = Player(pos_x, pos_y, width, height, velocity)
        player_edges = PlayerEdges(pos_x, pos_y, pos_x + width, pos_y + height)

        #calculate the distance between the player and the center of the circle
        distance = ((infoObject.current_w // 2 - pos_x) ** 2 + (infoObject.current_h // 2 - pos_y) ** 2) ** 0.5

        win.fill((16, 6, 48))

        #draw the transparent overlay
        win.blit(transparent_surface, (0, 0))

        #calculate the adjusted stormSize based on durability
        adjustedStormSize = initialStormSize * (realDurabilityNum / 500)

        #draw the storm (circle) with the adjusted size
        py.draw.circle(win, (53, 120, 2), (infoObject.current_w // 2, infoObject.current_h // 2), int(adjustedStormSize))

        if ticks % variables.burnerStrength == 0 and realDurabilityNum:

            if realDurabilityNum > 0 and realHealthNum > 0:
                realDurabilityNum -= 1
                realDurability = str(realDurabilityNum)

        #check if the player is outside the green circle (double the radius) and 100 ticks have passed
        if distance > adjustedStormSize and ticks % 75 == 0:

            if realHealthNum > 0 and realDurabilityNum > 0:
                realHealthNum -= 5
                realHealth = str(realHealthNum)

        distance = ((infoObject.current_w // 2 - pos_x) ** 2 + (infoObject.current_h // 2 - pos_y) ** 2) ** 0.5

        #check if the player is inside the circle
        if distance < adjustedStormSize:
            if realHealthNum < 100 and ticks % 45 == 0:
                if realHealthNum > 0 and realDurabilityNum > 0:
                    realHealthNum += 1
                    realHealth = str(realHealthNum)

        xp_conditions = [(variables.xpDivisor, 1), (6000, 150), (18000, 450), (30000, 1000)]

        for condition, xp_increment in xp_conditions:
            if ticks % condition == 0 and realHealthNum > 0 and realDurabilityNum > 0:
                variables.xp += xp_increment


        
        #power level
        if ticks % variables.powerLevelTickRate == 0:
            variables.powerLevel += 1

        if variables.powerLevel % 4 == 0 and not hit_multiple_4:
            hit_multiple_4 = True

            variables.powerLevelTickRate -= variables.powerLevelTickDecayRate

            if variables.powerLevelTickRate <= 400:
                variables.burnerStrength -= variables.strengthDecayMaxPowerLevel

            else:
                variables.burnerStrength -= variables.strengthDecay

            if variables.powerLevelTickRate < 400:
                variables.powerLevelTickRate = 400
        elif variables.powerLevel % 4 != 0:
            hit_multiple_4 = False

        power = variables.myFontMedium.render("Power Level: " + str(variables.powerLevel), False, WHITE)
        win.blit(power, (10, 130))
        strength = variables.myFont.render("Burner Strength: " + str(variables.burnerStrength), False, WHITE)
        win.blit(strength, (10, 170))

        #burner
        py.draw.rect(win, (0, 0, 255), (infoObject.current_w / 2 - 35, infoObject.current_h / 2 - 35, 70, 70))
        text = variables.myFontSmall.render("Burner", False, WHITE)
        win.blit(text, (infoObject.current_w / 2 - 30, infoObject.current_h / 2 - 15))

        burner_edges = Edges(infoObject.current_h / 2 - 35, infoObject.current_h / 2 - 35 + 70, infoObject.current_w / 2 - 35 + 70, infoObject.current_w / 2 - 35)

        if player_edges.playerRight >= burner_edges.left and player_edges.playerLeft <= burner_edges.right and player_edges.playerBottom >= burner_edges.top and player_edges.playerTop <= burner_edges.bottom:
            if variables.woodCount > 0:
                interact = variables.myFont.render("Press 'E' to add wood", False, WHITE)
                win.blit(interact, (infoObject.current_w / 2 - 120, infoObject.current_h / 2 - 200))

                if keys[py.K_e] and time_since_last_wood_addition >= 500:
                    variables.woodCount -= 1
                    realDurabilityNum += 25
                    last_wood_addition_time = current_time
                    variables.xp += 25

            if variables.coalCount > 0:
                interact = variables.myFont.render("Press 'F' to add coal", False, WHITE)
                win.blit(interact, (infoObject.current_w / 2 - 120, infoObject.current_h / 2 - 230))

                if keys[py.K_f] and time_since_last_coal_addition >= 500:
                    variables.coalCount -= 1
                    realDurabilityNum += 50
                    last_coal_addition_time = current_time
                    variables.xp += 50

            if variables.brickCount > 0:
                interact = variables.myFont.render("Press 'G' to add Strength", False, WHITE)
                win.blit(interact, (infoObject.current_w / 2 - 120, infoObject.current_h / 2 - 260))

                if keys[py.K_g] and time_since_last_brick_addition >= 500:
                    variables.brickCount -= 1
                    variables.burnerStrength += 1
                    last_brick_addition_time = current_time
                    variables.xp += 35

        wood_edges = Edges(woodY, woodY + 30, woodX + 30, woodX)

        wood2_edges = Edges(wood2Y, wood2Y + 30, wood2X + 30, wood2X)

        coal_edges = Edges(coalY, coalY + 30, coalX + 30, coalX)

        brick_edges = Edges(brickY, brickY + 30, brickX + 30, brickX)

        if player_edges.playerRight >= wood_edges.left and player_edges.playerLeft <= wood_edges.right and player_edges.playerBottom >= wood_edges.top and player_edges.playerTop <= wood_edges.bottom:
            woodFlag = False
            variables.woodCount += 1

        if woodFlag == False and realHealthNum and realDurabilityNum > 0:
                woodX = random.randint(5, 1800)
                woodY = random.randint(5, 1000)
                woodFlag = True

        if player_edges.playerRight >= wood2_edges.left and player_edges.playerLeft <= wood2_edges.right and player_edges.playerBottom >= wood2_edges.top and player_edges.playerTop <= wood2_edges.bottom:
            wood2Flag = False
            variables.woodCount += 1

        if wood2Flag == False and realHealthNum and realDurabilityNum > 0:
                wood2X = random.randint(5, 1800)
                wood2Y = random.randint(5, 1000)
                wood2Flag = True

        if player_edges.playerRight >= coal_edges.left and player_edges.playerLeft <= coal_edges.right and player_edges.playerBottom >= coal_edges.top and player_edges.playerTop <= coal_edges.bottom:
            coalFlag = False
            variables.coalCount += 1

        if coalFlag == False and realHealthNum and realDurabilityNum > 0:
                coalX = random.randint(5, 1800)
                coalY = random.randint(5, 1000)
                coalFlag = True

        if player_edges.playerRight >= brick_edges.left and player_edges.playerLeft <= brick_edges.right and player_edges.playerBottom >= brick_edges.top and player_edges.playerTop <= brick_edges.bottom:
            brickFlag = False
            variables.brickCount += 1

        if brickFlag == False and realHealthNum and realDurabilityNum > 0:
                brickX = random.randint(5, 1800)
                brickY = random.randint(5, 1000)
                brickFlag = True

        player.handle_input()
        player.update_position()
        levelUp()
        admin()
        wood()
        wood2()
        coal()
        brick()
        player.draw()
        ingameXpBar()
        Player.healthBarPlayer()
        healthBarBurner()
        back()
        player.woodCounter()
        player.coalCounter()
        player.brickCounter()


        fps_text = variables.myFontSmall.render(f'FPS: {fps}', True, (255, 255, 255))
        win.blit(fps_text, (infoObject.current_w - 100 , 10))

        py.display.update()

        clock.tick(desiredFps)

    py.quit()

def admin():
    global realHealth, realHealthNum, stormSize, realDurability, realDurabilityNum
    keys = py.key.get_pressed()

    if variables.isAdmin == 1:

        if keys[py.K_r]:
            variables.xp += 1

        if keys[py.K_t]:
            realHealthNum = int(realHealth)
            realHealthNum -= 1
            realHealth = str(realHealthNum)

        if keys[py.K_o]:
            stormSize -= 1

        if keys[py.K_i]:
            stormSize += 1

        if keys[py.K_p]:
            realDurabilityNum = int(realDurability)
            realDurabilityNum += 1
            realDurability = str(realDurabilityNum)

progressionW = int(variables.xp) * 250 / int(variables.xpToGo)
def ingameXpBar():
    global progressionW
    progressionW = int(variables.xp) * 250 / int(variables.xpToGo)  # Update progressionW based on current XP and XPToGo

    py.draw.rect(win, (125, 125, 125), (infoObject.current_w / 2.3, infoObject.current_h - 20, 250, 15))
    py.draw.rect(win, (0, 255, 0), (infoObject.current_w / 2.3, infoObject.current_h - 20, progressionW, 15))

    userLevel = variables.myFontSmall.render("Level: " + str(variables.level), False, WHITE)
    win.blit(userLevel, (infoObject.current_w / 2.5, infoObject.current_h - 45))

    userXp = variables.myFontSmall.render("Experience: " + str(variables.xp), False, WHITE)
    win.blit(userXp, (infoObject.current_w / 2.1, infoObject.current_h - 45))

    xpLimit = variables.myFontSmall.render("/ " + str(variables.xpToGo), False, WHITE)
    win.blit(xpLimit, (infoObject.current_w / 1.75, infoObject.current_h - 45))


def healthBarBurner():
    global realDurability, realDurabilityNum, realHealthNum, over, woodFlag, wood2Flag, coalFlag, brickFlag

    decreaseDurability = realDurabilityNum * durability / 500
    py.draw.rect(win, (125, 125, 125), (20, 100, 250, 25))
    py.draw.rect(win, (255, 140, 0), (20, 100, decreaseDurability, 25))
    durabilityDisplay = variables.myFontSmall.render(" | 500", False, WHITE)
    realDurabilityDisplay = variables.myFontSmall.render(str(realDurabilityNum), False, WHITE)
    burner = variables.myFont.render("Burner", False, WHITE)
    win.blit(durabilityDisplay, (45, 100))
    win.blit(realDurabilityDisplay, (21, 100))
    win.blit(burner, (21, 70))

    if realDurabilityNum > 500:
        realDurabilityNum = 500

    if realDurabilityNum <= 0:
        over = True
        woodFlag = False
        wood2Flag = False
        coalFlag = False
        brickFlag = False
        variables.coalCount = 0
        variables.woodCount = 0
        variables.brickCount = 0
        variables.powerLevel = 1
        if variables.setDifficulty == "Easy":
            variables.burnerStrength = variables.easyStrength
            variables.powerLevelTickRate = variables.easyPowerTick
        
        if variables.setDifficulty == "Medium":
            variables.burnerStrength = variables.medStrength
            variables.powerLevelTickRate = variables.medPowerTick

        if variables.setDifficulty == "Hard":
            variables.burnerStrength = variables.hardStrength
            variables.powerLevelTickRate = variables.medPowerTick
        gameOver()

def levelUp():
    variables.xp = int(variables.xp)
    variables.xpToGo = int(variables.xpToGo)

    if variables.xp >= variables.xpToGo:
        variables.xp -= variables.xpToGo
        initialXP = int(variables.xpToGo * variables.xpToGoMultiplier)
        variables.xpToGo = round(initialXP, -1)
        variables.level += 1
        
        if variables.level % 10 == 0:
            variables.currency += 100

        elif variables.level % 5 == 0:
            variables.currency += 50

        else:
            variables.currency += 20

        #move database update to a separate thread
        def update_database():
            try:
                connection = sqlite3.connect("user_credentials.db")
                cursor = connection.cursor()

                cursor.execute("UPDATE users SET level=?, xp=?, xpToGo=?, currency=? WHERE username=?", (variables.level, variables.xp, variables.xpToGo, variables.currency, variables.loggedIn))

                connection.commit()
                connection.close()
            except sqlite3.Error as e:
                print("SQLite error:", e)
            except Exception as ex:
                print("Error:", ex)

        #create a new thread for database update
        db_update_thread = threading.Thread(target=update_database)
        db_update_thread.start()

def gameOver():
    global run, realHealthNum, realDurabilityNum

    #create a semi-transparent black surface
    game_over_surface = py.Surface((1450, 700), py.SRCALPHA)
    game_over_surface.fill((0, 0, 0, 178))  # The fourth value (178) controls opacity (0-255)
    win.blit(game_over_surface, (250, 175))

    title = variables.myFontBig.render("Game Over", False, WHITE)
    win.blit(title, (850, 180))

    mousePos = py.mouse.get_pos()


    save_edges = Edges(300, 500, 835, 765)

    menu_edges = Edges(1445, 1645, 835, 765)

    py.draw.rect(win, (255, 0, 0), (save_edges.left, save_edges.top, 200, 70))
    save = variables.myFontBig.render("Save", False, WHITE)
    win.blit(save, (save_edges.left + 45, save_edges.top - 5))

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
                        #update the users xp in the database
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

    
    py.draw.rect(win, (255, 0, 0), (menu_edges.left, menu_edges.top, 200, 70))
    menu = variables.myFontBig.render("Menu", False, WHITE)
    win.blit(menu, (menu_edges.left + 45, menu_edges.top - 5))

    if py.mouse.get_pressed()[0]:
        if menu_edges.left <= mousePos[0] <= menu_edges.right and menu_edges.top <= mousePos[1] <= menu_edges.bottom:
            print("Menu button clicked")
            realDurabilityNum = 500
            realHealthNum = 100
            import menu
            menu.menu()
            run = False

def wood():
    if woodFlag == True:
        win.blit(imageWood, (woodX, woodY))

def wood2():
    if wood2Flag == True:
        win.blit(imageWood, (wood2X, wood2Y))

def coal():
    if coalFlag == True:
        win.blit(imageCoal, (coalX, coalY))

def brick():
    if brickFlag == True:
        win.blit(imageBrick, (brickX, brickY))

if __name__ == "__main__":
    startGame()