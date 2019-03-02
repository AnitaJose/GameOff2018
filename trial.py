import pygame
from pygame.locals import *
from helpfunctions import text_objects,button,drawbackground,drawman
from Game2 import gameloop1
import random,time

pygame.init()
#Make screen and background
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)




Screen=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Trial!!')
clock = pygame.time.Clock()


wolf_left = pygame.image.load('images/wolf_left.png')
wolf_left = pygame.transform.scale(wolf_left,(50, 50))
wolf_right = pygame.image.load('images/wolf_right.png')
wolf_right = pygame.transform.scale(wolf_right,(50, 50))
wolf_climbing_up = pygame.image.load('images/wolf_climbing_up.png')
wolf_climbing_up = pygame.transform.scale(wolf_climbing_up,(50, 50))
wolf_climbing_down = pygame.image.load('images/wolf_climbing_down.png')
wolf_climbing_down = pygame.transform.scale(wolf_climbing_down,(50, 50))
crash = pygame.image.load('images/crash.png')
crash = pygame.transform.scale(crash,(50, 50))


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Screen.fill((255,255,255))
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("Hybrid Games", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        Screen.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, (0,200,0), (0,255,0), gameloop)
        button("Quit", 550, 450, 100, 50, (255,0,0), (200,0,0), quitgame)

        pygame.display.update()
        clock.tick(15)

def paused(pause):
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    Screen.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue", 150, 450, 100, 50, (0,200,0), (0,255,0), unpause)
        button("Quit", 550, 450, 100, 50, (255,0,0), (200,0,0), quitgame)

        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause=False
    gameloop()

def quitgame():
    pygame.quit()
    quit()

def finishgame1(msg,won):
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects(msg, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    Screen.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)
        if won == 1:
            button("Play Again", 150, 450, 100, 50, (0, 200, 0), (0, 255, 0), gameloop1)
            button("Quit", 550, 450, 100, 50, (255, 0, 0), (200, 0, 0), quitgame)
        else:
            button("Next Level", 150, 450, 100, 50, (0, 200, 0), (0, 255, 0), gameloop)
            button("Quit", 550, 450, 100, 50, (255, 0, 0), (200, 0, 0), quitgame)

        pygame.display.update()
        clock.tick(15)


def manycheck(manx, many):
    if many <= 550 and many + 50 > 550 and ((manx >= 50 and manx + 50 <= 600) or (manx >= 650)):
        many = 550
    if many < 500 and many + 50 >= 500 and ((manx >= 50 and manx + 50 <= 600) or (manx >= 650)):
        many = 450
    if many <= 450 and many + 50 > 450 and ((manx >= 0 and manx + 50 <= 400) or (manx >= 450)):
        many = 450
    if many < 400 and many + 50 >= 400 and ((manx >= 0 and manx + 50 <= 400) or (manx >= 450)):
        many = 350
    if many <= 350 and many + 50 > 350 and ((manx >= 0 and manx + 50 <= 100) or (manx >= 150 and manx + 50 <= 750)):
        many = 350
    if many < 300 and many + 50 >= 300 and ((manx >= 0 and manx + 50 <= 100) or (manx >= 150 and manx + 50 <= 750)):
        many = 250
    if many <= 250 and many + 50 > 250 and ((manx >= 0 and manx + 50 <= 550) or (manx >= 600)):
        many = 250
    if many < 200 and many + 50 >= 200 and ((manx >= 0 and manx + 50 <= 550) or (manx >= 600)):
        many = 150
    if many <= 150 and many + 50 > 150 and (
            (manx >= 0 and manx + 50 <= 350) or (manx >= 400 and manx + 50 <= 700) or (manx >= 750)):
        many = 150
    if many < 100 and many + 50 >= 100 and (
            (manx >= 0 and manx + 50 <= 350) or (manx >= 400 and manx + 50 <= 700) or (manx >= 750)):
        many = 50
    if many <= 50 and many + 50 > 50 and ((manx >= 0 and manx + 50 <= 750)):
        many = 50
    return many

def manxcheck(x, many):
    if many in range(460, 530):
        x = 0
    if many in range(360,430):
        x = 0
    if many in range(260,330):
        x=0
    if many in range(160,230):
        x = 0
    if many in range(60,130):
        x = 0
    if many in range(0,49):
        x = 0
    return x



def enemyposCheck(wolfx,wolfy):
    side=0
    wx = 2
    wy = 2

    if wolfy in range(0,51):
        wx = 0
        side = 0
    if wolfy in range(51,100):
        wy = 0
        wx = -2
        side = 2
        if wolfx == 700:
            wy = 2
            wx = 0
            side = 0
    if wolfy in range(100,151):
        wx = 0
        side = 0
    if wolfy in range(151,200):
        wy = 0
        wx = -2
        side = 2
        if wolfx == 550:
            wy = 2
            wx = 0
            side = 0
    if wolfy in range(200,251):
        wx = 0
        side = 0
    if wolfy in range(251,300):
        wy = 0
        wx = 2
        side = 3
        if wolfx == 750:
            wy = 2
            wx = 0
            side = 0
    if wolfy in range(300,351):
        wx = 0
        side = 0
    if wolfy in range(351,400):
        wy = 0
        wx = -2
        side = 2
        if wolfx == 400:
            wy = 2
            wx = 0
            side = 0
    if wolfy in range(400,451):
        wx = 0
        side = 0
    if wolfy in range(451,500):
        wy = 0
        wx = 2
        side = 3
        if wolfx == 600:
            wy = 2
            wx = 0
            side = 0
    if wolfy in range(500,551):
        wx = 0
        side = 0
    if wolfy == 550:
        wy = 0
        wx = 2
        side = 3
        if wolfx == 750:
            wx = 2
            wy = 0
            side = 2

    wolfx+=wx
    wolfy+=wy

    pack = [wolfx, wolfy, side]
    return pack

def createEnemy(wolfx, wolfy,side):
    if side == 0:
        Screen.blit(wolf_climbing_down,(wolfx, wolfy))
    if side == 1:
        Screen.blit(wolf_climbing_up,(wolfx, wolfy))
    if side == 2:
        Screen.blit(wolf_left,(wolfx, wolfy))
    if side == 3:
        Screen.blit(wolf_right,(wolfx, wolfy))

def manWolfCrash(manx, many):
    Screen.blit(crash,(manx, many))
    return [750,550]

def gameloop():
    manx = 750
    many = 550
    manside = 0
    x=0
    y=0
    wolfx = 750
    wolfy = 0
    wx = 2
    wy = 2
    manWolfCrashnumber = 0
    gameexit = False
    while not gameexit:
        for event in pygame.event.get():
            #print(event)
            if event.type==QUIT or (event.type==KEYDOWN and (event.key==K_ESCAPE) ):
                pygame.quit()
                quit()

            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    manside = 1
                    x=-2
                    y=0
                elif event.key==K_RIGHT:
                    manside = 2
                    x=2
                    y=0
                elif event.key==K_UP:
                    manside = 3
                    x=0
                    y=-2
                elif event.key==K_DOWN:
                    manside = 3
                    x=0
                    y=2
                if event.key == pygame.K_p:
                    pause = True
                    paused(pause)
            elif event.type==KEYUP:
                x=0
                y=0

        x = manxcheck(x,many)
        manx+=x
        many+=y

        Screen.fill(black)
        drawbackground()
        drawman(manx,many,manside)

        #left and right borders
        if manx>display_width-50:
            manx=750
        elif manx<0:
            manx = 0

        #top and bottom borders
        if many>display_height-50:
            many = 550
        elif many<0:
            many = 0

        #brick borders
        many = manycheck(manx, many)

        #enemy creation
        pack = enemyposCheck(wolfx, wolfy)
        createEnemy(pack[0], pack[1],pack[2])
        wolfx = pack[0]
        wolfy = pack[1]
        if wolfy in range (540,600) and wolfx >= 780:
            wolfy = 0
            wolfx = 750
            pack = enemyposCheck(wolfx, wolfy)
            createEnemy(pack[0], pack[1], pack[2])
            wolfx = pack[0]
            wolfy = pack[1]

        #crash of man and wolf
        if (manx<=wolfx+50 and manx+50 >= wolfx) or (manx+50 >= wolfx and manx<=wolfx+50):
            if (many<=wolfy+50 and many+50>=wolfy ) or (many+50 >= wolfy and many <= wolfy+50):
                newpos = manWolfCrash(manx,many)
                manx = newpos[0]
                many = newpos[1]
                manWolfCrashnumber+=1
                if manWolfCrashnumber == 3:
                    finishgame1("Game Over!!!",0)
                    manWolfCrashnumber = 0

        #finish line
        if many == 0:
            finishgame1("You Won!!!",1)

        pygame.display.update()
        clock.tick(60)



game_intro()
gameloop()
pygame.display.update()
clock.tick(60)