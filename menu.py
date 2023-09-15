import pygame as py

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
BLUE = ()

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

        py.draw.rect(win, (125, 125, 125), (infoObject.current_w / 2.4, infoObject.current_h / 12.5, 295, 100))
        title = myFontBig.render("Dodge", False, WHITE)
        win.blit(title, (infoObject.current_w / 2.2, infoObject.current_h / 12))
        

        py.display.update()

    py.quit()

menu()