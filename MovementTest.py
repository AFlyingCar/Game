#############################################################
#Tyler Robbins											    #
#3/7/14											   		    #
#Movement Test											    #
#A script of the testing of character movement (user input).#
#############################################################

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
		self.shoot = False
		self.speed = 5
		self.hitbox = pygame.image.load("Images//hitbox.png")
		self.default = pygame.image.load("Images\\default.png")
		self.sprite = pygame.image.load("Images\\" + name + ".png")
		#pygame.transform.scale(self.sprite, (50,50))

	def getSprite(self):
		return self.sprite

	def setPos(self, pos):
		self.pos = pos

	def getPos(self):
		return self.pos

	def setFocus(self, TF):
		self.focus = TF

	def getFocus(self):
		if self.focus:
			self.speed = 1
			return [self.hitbox, self.speed]
		else:
			self.speed = 5
			return [self.default, self.speed]

	def getMove(self):
		return self.move

	def setMove(self, TF):
		self.move = TF

	def setShoot(self, TF):
		self.shoot = TF

x = raw_input("Character (1,2): ")

uchar = char("char" + x)
game = True
velY = 0
velX = 0
pos = [0,0]

pygame.init()

display = pygame.display.set_mode((640, 480)) #set size of window
pygame.display.set_caption("Move Me!") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #make font object

while True:
	while game:
		display.fill((BLACK))
		display.blit(uchar.getSprite(), uchar.getPos())
		display.blit(uchar.getFocus()[0], (uchar.getPos()[0] + 86, uchar.getPos()[1] + 185))

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			######Define key events######
			if event.type == KEYDOWN:

				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

				if event.key == K_UP:
					velY = -uchar.getFocus()[1]

				if event.key == K_DOWN:
					velY = uchar.getFocus()[1]

				if event.key == K_LEFT:
					velX = -uchar.getFocus()[1]

				if event.key == K_RIGHT:
					velX = uchar.getFocus()[1]

				if event.key == K_LSHIFT:
					print "FOCUS!"
					uchar.setFocus(True)

				if event.key == K_z:
					uchar.setShoot(True)

			if event.type == KEYUP:
				velY = 0
				velX = 0
				uchar.setFocus(False)
				uchar.setShoot(False)

		######Update player position######
		pos[1] += velY
		pos[0] += velX
		uchar.setPos(pos)
		print uchar.getPos()
		
		######Update Display######
		pygame.display.update()

nuclear = u'\u2622'