import pygame as py
from main import *
from instructions import *

py.init()

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.display.set_caption("Dodge em all")

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 35)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

WHITE = (255, 255, 255)
BLUE = (12, 60, 179)

buttonWidth = 295
buttonHeight = 100


playTop = infoObject.current_h / 4
playLeft = infoObject.current_w / 2.4
playBottom = infoObject.current_h / 4 + buttonHeight
playRight = infoObject.current_w / 2.4 + buttonWidth

instructionsTop = infoObject.current_h / 2.7
instructionsLeft = infoObject.current_w / 2.4
instructionsBottom = infoObject.current_h / 2.7 + buttonHeight
instructionsRight = infoObject.current_w / 2.4 + buttonWidth

loginTop = infoObject.current_h / 2.03
loginLeft = infoObject.current_w / 2.4
loginBottom = infoObject.current_h / 2.03 + buttonHeight
loginRight = infoObject.current_w / 2.4 + buttonWidth

registerTop = infoObject.current_h / 1.62
registerLeft = infoObject.current_w / 2.4
registerBottom = infoObject.current_h / 1.62 + buttonHeight
registerRight = infoObject.current_w / 2.4 + buttonWidth


run = True

def menu():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        win.fill((16, 6, 48))

        py.draw.rect(win, (125, 125, 125), (infoObject.current_w / 4, infoObject.current_h / 12.5, 930, buttonHeight))
        title = myFontBig.render("Dodge", False, WHITE)
        win.blit(title, (infoObject.current_w / 2.2, infoObject.current_h / 12))

        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 4, buttonWidth, buttonHeight))
        play = myFontBig.render("Play", False, WHITE)
        win.blit(play, (infoObject.current_w / 2.13, infoObject.current_h / 3.9))

        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 2.7, buttonWidth, buttonHeight))
        instructions = myFontBig.render("Instructions", False, WHITE)
        win.blit(instructions, (infoObject.current_w / 2.4, infoObject.current_h / 2.6))
        
        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 2.03, buttonWidth, buttonHeight))
        login = myFontBig.render("Login", False, WHITE)
        win.blit(login, (infoObject.current_w / 2.18, infoObject.current_h / 2))

        py.draw.rect(win, (BLUE), (infoObject.current_w / 2.4, infoObject.current_h / 1.62, buttonWidth, buttonHeight))
        register = myFontBig.render("Register", False, WHITE)
        win.blit(register, (infoObject.current_w / 2.28, infoObject.current_h / 1.6))

        if py.mouse.get_pressed()[0]:
            if playLeft <= mousePos[0] <= playRight and playTop <= mousePos[1] <= playBottom:
                print("Play button clicked")
                startGame()

        if py.mouse.get_pressed()[0]:
            if instructionsLeft <= mousePos[0] <= instructionsRight and instructionsTop <= mousePos[1] <= instructionsBottom:
                print("Instructions button clicked")
                instruction()
        

        py.display.update()

    py.quit()

menu()