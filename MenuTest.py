#Tyler Robbins
#2/16/14
#Menu Test
#Used to make a menu that will be used in the game

import pygame, sys
from pygame.locals import *
import time

WHITE = (255,255,255) #set the color WHITE to a variable
BLACK = (0,0,0) #set the color BLACK to a variable

#NOTE
#Currently, selected options are white, and deselected options are black


class button():
	def __init__(self): #all buttons start not selected
		self.bcolor = WHITE
		self.select = False
		self.name = ""
		self.loc = (250,250)

#	def __str__(self):
#		for button in self.button:
#			print button
#		return ""

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

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setLoc(self, loc):
		self.loc = loc

	def getLoc(self):
		return self.loc

x = 0
y = 0
loc = True
pygame.init()

startb = button()
exitb = button()
optionb = button()

startb.setName("startb")
exitb.setName("exitb")
optionb.setName("optionb")

buttons = {1:startb, 2:exitb, 3:optionb}
selected = 1


startb.setChoice(True)
exitb.setChoice(False)
optionb.setChoice(False)

startb.setLoc((135, 320))
optionb.setLoc((320, 250))

#buttons[selected].setChoice(True):

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
	startdisp = fontObj.render("Start", True, startb.getSelect())
	exitdisp = fontObj.render("Exit", True, exitb.getSelect())
	optiondisp = fontObj.render("Options", True, optionb.getSelect())
	
	while loc:
		print "loop2"
		display.blit(startdisp, (135, 320))
		display.blit(exitdisp, exitb.getLoc())
		display.blit(optiondisp, optionb.getLoc())
		startdisp = fontObj.render("Start", True, startb.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
		optiondisp = fontObj.render("Options", True, optionb.getSelect())
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
				
#					if buttons[selected] == :
#						print "Closing!"
#						pygame.quit()
#						sys.exit()
#					if buttons[selected].getChoice():
#						print "z"
#						if str(buttons[selected]) == "exitb":
#							print "Closing!"
#							pygame.quit()
#							sys.exit()
#						elif str(buttons[selected]) == "startb":
#							print "Starting!"

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
#					if selected == 1:
#						selected += 1
					
#					elif selected <= 0:
#						selected = 1

#					else:
#						selected -= 1
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
#			print "foo" + str(item) + str(buttons[item])
#			if item == selected:
#			else:
#				buttons[selected].setSelect(False)

#		time.sleep(0.5)

#		print "start", startb.getSelect()
#		print "exit", exitb.getSelect()
		print ">start", startb.getChoice()
		print ">exit", startb.getChoice()

		pygame.display.update()

nuclear = u'\u2622'