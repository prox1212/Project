import pygame as py
from vars import Edges

py.init()

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 35)
myFontBig = py.font.SysFont('Comic Sans MS', 50)

WHITE = (255, 255, 255)

run = True

def back():
    global run

    mousePos = py.mouse.get_pos()
    keys = py.key.get_pressed()

    back_edges = Edges(infoObject.current_w / 1.13, infoObject.current_w / 1.13 + 200, infoObject.current_h / 1.09 + 70, infoObject.current_h / 1.09)

    py.draw.rect(win, (255, 0, 0), (infoObject.current_w / 1.13, infoObject.current_h / 1.09, 200, 70))
    back = myFontBig.render("Back", False, WHITE)
    win.blit(back, (infoObject.current_w / 1.1, infoObject.current_h / 1.09))

    if py.mouse.get_pressed()[0]:
        if back_edges.left <= mousePos[0] <= back_edges.right and back_edges.top <= mousePos[1] <= back_edges.bottom:
            import menu
            menu.menu()
            run = False

        if keys[py.K_ESCAPE]:
            import menu
            menu.menu()
            run = False