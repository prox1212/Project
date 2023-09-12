import pygame as py
import math
import random
from inventory import *
from brightcore_ore import *
from options import *

py.init()

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.display.set_caption("stw")

#speed of player
velocity = 2.5
velocityDiagonal = 0.2

#player info
width = 100
height = 100

pos_x = 0
pos_y = 120

#back button
backButtonW = 120
backButtonH = 80
backButtonX = infoObject.current_w - backButtonW - 10
backButtonY = 10


#progress bar
xpBarW = 600
xpBarH = 40

progressWidth = 1
progressHeight = 40

experience = 0
experienceToGet = 50
totalExperience = 0

rank = 'Iron'

level = 1

WHITE = (255, 255, 255)
LEVELCOL = (255, 255, 255)

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 19)
myFontBig = py.font.SysFont('Comic Sans MS', 22)
myFontObease = py.font.SysFont('Comic Sans MS', 35)

# backTop = infoObject.current_w - 130
# backLeft = 10
# backBottom = infoObject.current_w - 130 + backButtonH
# backRight = 10 + backButtonW

chestSizeX = 100
chestSizeY = 45

chestX = random.randint(30, (infoObject.current_w - 120))
chestY = random.randint(120, (infoObject.current_h - 120))

chestLeft = chestX
chestRight = chestX + chestSizeX
chestTop = chestY
chestBottom = chestY + chestSizeY

chestOpened = False
starter = 0

#custom event for the timer
TIMER_EVENT = py.USEREVENT + 1
py.time.set_timer(TIMER_EVENT, 1000)  # Trigger the event every 1000 milliseconds (1 second)

def experienceBar():
    py.draw.rect(win, (164, 167, 171), (infoObject.current_w / 3, infoObject.current_h - 20, xpBarW, xpBarH))
    xp = myFont.render(" Experience = " + str(experience), False, WHITE)
    win.blit(xp, (infoObject.current_w / 2, infoObject.current_h - 45))

    displayLevel = myFont.render("Level: " + str(level), False, LEVELCOL)
    win.blit(displayLevel, (infoObject.current_w / 2.2, infoObject.current_h - 45))

    py.draw.rect(win, (0, 255, 0), (infoObject.current_w / 3, infoObject.current_h - 20, progressWidth, progressHeight))
    progress = myFont.render("Level up: " + str(experienceToGet), False, WHITE)
    win.blit(progress, (infoObject.current_w / 2, infoObject.current_h - 20))


def progression():
    global progressWidth
    test = experience / experienceToGet * xpBarW 
    progressWidth = test
    #old system
    #displayProgress = experience / (infoObject.current_w - 10 * 100)
    #progressWidth = displayProgress * (xpBarW - 10)

def levelUp():
    global progressWidth, level, experience
    if experience >= experienceToGet:
        experience = 0
        progressWidth = 1
        level += 1

def xpRequirements():
    global experienceToGet, LEVELCOL, rank
    if level >= 5 and level < 9:
        experienceToGet = 75

    elif level >= 10 and level < 14:
        experienceToGet = 100
        LEVELCOL = (205, 127, 50)
        rank = 'Bronze'

    elif level >= 15 and level < 20:
        experienceToGet = 125
        LEVELCOL = (205, 127, 50)
        rank = 'Bronze'

    elif level >= 20 and level < 24:
        experienceToGet = 150
        LEVELCOL = (192, 192, 192)
        rank = 'Silver'

    elif level >= 25 and level < 30:
        experienceToGet = 175
        LEVELCOL = (192, 192, 192)
        rank = 'Silver'

    elif level >= 30 and level < 34:
        experienceToGet = 200
        LEVELCOL = (255,215,0)
        rank = 'Gold'

    elif level >= 35 and level < 40:
        experienceToGet = 225
        LEVELCOL = (255,215,0)
        rank = 'Gold'

    elif level >= 40 and level < 44:
        experienceToGet = 350
        LEVELCOL = (243, 71, 255)
        rank = 'Master'

    elif level >= 45 and level < 50:
        experienceToGet = 475
        LEVELCOL = (243, 71, 255)
        rank = 'Master'

    elif level >= 50:
        experienceToGet = 1000
        LEVELCOL = (240, 26, 26)
        rank = 'Elite'

chest = py.image.load('Assets/chest.png')
displayPistol1Message = False
pistol1Timer = 0

def rotate_player_towards_mouse(player_image, player_pos):
    mouse_pos = py.mouse.get_pos()
    angle = math.degrees(math.atan2(mouse_pos[1] - player_pos[1], mouse_pos[0] - player_pos[0]))
    rotated_player = py.transform.rotate(player_image, -angle)
    rotated_rect = rotated_player.get_rect(center=player_image.get_rect(center=player_pos).center)
    return rotated_player, rotated_rect

def Chest():
    global experience, totalExperience, chestOpened, chest, starter, displayPistol1Message, pistol1Timer
    if chestOpened:
        return
    
    chest = py.transform.scale(chest, (chestSizeX, chestSizeY))
    win.blit(chest, (chestX, chestY))

    keys = py.key.get_pressed()
    player_right = pos_x + width
    player_left = pos_x
    player_bottom = pos_y + height
    player_top = pos_y

    if player_right >= chestLeft and player_left <= chestRight and player_bottom >= chestTop and player_top <= chestBottom:
        if not chestOpened:
            openChest = myFontBig.render("'E' To open Chest", False, WHITE)
            win.blit(openChest, (infoObject.current_w / 2.2, infoObject.current_h / 1.7))

        if keys[py.K_e]:
            experience += 25
            totalExperience += 25
            chestOpened = True

            displayPistol1Message = True
            pistol1Timer = py.time.get_ticks()
            starter = 1

            #if chestOpened == True:
            #chest = py.image.load('Assets/chest_open.png')

#pre rendering items
pistol1 = py.image.load("Assets/pistol_level1.png")
pistol1Display = py.transform.scale(pistol1, (90, 90))

def loadPistol1():
    if starter == 1:
        win.blit(pistol1Display, (10, 10))



def backButton():
    global run
    mousePos = py.mouse.get_pos()
    click = py.mouse.get_pressed()

    if backButtonX <= mousePos[0] <= backButtonX + backButtonW and \
            backButtonY <= mousePos[1] <= backButtonY + backButtonH:
        py.draw.rect(win, (128, 0, 0), (backButtonX, backButtonY, backButtonW, backButtonH))
        if click[0]:
            import menu
            menu.menus()
            run = False
    else:
        py.draw.rect(win, (255, 0, 0), (backButtonX, backButtonY, backButtonW, backButtonH))

    back = myFontObease.render("Back", False, WHITE)
    win.blit(back, (backButtonX + 10, backButtonY + 10))

run = True

def startGame():
    global run, pos_x, pos_y, experience, progressWidth, totalExperience, starter, displayPistol1Message, pistol1Timer
    while run:
        py.time.delay(10)
        current_time = py.time.get_ticks()

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        keys = py.key.get_pressed()

        if keys[py.K_LEFT] or keys[py.K_a] and pos_x > 0:
            pos_x -= velocity

        if keys[py.K_RIGHT] or keys[py.K_d] and pos_x < infoObject.current_w - width:
            pos_x += velocity

        if keys[py.K_UP] or keys[py.K_w] and pos_y > 0:
            pos_y -= velocity

        if keys[py.K_DOWN] or keys[py.K_s] and pos_y < infoObject.current_h - height:
            pos_y += velocity

        # elif keys[py.K_DOWN] or keys[py.K_s] and keys[py.K_RIGHT] or keys[py.K_d] and pos_y < infoObject.current_h - height:
        #     pos_y += velocityDiagonal
        #     pos_x += velocityDiagonal

        update_player_pos(pos_x, pos_y)

        win.fill((8, 89, 80))

        #player
        player = py.image.load('Assets/player.png')
        player_scaled = py.transform.scale(player, (width, height))
        rotated_player, player_rect = rotate_player_towards_mouse(player_scaled, (pos_x + width // 2, pos_y))
        win.blit(rotated_player, player_rect.topleft)

        #inventory
        inventory()
        loadPistol1()

        # Display the message if the flag is True and less than 3 seconds have passed
        if displayPistol1Message and current_time - pistol1Timer < 3000:
            message = myFontMedium.render("Received: Starter Pistol", False, WHITE)
            win.blit(message, (5, infoObject.current_h / 2))

        # After 3 seconds, reset the flag to stop displaying the message
        if current_time - pistol1Timer >= 3000:
            displayPistol1Message = False

        #brightcore
        #spawnBrightcore()
        #brightcoreDisplayHealth()

        #back button
        # py.draw.rect(win, (255, 0, 0), (infoObject.current_w - 130, 10, backButtonW, backButtonH))
        # back = myFontObease.render("Back", False, WHITE)
        # win.blit(back, (infoObject.current_w - 110, 20))

        #experience bar
        py.draw.rect(win, (164, 167, 171), (infoObject.current_w / 3, infoObject.current_h - 20, xpBarW, xpBarH))
        xp = myFont.render(" Experience = " + str(experience), False, WHITE)
        win.blit(xp, (infoObject.current_w / 2.2, infoObject.current_h - 45))

        displayLevel = myFont.render("Level: " + str(level), False, LEVELCOL)
        win.blit(displayLevel, (infoObject.current_w / 2.6, infoObject.current_h - 45))

        py.draw.rect(win, (0, 255, 0), (infoObject.current_w / 3, infoObject.current_h - 20, progressWidth, progressHeight))
        progress = myFont.render("Level up: " + str(experienceToGet), False, WHITE)
        win.blit(progress, (infoObject.current_w / 2.15, infoObject.current_h - 20))

        #display rank
        displayRank = myFont.render("Rank: " + str(rank), False, LEVELCOL)
        win.blit(displayRank, (infoObject.current_w / 1.8, infoObject.current_h - 45))

        #net xp
        progress = myFontMedium.render("Net Experience: " + str(totalExperience), False, WHITE)
        win.blit(progress, (10, infoObject.current_h - 30))

        if keys[py.K_r]:
            experience += 1
            totalExperience += 1

        progression()
        levelUp()
        xpRequirements()

        #chests
        Chest()

        backButton()

        py.display.update()

    py.quit()

if __name__ == "__game__":
    startGame()