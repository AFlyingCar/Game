#Tyler Robbins
#2/16/14
#Menu Test
#Used to make a menu that will be used in the game

import pygame, sys
from pygame.locals import *

WHITE = (255,255,255) #set the color WHITE to a variable
BLACK = (0,0,0) #set the color BLACK to a variable

class button():
	def __init__(self, loc, select, name): #all buttons start not selected
		self.bcolor = WHITE
		self.select = select
		self.name = name
		self.loc = loc

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

x = 0
y = 0
loc = True
pygame.init()

startb = button((500, 125), True, "startb")
optionb = button((500, 250), False, "optionb")
exitb = button((500, 320), False, "exitb")

buttons = {1:startb, 2:exitb, 3:optionb}
selected = 1

display = pygame.display.set_mode((640, 480)) #set size of window
display.fill((WHITE))
pygame.display.set_caption("Game Menu")
fontObj = pygame.font.Font('freesansbold.ttf', 29)

print str(buttons)
while True:
	print "loop1"
	buttons[selected].setSelect(True)
	print "start", startb.getSelect()
	print "exit", exitb.getSelect()

	while loc:
		print "loop2"
		startdisp = fontObj.render("Start", True, startb.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
		optiondisp = fontObj.render("Options", True, optionb.getSelect())
		display.blit(startdisp, startb.getLoc())
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())

		for event in pygame.event.get():
			if event.type == QUIT:
				print "closing"
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				print "keydown"
				print selected

				if event.key == K_z: #enter option
					print "z"
					for item in buttons:
						if buttons[item].getChoice():
							print buttons[item].getName() + " has been selected."
							if buttons[item].getName() == "exit":
								print "closing"
								pygame.quit()
								sys.exit()

				elif event.key == K_DOWN: #move down through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 2
					elif selected == 2:
						selected -= 1
					else:
						selected -= 1
					buttons[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons[selected].setChoice(False)
					if selected == 1:
						selected += 1
					elif selected == 2:
						selected += 1
					else:
						selected -= 2
					buttons[selected].setChoice(True)
		
		for item in buttons:
			print buttons[item].getName(), buttons[item].getChoice()
			buttons[item].setSelect(buttons[item].getChoice())

		print ">start", startb.getChoice()
		print ">exit", startb.getChoice()

		pygame.display.update()

nuclear = u'\u2622'