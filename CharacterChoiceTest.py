#Tyler Robbins
#2/19/14
#Character Selection Test
#Testing a character choice menu

import pygame, sys, os
from pygame.locals import *
import platform as plat

if str(plat.system()) == "Windows":
	slash = "\\"
else:
	slash = "//"

WHITE = (255,255,255) #set the color WHITE to a variable
BLACK = (0,0,0) #set the color BLACK to a variable

class button():
	def __init__(self, loc, select, name, image): #all buttons start not selected
		self.bcolor = WHITE
		self.select = select
		self.name = name
		self.loc = loc
		self.image = slash + "Images" + slash + self.name + ".png"

	def getSelect(self):
		return self.bcolor
		
	def setSelect(self, select):
		if select:
			self.bcolor = BLACK
		else:
			self.bcolor = WHITE

	def setChoice(self, pressed):
			self.select = pressed

	def getChoice(self):
		return self.select

	def getName(self):
		return self.name

	def getLoc(self):
		return self.loc

class character():
	def __init__(self, speed, name, power, img):
		self.speed = speed
		self.name = name
		self.power = power
		self.loc = [250, 50]
		self.hitbox = slash + "Images" + slash + "hitbox.png"
		self.img = "Images" + slash + img

	def getSpeed(self):
		return self.speed

	def getName(self):
		return self.name

	def getPower(self):
		return self.power

	def getHb(self):
		pygame.image.load(self.hitbox).convert_alpha()

	def setImg(self, img):
		self.img = img

	def getImg(self):
		pygame.image.load(self.img).convert_alpha()

menu1 = True
pygame.init()

char1b = button((500, 180), True, "char1b", "char1b")
char2b = button((500, 250), False, "char2b", "char2b")
exitb = button((500, 320), False, "exitb", "") #Every button must have a picture attached to it.

char1 = character(5, "char1", 20, "char1.png")
char2 = character(7, "char2", 15, "char2.png")

buttons = {1:char1b, 3:exitb, 2:char2b}
chars = {1:char1, 2:char2}
selectedb = 1
selectedc = 1

display = pygame.display.set_mode((640, 480)) #set size of window
display.fill((WHITE)) #This color is temporary. It will be replaced with an image later.
pygame.display.set_caption("Game Menu") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #make font object

while True:
	buttons[selectedb].setSelect(True)

	while menu1:
		print "loop2"
		char1disp = fontObj.render("Char 1", True, char1b.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
		char2disp = fontObj.render("Char 2", True, char2b.getSelect())

		display.blit(char1disp, char1b.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(char2disp, char2b.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				print "closing"
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				print "keydown"
				print selectedb

				if event.key == K_z: #enter option
					print "z"
					for item in buttons:
						if buttons[item].getChoice():
							print buttons[item].getName() + " has been selected."
							if buttons[item].getName() == "exitb":
								print "closing"
								pygame.quit()
								sys.exit()

							elif buttons[item].getName() == "char1b":
								print "character 1"
								print char2.getImg()
								display.blit(char1.getImg(), (250,250))

							elif buttons[item].getName() == "char2b":
								print "character 2"
								print char2.getImg()
								display.blit(char2.getImg(), (0,0))

				elif event.key == K_UP: #move down through menu
					buttons[selectedb].setChoice(False)
					if selectedb == 1:
						selectedb += 2
					elif selectedb == 2:
						selectedb -= 1
					else:
						selectedb -= 1
					buttons[selectedb].setChoice(True)
				
				elif event.key == K_DOWN: #move up through menu
					buttons[selectedb].setChoice(False)
					if selectedb == 1:
						selectedb += 1
					elif selectedb == 2:
						selectedb += 1
					else:
						selectedb -= 2
					buttons[selectedb].setChoice(True)
		
		for item in buttons:
			print buttons[item].getName(), buttons[item].getChoice()
			buttons[item].setSelect(buttons[item].getChoice())

		pygame.display.update()

nuclear = u'\u2622'