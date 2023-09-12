import pygame as py
import random

py.init()

brightcoreX = random.randint(60,1200)
brightcoreY = random.randint(70, 900)
brightcoreHealthX = brightcoreX - 10
brightcoreHealthY = brightcoreY + 60
brightcoreSizeX = 60
brightcoreSizeY = 60

pos_x = 0
pos_y = 115

width = 35
height = 35

player_left = pos_x
player_right = pos_x + width
player_top = pos_y
player_bottom = pos_y + height

brightcore_left = brightcoreX
brightcore_right = brightcoreX + brightcoreSizeX
brightcore_top = brightcoreSizeY
brightcore_bottom = brightcoreY + brightcoreSizeY

WHITE = (255, 255, 255)

brightcoreHealth = 2000

py.font.init()
myFont = py.font.SysFont('Comic Sans MS', 16)
myFontMedium = py.font.SysFont('Comic Sans MS', 19)
myFontBig = py.font.SysFont('Comic Sans MS', 22)

infoObject = py.display.Info()
win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

def update_player_pos(new_x,new_y):
    global pos_x,pos_y,player_left,player_right,player_bottom,player_top

    pos_x = new_x
    pos_y = new_y

    player_left = pos_x
    player_right = pos_x + width
    player_top = pos_y
    player_bottom = pos_y + height

def spawnBrightcore():
    brightcore = py.image.load('Assets/brightcore.png')
    displayBrightcore = py.transform.scale(brightcore, (brightcoreSizeX,brightcoreSizeY))
    win.blit(displayBrightcore, (brightcoreX, brightcoreY))

def brightcoreDisplayHealth():
    global player_left, player_right, player_top, player_bottom, brightcore_left, brightcore_right, brightcore_top, brightcore_bottom, brightcoreHealth

    displaybrightcoreHealth = myFont.render('Health: ' + str(brightcoreHealth), True, WHITE)
    win.blit(displaybrightcoreHealth, (brightcoreHealthX, brightcoreHealthY))
    if player_right >= brightcore_left and player_left <= brightcore_right and player_bottom >= brightcore_top and player_top <= brightcore_bottom:
        brightcoreHealth - 50

