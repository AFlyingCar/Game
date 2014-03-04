#Tyler Robbins
#2/27/14
#Boss Fight Test

import pygame
from pygame.locals import *
import platform as plat
import sys

if str(plat.system()) == "Windows":
	slash = "\\"
else:
	slash = "//"

WHITE = (255,255,255) #set the color WHITE to a variable

class SpC():
	def __init__(self, names = []):
		self.slist = []
		for item in names:
			self.slist.append(item)

	def setPat(self, bamt, dire):
		blist = []
		for i in range(bamt):
			x = bullet()
			x.attr = i
			blist.append(x)


	def getSpCName(self):
		return self.slist

class bullet():
	def __init__(self):
		self.color = (255,25,200)

	def move(self):
		pass

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

class Boss():
	def __init__(self, name, SPCamt, music, spells = []):
		self.health = 1000000
		self.name = name
		self.spellamt = SPCamt
#		self.image = pygame.image.load("Images" + slash + name + ".png").convert_alpha()
		self.music = music
		self.spells = spells

	def getHealth(self):
		return self.health

	def getImage(self):
		return self.image

	def shoot(self, bamt):
		pass

class player():
	def __init__(self, name):
		self.pos = (20,40)
		self.sprite = pygame.image.load("Images" + slash + name + ".png").convert_alpha()

	def move(self, key):
		if key == K_DOWN:
			while key == K_DOWN:
				self.pos[1] -= 1

		elif key == K_LEFT:
			while key == K_LEFT:
				self.pos[0] -= 1

		elif key == K_RIGHT:
			while key == K_LEFT:
				self.pos[0] += 1

		elif key == K_UP:
			while key == K_UP:
				self.pos[1] += 1

	def getImg(self):
		return self.sprite

	def getPos(self):
		return self.pos

b6Cards = SpC(["light", "thunder"])
#b6Cards.setPat(15, "")
b6 = Boss("zeus", 2, "")

p1 = player("char1")
pSprite = pygame.image.load(p1.getImg())

pygame.init()

display = pygame.display.set_mode((640, 480))
display.fill((WHITE))
pygame.display.set_caption("BOSS FIGHT")
fontObj = pygame.font.Font('freesansbold.ttf', 29)

while True:
	print "loop1"
	display.blit(pSprite, (p1.getPos()))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == KEYDOWN:
			print "keydown"
			p1.move(event.key)

	pygame.display.update()

nuclear = u'\u2622'