#Tyler Robbins
#2/16/14
#Menu Test
#Used to make a menu that will be used in the game

import pygame, sys
from pygame.locals import *
import time

WHITE = (255,255,255) #set the color WHITE to a variable
BLACK = (0,0,0) #set the color BLACK to a variable

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
			self.bcolor = WHITE
		else:
			self.bcolor = BLACK

	def Choice(self, pressed):
		if pressed:
			pass
		else:
			pass

	def setName(name):
		self.name = name

	def getName():
		return self.name

	def setLoc(loc):
		self.loc = loc

	def getloc():
		return self.loc

x = 0
y = 0
loc = True
pygame.init()

startb = button()
exitb = button()

buttons = {1:startb, 2:exitb}
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
	startdisp = fontObj.render("Start", True, startb.getSelect())
	exitdisp = fontObj.render("Exit", True, exitb.getSelect())
	display.blit(startdisp, (135, 320))
	display.blit(exitdisp, (235, 250))
	
	while loc:
		print "loop2"
		startdisp = fontObj.render("Start", True, startb.getSelect())
		exitdisp = fontObj.render("Exit", True, exitb.getSelect())
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
				
					if type(buttons[selected]).__name__ == "exitb":
						print "Closing!"
						pygame.quit()
						sys.exit()

					if buttons[selected].Choice(True):
						print "z"
						if str(buttons[selected]) == "exitb":
							print "Closing!"
							pygame.quit()
							sys.exit()

						elif str(buttons[selected]) == "startb":
							print "Starting!"

				elif event.key == K_DOWN: #move down through menu
					if selected == 2:
						selected -= 1
					else:
						selected += 1
				
				elif event.key == K_UP: #move up through menu
					if selected == 1:
						selected += 1
					
					elif selected <= 0:
						selected = 1

					else:
						selected -= 1
				
				else:
					continue

		for item in buttons:
			print "foo" + str(item) + str(buttons[item])
			if item == selected:
				buttons[selected].setSelect(True)
			else:
				buttons[selected].setSelect(False)

		time.sleep(1)
		print "start", startb.getSelect()
		print "exit", exitb.getSelect()

		pygame.display.update()

nuclear = u'\u2622'