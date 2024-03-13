import random
import pygame as py

class Edges:
    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
    
    def size(self):
        return (self.right - self.left, self.bottom - self.top)

class variables:
    WHITE = (255, 255, 255)
    BLUE = (12, 60, 179)

    py.font.init()
    myFont = py.font.SysFont('Comic Sans MS', 24)
    myFontMedium = py.font.SysFont('Comic Sans MS', 35)
    myFontSmall = py.font.SysFont('Comic Sans MS', 16)
    myFontBig = py.font.SysFont('Comic Sans MS', 50)

    # fullscreen
    py.init()
    infoObject = py.display.Info()
    win = py.display.set_mode((infoObject.current_w, infoObject.current_h))

    # player info
    loggedIn = 'nul'
    level = 1
    xp = 0
    xpToGo = 100
    xpToGoMultiplier = 1.2
    xpDivisor = 30
    currency = 0
    isAdmin = 0
    woodCount = 0
    coalCount = 0
    brickCount = 0
    colour = (255, 0, 255)
    setDifficulty = "Easy"
    powerLevel = 1
    powerLevelTickRate = 1200
    gameNotOver = False

    #player owned items
    red = 0
    white = 0
    orange = 0

    #woodSpawnRate = 0

    #storm
    burnerStrength = 12

    easyStrength = 12
    medStrength = 10
    hardStrength = 8

    easyPowerTick = 1200
    medPowerTick = 1000
    hardPowerTick = 800

    powerLevelTickDecayRate = 30

    strengthDecay = 3
    strengthDecayMaxPowerLevel = 2