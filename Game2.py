import pygame
from pygame.locals import *
from helpfunctions import text_objects,button,drawman
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

forest = pygame.image.load('images/forest.jpg')
forest = pygame.transform.scale(forest, (800, 500))
forest1 = pygame.image.load('images/forest.jpg')
forest1 = pygame.transform.scale(forest1, (800, 500))
ground = pygame.image.load('images/brown_wall.jpg')
man_right = pygame.image.load('images/man_right.png')
man_right = pygame.transform.scale(man_right,(150, 150))
dragon = pygame.image.load('images/dragon.png')
dragon = pygame.transform.scale(dragon,(150,150))
crash = pygame.image.load('images/crash.png')
crash = pygame.transform.scale(crash,(150, 150))


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
    gameloop1()

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

        button("Next Level", 150, 450, 100, 50, (0, 200, 0), (0, 255, 0), gameloop1)
        button("Quit", 550, 450, 100, 50, (255, 0, 0), (200, 0, 0), quitgame)

        pygame.display.update()
        clock.tick(15)



def background(forestx, foresty, manx, many):
    Screen.blit(forest,(forestx,foresty))
    Screen.blit(forest,(forestx+800,foresty))
    Screen.blit(ground,(0,500))
    Screen.blit(man_right,(manx,many))


def createdragon(dragonx,dragony):
    dx = -2
    dy = -2
    if dragonx in range(540,800):
        dy = -2
        dx = -2
    if dragonx in range(440,539):
        dy = 2
        dx = -2
    if dragonx in range(140,339):
        dy= -2
        dx = -2
    if dragonx in range(0,239):
        dy = 2
        dx = -2
    dragonx+=dx
    dragony+=dy
    return [dragonx,dragony]
def drawdragon(dragonx,dragony):
    Screen.blit(dragon,(dragonx,dragony))

def dragoncrash(manx,many):
    Screen.blit(crash, (manx, many))
    finishgame1("You Died",0)


def gameloop1():
    forestx = 0
    foresty = 0
    manx = 0
    many = 350
    x = 0
    y = 0
    dragonx = 650
    dragony = 350
    gameexit = False
    while not gameexit:
        for event in pygame.event.get():
            #print(event)
            if event.type==QUIT or (event.type==KEYDOWN and (event.key==K_ESCAPE) ):
                pygame.quit()
                quit()
            if event.type==KEYDOWN:
                if event.key == K_RIGHT:
                    x = -2

            elif event.type == KEYUP:
                x = 0

        forestx+=x
        foresty+=y
        manx-=x
        many-=y

        Screen.fill(black)
        background(forestx,foresty, manx, many)
        #left and right border
        if manx <= 0:
            manx = 0
        if manx >=600:
            manx = 600

        #dragon creation
        if dragonx+150<0:
            dragonx = 750
            dragony = 350
        dragonxy = createdragon(dragonx,dragony)
        drawdragon(dragonxy[0],dragonxy[1])
        dragonx = dragonxy[0]
        dragony = dragonxy[1]

        #dragoncrash
        if (manx+100>=dragonx and manx <= dragonx+100) or (manx <= dragonx+100 and manx+100 >= dragonx):
            if (many <= dragony+100 and many+100 >=dragony ) or (many <=dragony+100 and many +100 >= dragony):
                dragoncrash(manx, many)


        pygame.display.update()
        clock.tick(60)




#gameloop1()
pygame.display.update()
clock.tick(60)