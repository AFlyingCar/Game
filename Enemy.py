#Tyler Robbins
#3/27/14
#Enemy
#Defines the behavior of enemies and bosses

import pygame
from pygame.locals import *
import math
import Sprites

TOP_SIDE = 0
BOTTOM_SIDE = 2
R_SIDE = 1
L_SIDE = 3

def speed_to_side(dx,dy):
	if abs(dx) > abs(dy):
		dy = 0
	else:
		dx = 0
	if dy < 0:
		return 0
	elif dx > 0:
		return 1
	elif dx < 0:
		return 3
	elif dy > 0:
		return 2
	else:
		return 0,0

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

class Enemy(Collidable):
	def __init__(self, pos, hp=1):
		Collidable.__init__(self, self.groups)
		self.left_images = []
		for i in self.right_images:
			self.left_images.append(pygame.transform.flip(i, 1, 0))
		self.rect = self.image.get_rect(topleft = pos)
		self.facing = 1
		self.frame = 0
		self.dying = False
		self.shooting = False
		self.hp = hp
		self.hit_timer = 3
		self.hit_sound = load_sound("pichun.ogg")

	def kill(self):
		if self.hp <= 0:
			pygame.sprite.Sprite.kill(self)

	def on_collision(self, side, sprite, group):
		self.clamp_off(sprite, side)
		if get_bullet() == "p":
			self.kill()

	def hit(self):
		if self.hit_timer <= 0:
			self.hit_timer = 20
			self.hp -= 1
			if self.hp <= 0:
				self.kill()

			if (self.hp/self.old_hp)*100 <= 10:
				self.hit_sound.play()

	def stop_attacking(self):
		self.shooting = False

	def update(self):
		self.frame += 1
		self.hit_timer -= 1
		dx = 0

		if self.facing > 0:
			self.image = pygame.transform.flip(self.image, True, False)

class Boss(Enemy):
	def __init__(self, name="Enemy", lev=[1,0]):
		Enemy.__init__(pos=(320, 0), hp=(lev[0]*1000))
		self.read=0
		self.name=name
		self.image = "\\Images\\boss-%d-%d" % lev[0],lev[1]

	def dispHealth(self):
		health = self.fontObj.render(self.name, 1, (30,144,255))
		self.display.blit(health, (0,0))
		pygame.draw.line(display, (30,144,255), health.get_width()+5, (self.hp/self.old_hp)*100)
		self.display.update()

	def getTalk(self, key=False):
		read = open('\\data\\conv-%d-%d-%d' % char,lev[0],lev[1]).split(",")[read]
		self.read += 1
		read = self.fontObj.render(read, 1, (255,255,255))
		self.display.blit(read, (320,(480-read.get_height()-5)))

class Boss_1(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="Alraune", lev=[1,1])
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

	######SpellCards######

class Boss_2(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="Cirno", lev=[1,1])
		self.spellnum = 2

	def getSpellNum(self):
		return self.spellnum

class Boss_3(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

class Boss_4(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="")
		self.spellnum = 4

	def getSpellNum(self):
		return self.spellnum

class Boss_5(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

class Boss_6(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="")
		self.spellnum = 5

	def getSpellNum(self):
		return self.spellnum

class Boss_7(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="")
		self.spellnum = 6

	def getSpellNum(self):
		return self.spellnum

class Boss_8(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

class Boss_9(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="Nitori")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

class Boss_10(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="Nitori")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

class Boss_11(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="TomF2")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

class Boss_12(Boss):
	def __init__(self, *groups):
		Boss.__init__(name="Tom")
		self.spellnum = 1

	def getSpellNum(self):
		return self.spellnum

nuclear = u'\u2622'