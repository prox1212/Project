import pygame as py
from game import *
from instructions import *
from login import *
from leaderboard import *
from versionTrack import *

py.init()

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

WHITE = (255, 255, 255)
RED = (255, 0, 0)

buttonWidth = 300
buttonHeight = 80

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 35)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

playTop = infoObject.current_h / 3.3
playLeft = infoObject.current_w / 2.4
playBottom = infoObject.current_h / 3.3 + buttonHeight
playRight = infoObject.current_w / 2.4 + buttonWidth

instructionsTop = infoObject.current_h / 2.5
instructionsLeft = infoObject.current_w / 2.4
instructionsBottom = infoObject.current_h / 2.5 + buttonHeight
instructionsRight = infoObject.current_w / 2.4 + buttonWidth

loginTop = infoObject.current_h / 1.66
loginLeft = infoObject.current_w / 2.4
loginBottom = infoObject.current_h / 1.66 + buttonHeight
loginRight = infoObject.current_w / 2.4 + buttonWidth

leaderboardTop = infoObject.current_h / 2
leaderboardLeft = infoObject.current_w / 2.4
leaderboardBottom = infoObject.current_h / 2 + buttonHeight
leaderboardRight = infoObject.current_w / 2.4 + buttonWidth

run = True

def menus():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        win.fill((95, 132, 158))

        title = myFontBig.render("Lorem Ipsum", False, WHITE)
        win.blit(title, (infoObject.current_w / 2.4, infoObject.current_h / 12))

        py.draw.rect(win, (50, 168, 82), (infoObject.current_w / 2.4, infoObject.current_h / 3.3, buttonWidth, buttonHeight))
        play = myFontMedium.render("Play", False, WHITE)
        win.blit(play, (infoObject.current_w / 2.1, infoObject.current_h / 3.15))

        py.draw.rect(win, (50, 168, 82), (infoObject.current_w / 2.4, infoObject.current_h / 2.5, buttonWidth, buttonHeight))
        instructions = myFontMedium.render("How to play", False, WHITE)
        win.blit(instructions, (infoObject.current_w / 2.25, infoObject.current_h / 2.43))

        py.draw.rect(win, (50, 168, 82), (infoObject.current_w / 2.4, infoObject.current_h / 2, buttonWidth, buttonHeight))
        leaderboard = myFontMedium.render("Leaderboard", False, WHITE)
        win.blit(leaderboard, (infoObject.current_w / 2.28, infoObject.current_h / 1.95))

        py.draw.rect(win, (50, 168, 82), (infoObject.current_w / 2.4, infoObject.current_h / 1.66, buttonWidth, buttonHeight))
        login = myFontMedium.render("Login", False, WHITE)
        win.blit(login, (infoObject.current_w / 2.12, infoObject.current_h / 1.63))

        versionDisplay()
        userDisplay()

        # if loggedIn == 'null':
        #     loginRequired = myFontMedium.render("You need to login to play", False, WHITE)
        #     win.blit(loginRequired, (10, 40))
        
        # py.draw.rect(win, (50, 168, 82), (infoObject.current_w / 2.4, infoObject.current_h / 1.66, buttonWidth, buttonHeight))
        # register = myFontMedium.render("Register", False, WHITE)
        # win.blit(register, (infoObject.current_w / 2.18, infoObject.current_h / 1.63))

        if py.mouse.get_pressed()[0]:
            if playLeft <= mousePos[0] <= playRight and playTop <= mousePos[1] <= playBottom:
                print("Play button clicked")
                startGame()

                # if loggedIn == 'null':
                #     loginRequired = myFontMedium.render("You need to login to play", False, RED)
                #     win.blit(loginRequired, (10, 40))
                
                # else:
                #     startGame()

            if instructionsLeft <= mousePos[0] <= instructionsRight and instructionsTop <= mousePos[1] <= instructionsBottom:
                print("Instructions button clicked")
                instructionsPage()

            if loginLeft <= mousePos[0] <= loginRight and loginTop <= mousePos[1] <= loginBottom:
                print("Login button clicked")
                login_register()

            if leaderboardLeft <= mousePos[0] <= leaderboardRight and leaderboardTop <= mousePos[1] <= leaderboardBottom:
                print("Leaderboard button clicked")
                leaderboardDisplay()

        py.display.update()

    py.quit()

menus()
