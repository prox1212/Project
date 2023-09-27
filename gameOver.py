import pygame as py

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

WHITE = (255, 255, 255)

def exit():
    global run

    mousePos = py.mouse.get_pos()

    backTop = infoObject.current_h / 4
    backLeft = infoObject.current_w / 2.3
    backBottom = infoObject.current_h / 4 + 70
    backRight = infoObject.current_w / 2.3 + 200

    py.draw.rect(win, (255, 0, 0), (infoObject.current_w / 2.3, infoObject.current_h / 4, 200, 70))
    back = myFontBig.render("Exit", False, WHITE)
    win.blit(back, (infoObject.current_w / 2.2, infoObject.current_h / 4))

    if py.mouse.get_pressed()[0]:
        if backLeft <= mousePos[0] <= backRight and backTop <= mousePos[1] <= backBottom:

            run = False

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
        win.blit(title, (infoObject.current_w / 2.3, 60))

        body = myFont.render("Your level progression has been saved.", False, WHITE)
        win.blit(body, (infoObject.current_w / 2.9, 165))

        exit()

        py.display.update()

    py.quit()
