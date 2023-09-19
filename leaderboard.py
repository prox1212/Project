import pygame as py
import sqlite3
from backButton import *
from login import *

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
GREY = (201, 201, 199)

def displayLeaderboard():
    # Connect to the database
    connection = sqlite3.connect("user_credentials.db")
    cursor = connection.cursor()

    # Retrieve the top N players based on their level
    cursor.execute("SELECT username, level FROM users ORDER BY level DESC LIMIT 10")
    leaderboard_data = cursor.fetchall()

    # Display the leaderboard data on the screen
    yOffset = 200
    for i, (username, player_level) in enumerate(leaderboard_data, start=1):
        leaderboardEntry = myFontMedium.render(f"       {i})                {username}              -               Level {player_level}", False, GREY)
        win.blit(leaderboardEntry, (infoObject.current_w / infoObject.current_w + 35, infoObject.current_h / infoObject.current_h + yOffset))
        yOffset += 60

    # Close the database connection
    connection.close()

# Call this function in your main loop to display the leaderboard
run = True

def leaderboard():
    global run
    while run:
        py.time.delay(10)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            win.fill((16, 6, 48))

            title = myFontBig.render("Learderboard", False, WHITE)
            win.blit(title, (infoObject.current_w / infoObject.current_w + 80, infoObject.current_h / infoObject.current_h + 35))

            rank = myFontMedium.render("Rank", False, WHITE)
            win.blit(rank, (infoObject.current_w / infoObject.current_w + 80, infoObject.current_h / infoObject.current_h + 150))

            name = myFontMedium.render("Name", False, WHITE)
            win.blit(name, (infoObject.current_w / infoObject.current_w + 300, infoObject.current_h / infoObject.current_h + 150))

            level = myFontMedium.render("Level", False, WHITE)
            win.blit(level, (infoObject.current_w / infoObject.current_w + 650, infoObject.current_h / infoObject.current_h + 150))

            py.draw.rect(win, (64, 64, 64), (infoObject.current_w - 380, 250, 350, 600))

            displayLeaderboard()
            userBigDisplay()
            levelXPDisplayInvert()
            back()

        py.display.update()

    py.quit()