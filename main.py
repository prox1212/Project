import pygame as py

py.init()

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

py.display.set_caption("Dodge em all")

#player info
width = 35
height = 35

pos_x = 0
pos_y = 120

velocity = 2.5
velocityDiagonal = 0.2

run = True

def startGame():
    global pos_x, pos_y
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()

        if keys[py.K_LEFT] or keys[py.K_a] and pos_x > 0:
            pos_x -= velocity

        if keys[py.K_RIGHT] or keys[py.K_d] and pos_x < infoObject.current_w - width:
            pos_x += velocity

        if keys[py.K_UP] or keys[py.K_w] and pos_y > 0:
            pos_y -= velocity

        if keys[py.K_DOWN] or keys[py.K_s] and pos_y < infoObject.current_h - height:
            pos_y += velocity

        win.fill((16, 6, 48))

        py.draw.rect(win, (255, 0, 255), (pos_x, pos_y, width, height))

        py.display.update()

    py.quit()

if __name__ == "__main__":
    startGame()