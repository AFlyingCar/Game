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
		self.focus = False
		self.move = True
		self.hitbox = pygame.image.load("Images\\hitbox.png")
		self.default = pygame.image.load("Images\\default.png")
		self.sprite = pygame.image.load("Images\\" + name + ".png")
		#pygame.transform.scale(self.sprite, (50,50))

	def getSprite(self):
		return self.sprite

	def setPos(self, pos = [0,0]):
		self.pos = pos

	def getPos(self):
		return self.pos

	def setFocus(self, TF):
		self.focus = TF

	def getFocus(self):
		if self.focus:
			return self.hitbox
		else:
			return self.default

	def getMove(self):
		return self.move

	def setMove(self, TF):
		self.move = TF

x = raw_input("Character (1,2): ")

uchar = char("char" + x)
game = True

pygame.init()

display = pygame.display.set_mode((640, 480)) #set size of window
pygame.display.set_caption("Move Me!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #make font object

while True:
	while game:
		print "loop"
		display.fill((BLACK))
		display.blit(uchar.getSprite(), uchar.getPos())
#		display.blit(uchar.getFocus(), uchar.getPos())

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

				elif event.key == K_UP:
					pos = uchar.getPos()
					pos[1] -= 5
					uchar.setPos(pos)

				elif event.key == K_DOWN:
					pos = uchar.getPos()
					pos[1] += 5
					uchar.setPos(pos)

				elif event.key == K_LEFT:
					#while uchar.getMove():
					#	if event.key != K_LEFT:
					#		uchar.setMove(False)
					#	else:
					pos = uchar.getPos()
					pos[0] -= 5
					uchar.setPos(pos)
					uchar.setMove(True)

				elif event.key == K_RIGHT:
					pos = uchar.getPos()
					pos[0] += 5
					uchar.setPos(pos)

				elif event.key == K_RSHIFT or event.key == L_SHIFT:
					if event.key == K_RSHIFT or event.key == L_SHIFT:
						char1.setFocus(True)
					else:
						char1.setFocus(False)

		pygame.display.update()

nuclear = u'\u2622'