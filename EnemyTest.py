#Tyler Robbins
#2/18/14
#Enemy Test
#Testing AI movements

from pygame.locals import *
import pygame, sys, os
import platform as plat

if str(plat.system()) == "Windows":
	slash = "\\"
else:
	slash = "//"

class Entity():
	def __init__(self, speed, loc):
		self.speed = speed
		self.health = 10
		self.loc = loc
		self.image = pygame.image.load("Images" + slash + "blank.png").convert_alpha()
		self.ihitbox = pygame.image.load("Images" + slash + "hitbox.png").convert_alpha()

	def getHealth(self):
		return self.health

	def move(self, loc, dest):
		for item in loc:
			loc1 = loc.index(item)
	
			if item > dest[loc1]:
				while item > dest[loc1]:
					item -= 1
	
			elif item < dest[loc1]:
				while item < dest[loc1]:
					item += 1
	
			loc[loc1] = item

		return dest

	def setImage(self, image):
		self.image = image

	def getImage(self):
		return self.image

num = 0
enemylist = []
for i in range(2):
	num += 1
	enemy = Entity(1, [250, 250])
	enemy.attr = i
	enemylist.append(enemy)

pygame.init()




nuclear = u'\u2622'