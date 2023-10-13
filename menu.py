import pygame as py
from main import *
from instructions import *
from register import *
#from login import *
from leaderboard import *

py.init()

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.display.set_caption("Fight the Storm")

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 35)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

WHITE = (255, 255, 255)
BLUE = (12, 60, 179)

buttonWidth = 300
buttonHeight = 80


playTop = infoObject.current_h / 3.3
playLeft = infoObject.current_w / 2.4
playBottom = infoObject.current_h / 3.3 + buttonHeight
playRight = infoObject.current_w / 2.4 + buttonWidth

instructionsTop = infoObject.current_h / 2.5
instructionsLeft = infoObject.current_w / 2.4
instructionsBottom = infoObject.current_h / 2.5 + buttonHeight
instructionsRight = infoObject.current_w / 2.4 + buttonWidth

loginTop = infoObject.current_h / 2
loginLeft = infoObject.current_w / 2.4
loginBottom = infoObject.current_h / 2 + buttonHeight
loginRight = infoObject.current_w / 2.4 + buttonWidth

registerTop = infoObject.current_h / 1.66
registerLeft = infoObject.current_w / 2.4
registerBottom = infoObject.current_h / 1.62 + buttonHeight
registerRight = infoObject.current_w / 2.4 + buttonWidth

leaderboardTop = infoObject.current_h / 1.3
leaderboardLeft = infoObject.current_w / 2.4
leaderboardBottom = infoObject.current_h / 1.3 + buttonHeight
leaderboardRight = infoObject.current_w / 2.4 + buttonWidth

customTop = infoObject.current_h / 2
customLeft = infoObject.current_w / 1.3
customBottom = infoObject.current_h / 2 + buttonHeight
customRight = infoObject.current_w / 1.3 + buttonWidth

run = True


def exit():
    global run, loggedIn, level, xp

    mousePos = py.mouse.get_pos()

    backTop = infoObject.current_h / infoObject.current_h + 35
    backLeft = infoObject.current_w / infoObject.current_w + 35
    backBottom = infoObject.current_h / infoObject.current_w + 35 + 70
    backRight = infoObject.current_w / infoObject.current_w + 35 + 200

    py.draw.rect(win, (255, 0, 0), (infoObject.current_w / infoObject.current_w + 35, infoObject.current_h / infoObject.current_h + 35, 200, 70))
    back = myFontBig.render("Exit", False, WHITE)
    win.blit(back, (infoObject.current_w / infoObject.current_w + 80, infoObject.current_h / infoObject.current_h + 35))

    if py.mouse.get_pressed()[0]:
        if backLeft <= mousePos[0] <= backRight and backTop <= mousePos[1] <= backBottom:

            run = False

def menu():
    global run, loggedIn
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()

        mousePos = py.mouse.get_pos()

        win.fill((16, 6, 48))

        py.draw.rect(win, (125, 125, 125), (infoObject.current_w / 4, infoObject.current_h / 12.5, 930, buttonHeight))
        title = myFontBig.render("Fight the Storm", False, WHITE)
        win.blit(title, (infoObject.current_w / 2.5, infoObject.current_h / 12))

        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 3.3, buttonWidth, buttonHeight))
        play = myFontMedium.render("Play", False, WHITE)
        win.blit(play, (infoObject.current_w / 2.1, infoObject.current_h / 3.15))

        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 2.5, buttonWidth, buttonHeight))
        instructions = myFontMedium.render("How To Play", False, WHITE)
        win.blit(instructions, (infoObject.current_w / 2.25, infoObject.current_h / 2.43))
        
        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 2, buttonWidth, buttonHeight))
        login = myFontMedium.render("Login", False, WHITE)
        win.blit(login, (infoObject.current_w / 2.14, infoObject.current_h / 1.95))

        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 1.66, buttonWidth, buttonHeight))
        register = myFontMedium.render("Register", False, WHITE)
        win.blit(register, (infoObject.current_w / 2.2, infoObject.current_h / 1.63))

        py.draw.rect(win, (255, 0, 255), (infoObject.current_w / 2.4, infoObject.current_h / 1.3, buttonWidth, buttonHeight))
        register = myFontMedium.render("Leaderboard", False, WHITE)
        win.blit(register, (infoObject.current_w / 2.28, infoObject.current_h / 1.28))
        
        py.draw.rect(win, (112, 112, 112), (infoObject.current_w / 1.3, infoObject.current_h / 2, buttonWidth, buttonHeight))
        customise = myFontMedium.render("Customise", False, WHITE)
        win.blit(customise, (infoObject.current_w / 1.25, infoObject.current_h / 1.95))

        admin()

        # if py.mouse.get_pressed()[0]:
        #     if loggedIn == 'nul':
        #         print("Login nul")
        #         toPlay = myFontBig.render("You need to login to play!", False, WHITE)
        #         win.blit(toPlay, (infoObject.current_w / 2.6, infoObject.current_h / 1.2))

        #     if loggedIn != 'nul':
        #         if playLeft <= mousePos[0] <= playRight and playTop <= mousePos[1] <= playBottom:
        #             print("Play button clicked")
        #             startGame()
        
        if py.mouse.get_pressed()[0]:
            if playLeft <= mousePos[0] <= playRight and playTop <= mousePos[1] <= playBottom:
                print("Play button clicked")
                startGame()

        if py.mouse.get_pressed()[0]:
            if instructionsLeft <= mousePos[0] <= instructionsRight and instructionsTop <= mousePos[1] <= instructionsBottom:
                print("Instructions button clicked")
                instruction()

        if py.mouse.get_pressed()[0]:
            if registerLeft <= mousePos[0] <= registerRight and registerTop <= mousePos[1] <= registerBottom:
                print("Register button clicked")
                registerUser()

        if py.mouse.get_pressed()[0]:
            if loginLeft <= mousePos[0] <= loginRight and loginTop <= mousePos[1] <= loginBottom:
                print("Login button clicked")
                loginUser()

        if py.mouse.get_pressed()[0]:
            if leaderboardLeft <= mousePos[0] <= leaderboardRight and leaderboardTop <= mousePos[1] <= leaderboardBottom:
                print("Leaderboard button clicked")
                leaderboard()

        if py.mouse.get_pressed()[0]:
            if customLeft <= mousePos[0] <= customRight and customTop <= mousePos[1] <= customBottom:
                print("Custom button clicked")
                colourChange()

        py.draw.rect(win, (64, 64, 64), (infoObject.current_w / infoObject.current_w + 15, 250, 400, 600))

        userDisplay()
        levelXPDisplay()
        levelUp()
        save()
        exit()
        currencyDisplay()

        #fps_text = myFontSmall.render("FPS:{:0.2f} ".format(fps), False, WHITE)
        #win.blit(fps_text, (infoObject.current_w - 100 , 10))

        framesPerSecond()
        
        py.display.update()

    py.quit()

menu()