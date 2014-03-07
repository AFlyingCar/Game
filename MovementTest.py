###########
#Tyler Robbins
#3/7/14
#Movement Test
#A script of the testing of character movement (user input)#
###########

import pygame
from pygame.locals import *
import os,sys

WHITE = (255,255,255) #set the color WHITE to a variable
BLACK = (0,0,0) #set the color BLACK to a variable

class char():
	def __init__(self, name):
		self.pos = [0,0]
		self.sprite = pygame.image.load("Images\\" + name + ".png")
		pygame.transform.scale(self.sprite, (50,50))

	def getSprite(self):
		return self.sprite

	def setPos(self, pos = [0,0]):
		self.pos = pos

	def getPos(self):
		return self.pos

char1 = char("char2")
game = True

pygame.init()

display = pygame.display.set_mode((640, 480)) #set size of window
pygame.display.set_caption("Move Me!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #make font object

while True:
	while game:
		print "loop"
		display.fill((BLACK))
		display.blit(char1.getSprite(), char1.getPos())

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

				elif event.key == K_UP:
					pos = char1.getPos()
					pos[1] -= 5
					char1.setPos(pos)

				elif event.key == K_DOWN:
					pos = char1.getPos()
					pos[1] += 5
					char1.setPos(pos)

				elif event.key == K_LEFT:
					pos = char1.getPos()
					pos[0] -= 5
					char1.setPos(pos)

				elif event.key == K_RIGHT:
					pos = char1.getPos()
					pos[0] += 5
					char1.setPos(pos)

		pygame.display.update()

nuclear = u'\u2622'