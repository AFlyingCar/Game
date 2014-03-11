import pygame, sys
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
print pygame.mixer.get_init() 
screen=pygame.display.set_mode((400,400),0,32) 
channel1 = pygame.mixer.Sound("pichun.ogg")
channel1.play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            elif event.key==K_UP:
                ch = channel1.play()
                while ch.get_busy():
                    pygame.time.delay(100)
    pygame.display.update()