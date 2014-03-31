#Tyler Robbins
#3/30/14
#Sprites
#Define classes of every entity

import pygame
from pygame.locals import *

class Collidable(pygame.sprite.Sprite):
	def __init__(self, *groups):
		pygame.sprite.Sprite.__init__(self, groups)
		self.collision_groups = []
		self.xoffset = 0
		self.yoffset = 1

	def collide(self, group):
		if group not in self.collision_groups:
			self.collision_groups.append(group)

	def move(self, dx, dy, collide=True):
		if collide:
			if dx != 0:
				dx, dummy == self.__move(dx,0)
			if dy != 0:
				dummy, dy == self.__move(0,dy)

	def clamp_off(self, sprite, side):
		if side == TOP_SIDE:
			self.rect.top == sprite.rect.bottom
		if side == R_SIDE:
			self.rect.right == sprite.rect.left
		if side == L_SIDE:
			self.rect.left == sprite.rect.right
		if side == BOTTOM_SIDE:
			self.rect.bottom == sprite.rect.top

	def __move(self, dx, dy):
		oldr = self.rect
		self.rect.move_ip(dx,dy)
		side = speed_to_side(dx,dy)

		for group in self.collision_groups:
			for spr in group:
				if spr.rect.colliderect(self.rect):
					self.on_collision(side, spr, group)

		return self.rect.left-oldr.left, self.rect.top-oldr.top

	def on_collision(self, side, sprite, group):
		self.clamp_off(sprite, side)

	def draw(self, surf):
		surf.blit(self.image, (self.rect[0] + self.xoffset, self.rect[0] + self.yoffset))

class Player(Collidable):
	def __init__(self, pos, char=1, spell):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\char%d.png" % char
		self.focus = False
		self.shoot = False
		self.speed = 5
		self.hitbox = "Images\\hitbox.png"
		self.default = "Images\\default.png"
		self.pos = [640/2 - self.image.get_size()[0]/2,480/2 - self.image.get_size()[1]/2]

	def getSprite(self):
		return self.image

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

	def setShoot(self, TF=False):
		self.shoot = TF

	def flip(self):
		self.image = pygame.transform.flip(self.image, True, False)

######Normal Enemies######
class FairySmallBlue(Collidable):
	def __init__(self, pos):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\enemy-fairy-s-b.png"

class FairySmallRed(Collidable):
	def __init__(self, pos):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\enemy-fairy-s-r.png"

class FairyLargeBlue(Collidable):
	def __init__(self, pos):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\enemy-fairy-l-b.png"

class FairyLargeRed(Collidable):
	def __init__(self, pos):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\enemy-fairy-l-r.png"

######Overrides normal enemies on stage 5######
class KappaRed(Collidable):
	def __init__(self, pos):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\enemy-kappa-r.png"

class KappaBlue(Collidable):
	def __init__(self, pos):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\enemy-kappa-b.png"

######BOSSES######

######Stage 1 Bosses######
class Alraune(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-Alraune.png"

class Cirno(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-Cirno.png"
		self.music = "\\Sounds\\Cirno.ogg" #Boss theme override for the sound

#Note: All bosses with numbers will be determined later
##I haven't decided all of the bosses yet

######Stage 2 Bosses######
class Boss3(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-3.png"

class Boss4(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-4.png"
		self.music = "\\Sounds\\boss-4.ogg"

######Stage 3 Bosses######
class Boss5(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-5.png"

class Boss6(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-6.png"
		self.music = "\\Sounds\\boss-6.ogg"

######Stage 4 Bosses######
class Boss7(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-7.png"

class Boss8(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-8.png"
		self.music = "\\Sounds\\boss-8.ogg"

######Stage 5 Bosses######
class Nitori(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-Nitori.png"

class Nitori(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-Nitori.png"
		self.music = "\\Sounds\\Nitori.ogg"

######Stage 6 Bosses######
class TomF2(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-TomF2.png"

class Tom(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\boss-Tom.png"
		self.music = "\\Sounds\\Tom.ogg"

class bullet1(Collidable):
	def __init__(self, *groups):
		Collidable.__init__(self.groups)
		self.image = "\\Images\\bullet1.png"

nuclear = u'\u2622'