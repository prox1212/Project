import pygame as py

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 19)

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

WHITE = (255, 255, 255)

def versionDisplay():
    version = myFont.render("Version 1.13", False, WHITE)
    win.blit(version, (2, infoObject.current_h - 25))