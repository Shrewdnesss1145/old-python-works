import pygame
pygame.init()
pygame.display.set_caption('sb')
screen = pygame.display.set_mode(( 800,600))
gtx = pygame.image.load('image/gtx.png')
x=100
y=200
speed_x=2
speed_y=2
while True:
    screen.fill((255,250,150))
    screen.blit(gtx,(x,y))
    x+=1
    if x>=600 or x<=0:
        speed_x=-speed_x
    if y>=600 or y<=
    for i in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    pygame.display.update()
    pygame.time.Clock().tick(60)
    