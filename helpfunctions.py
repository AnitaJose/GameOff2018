import pygame

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)

Screen=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Trial!!')
clock = pygame.time.Clock()

brick = pygame.image.load('images/brick.jpg')
brick = pygame.transform.scale(brick, (50, 50))
ladder = pygame.image.load('images/ladder.jpg')
ladder = pygame.transform.scale(ladder,(50,100))
man_straight = pygame.image.load('images/man_straight.png')
man_straight = pygame.transform.scale(man_straight,(50, 50))
man_right = pygame.image.load('images/man_right.png')
man_right = pygame.transform.scale(man_right,(50, 50))
man_left = pygame.image.load('images/man_left.png')
man_left = pygame.transform.scale(man_left,(50, 50))
man_back = pygame.image.load('images/man_back.png')
man_back = pygame.transform.scale(man_back,(50, 50))


def text_objects(text, font):
    textSurface = font.render(text, True, (0,128,0))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(Screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(Screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    Screen.blit(textSurf, textRect)

def drawbackground():

    for i in range(0,750,50):
        Screen.blit(brick,(i,0))
    Screen.blit(ladder,(750,0))
    for i in range(50,350,50):
        Screen.blit(brick,(i,100))
    Screen.blit(ladder, (0, 100))
    Screen.blit(ladder, (350, 100))
    for i in range(400,700,50):
        Screen.blit(brick, (i, 100))
    Screen.blit(ladder, (700, 100))
    for i in range(750, 800, 50):
        Screen.blit(brick, (i, 100))
    for i in range(0,550,50):
        Screen.blit(brick,(i, 200))
    Screen.blit(ladder, (550, 200))
    for i in range(600,800,50):
        Screen.blit(brick,(i,200))
    for i in range(0,100,50):
        Screen.blit(brick,(i,300))
    Screen.blit(ladder, (100, 300))
    for i in range(150,750,50):
        Screen.blit(brick,(i,300))
    Screen.blit(ladder, (750, 300))
    for i in range(0,400,50):
        Screen.blit(brick,(i,400))
    Screen.blit(ladder, (400, 400))
    for i in range(450,800,50):
        Screen.blit(brick,(i,400))
    for i in range(50,600,50):
        Screen.blit(brick,(i,500))
    Screen.blit(ladder, (0, 500))
    Screen.blit(ladder, (600, 500))
    for i in range(650,800,50):
        Screen.blit(brick,(i,500))

def drawman(manx,many,manside):
    if manside == 0:
        Screen.blit(man_straight,(manx, many))
    elif manside == 1:
        Screen.blit(man_left,(manx, many))
    elif manside == 2:
        Screen.blit(man_right,(manx, many))
    elif manside == 3:
        Screen.blit(man_back,(manx,many))
