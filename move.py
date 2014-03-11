import pygame
from pygame.locals import *
import sys

pygame.init()

display = pygame.display.set_mode((640, 480)) #set size of window
pygame.display.set_caption("Move Me!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #make font object
velX = 0
velY = 0
pos = [0,0]
img = pygame.image.load("char1.png")

while True:
    display.fill((0,0,0))
    display.blit(img, pos)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                velY += 10

            if event.key == K_UP:
                velY -= 10

            if event.key == K_LEFT:
                velX -= 10

            if event.key == K_RIGHT:
                velX += 10

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == KEYUP:
            velY = 0
            velX = 0
            
    pos[0] += velX
    pos[1] += velY
    print pos
    
    pygame.display.update()



#continuously reset the keypress
