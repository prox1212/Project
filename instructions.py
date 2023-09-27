import pygame as py
from instructions import *
#from login import userDisplay
from backButton import *
from main import userDisplay

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

run = True

def instruction():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        win.fill((16, 6, 48))

        userDisplay()

        back()

        py.display.update()

    py.quit()