import pygame as py
from instructions import *
#from login import userDisplay
from backButton import *
from main import userDisplay

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

clock = py.time.Clock()
desiredFps = 165

run = True

def instruction():
    global run
    while run:
        py.time.delay(10)

        #clock.tick(desiredFps)
        fps = int(clock.get_fps())

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        win.fill((16, 6, 48))

        userDisplay()

        back()

        fps_text = myFont.render(f'FPS: {fps}', True, (255, 255, 255))
        win.blit(fps_text, (infoObject.current_w - 100 , 10))

        py.display.update()

    py.quit()