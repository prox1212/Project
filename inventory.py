import pygame as py

py.init()

WHITE = (255, 255, 255)

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 19)
myFontBig = py.font.SysFont('Comic Sans MS', 22)

#fullscreen
infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

selected_slot = 0

slot1 = myFontMedium.render('1', True, WHITE)
slot2 = myFontMedium.render('2', True, WHITE)
slot3 = myFontMedium.render('3', True, WHITE)
slot4 = myFontMedium.render('4', True, WHITE)
slot5 = myFontMedium.render('5', True, WHITE)

slot1_rect = py.Rect(10, 10, 100, 90)
slot2_rect = py.Rect(120, 10, 100, 90)
slot3_rect = py.Rect(230, 10, 100, 90)
slot4_rect = py.Rect(340, 10, 100, 90)
slot5_rect = py.Rect(450, 10, 100, 90)

colour = py.Color(61, 59, 54)
selected_colour = py.Color(38, 37, 34)

def inventory():
    global selected_slot

    keys = py.key.get_pressed()

    if keys[py.K_1]:
        selected_slot = 1
    elif keys[py.K_2]:
        selected_slot = 2
    elif keys[py.K_3]:
        selected_slot = 3
    elif keys[py.K_4]:
        selected_slot = 4
    elif keys[py.K_5]:
        selected_slot = 5

    py.draw.rect(win, (89, 98, 112), (0, 0, 560, 110))
    py.draw.rect(win, (61, 59, 54), (10, 10, 100, 90))
    py.draw.rect(win, (61, 59, 54), (120, 10, 100, 90))
    py.draw.rect(win, (61, 59, 54), (230, 10, 100, 90))
    py.draw.rect(win, (61, 59, 54), (340, 10, 100, 90))
    py.draw.rect(win, (61, 59, 54), (450, 10, 100, 90))
    win.blit(slot1, (50, 100))
    win.blit(slot2, (160, 100))
    win.blit(slot3, (270, 100))
    win.blit(slot4, (380, 100))
    win.blit(slot5, (490, 100))

    if selected_slot == 1:
        py.draw.rect(win, (38, 37, 34), (10, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (120, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (230, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (340, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (450, 10, 100, 90))
    elif selected_slot == 2:
        py.draw.rect(win, (61, 59, 54), (10, 10, 100, 90))
        py.draw.rect(win, (38, 37, 34), (120, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (230, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (340, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (450, 10, 100, 90))
    elif selected_slot == 3:
        py.draw.rect(win, (61, 59, 54), (10, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (120, 10, 100, 90))
        py.draw.rect(win, (38, 37, 34), (230, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (340, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (450, 10, 100, 90))
    elif selected_slot == 4:
        py.draw.rect(win, (61, 59, 54), (10, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (120, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (230, 10, 100, 90))
        py.draw.rect(win, (38, 37, 34), (340, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (450, 10, 100, 90))
    elif selected_slot == 5:
        py.draw.rect(win, (61, 59, 54), (10, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (120, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (230, 10, 100, 90))
        py.draw.rect(win, (61, 59, 54), (340, 10, 100, 90))
        py.draw.rect(win, (38, 37, 34), (450, 10, 100, 90)) 