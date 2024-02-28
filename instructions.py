import pygame as py
#from login import userDisplay
from backButton import *

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

run = True

def instruction():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        win.fill((16, 6, 48))

        head = myFontBig.render("How to play", False, WHITE)
        win.blit(head, (15, 15))

        body = myFontMedium.render("1) Use W A S D to move", False, WHITE)
        win.blit(body, (15, 100))

        body = myFontMedium.render("2) Move over objects to pick them up", False, WHITE)
        win.blit(body, (15, 145))

        body = myFontMedium.render("3) Move to the Burner to deposit materials using E F G", False, WHITE)
        win.blit(body, (15, 190))

        body = myFontMedium.render("4) Keep the burner healthy and strong", False, WHITE)
        win.blit(body, (15, 235))

        body = myFontMedium.render("5) Last as long as you can to gain Experience", False, WHITE)
        win.blit(body, (15, 280))

        import menu
        menu.userDisplay()

        back()

        py.display.update()

    py.quit()