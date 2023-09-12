import pygame as py
from options import *
from versionTrack import *

py.init()

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

WHITE = (255, 255, 255)

backButtonW = 120
backButtonH = 80
backButtonX = infoObject.current_w - backButtonW - 10
backButtonY = 10

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 19)
myFontMedium = py.font.SysFont('Comic Sans MS', 35)
myFontBig = py.font.SysFont('Comic Sans MS', 50)
myFontObease = py.font.SysFont('Comic Sans MS', 35)

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

def instructionsPage():
    global run
    while run:
        py.time.delay(10)

        mousePos = py.mouse.get_pos()

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        win.fill((95, 132, 158))

        header = myFontBig.render("How to play", False, WHITE)
        win.blit(header, (20, 20))

        body = myFont.render("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod"
                             "tempor incididunt ut labore et dolore magna aliqua.", False, WHITE)
        
        body2 = myFont.render("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi"
                              "ut aliquip ex ea commodo consequat.", False, WHITE)

        body3 = myFont.render("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu"
                              "fugiat nulla pariatur.", False, WHITE)
        
        body4 = myFont.render("Excepteur sint occaecat cupidatat non proident, sunt in culpa"
                              "qui officia deserunt mollit anim id est laborum.", False, WHITE)
        win.blit(body, (20, 130))
        win.blit(body2, (20, 160))
        win.blit(body3, (20, 190))
        win.blit(body4, (20, 220))
    
        backButton()

        versionDisplay()

        py.display.update()

    py.quit()