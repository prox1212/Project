import pygame as py
#from menu import *

py.init()

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

WHITE = (255, 255, 255)

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 35)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

buttonWidth = 300
buttonHeight = 80

menuTop = infoObject.current_h / 3.3
menuLeft = infoObject.current_w / 2.4
menuBottom = infoObject.current_h / 3.3 + buttonHeight
menuRight = infoObject.current_w / 2.4 + buttonWidth

run = True

def options():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        mousePos = py.mouse.get_pos()

        win.fill((95, 132, 158))

        py.draw.rect(win, (50, 168, 82), (infoObject.current_w / 2.4, infoObject.current_h / 3.3, buttonWidth, buttonHeight))
        menu = myFontMedium.render("Menu", False, WHITE)
        win.blit(menu, (infoObject.current_w / 2.1, infoObject.current_h / 3.15))

        if py.mouse.get_pressed()[0]:
            if menuLeft <= mousePos[0] <= menuRight and menuTop <= mousePos[1] <= menuBottom:
                print("Menu button clicked")
                #menus()

        py.display.update()

    py.quit()



