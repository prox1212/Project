import pygame as py
from login import *
from backButton import *

py.init()

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 35)
myFontMedium = py.font.SysFont('Comic Sans MS', 24)
myFontSmall = py.font.SysFont('Comic Sans MS', 16)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.display.set_caption("Dodge em all")

run = True

def gameOver():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        win.fill((16, 6, 48))

        title = myFontBig.render("Game Over", False, WHITE)
        win.blit(title, (infoObject.current_w / 2, 60))

        back()

        py.display.update()

    py.quit()
