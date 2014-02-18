from pygame.locals import *
import pygame, sys
#from MenuTest import *

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

menu2 = True
menu3 = False
menu4 = False
pygame.init()

backb = button((50, 320), False, "backb")
screenb = button((50, 250), True, "screenb")

#Screen Resolution Options
screenSize = button((400, 180), True, "screensb")
backb2 = button((400, 390), False, "backb2")

#Screen Size Options
default = button((500, 250), True, "default")
full = button((500, 320), False, "full")


buttons1 = {1:backb, 2:screenb}
buttons2 = {1:screenSize, 2:backb2}
buttons3 = {1:default, 2:full}
selected = 1

display = pygame.display.set_mode((640, 480)) #set size of window
display.fill((WHITE)) #This color is temporary. It will be replaced with an image later.
pygame.display.set_caption("Game Menu") #set window caption
fontObj = pygame.font.Font('freesansbold.ttf', 29) #make font object

#Menu Buttons
backdisp = fontObj.render("Back", True, backb.getSelect())
screendisp = fontObj.render("Screen Resolution", True, screenb.getSelect())

#Screen Resolution Buttons
screensdisp = fontObj.render("Screen Size", True, screenSize.getSelect())
back2disp = fontObj.render("Back", True, backb2.getSelect())

#Screen Size Buttons
defaultdisp = fontObj.render("Default", True, default.getSelect())
fulldisp = fontObj.render("Full Screen", False, full.getSelect())

while True:
	while menu2:
		print "loop2"
		display.blit(backdisp, backb.getLoc())
		display.blit(screendisp, screenb.getLoc())

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
					for item in buttons1:
						if buttons1[item].getChoice():
							print buttons1[item].getName() + " has been selected."

							if buttons1[item].getName() == "backb":
								print "going back to main menu"
								pygame.quit()
								sys.exit()

							elif buttons1[item].getName() == "screenb":
								print "screen resolution"
								display.blit(screensdisp, screenSize.getLoc())
								display.blit(back2disp, backb2.getLoc())
								menu2 = False
								menu3 = True

				elif event.key == K_DOWN: #move down through menu
					buttons1[selected].setChoice(False)
					if selected == 1:
						selected += 1
					else:
						selected -= 1
					buttons1[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons1[selected].setChoice(False)
					if selected == 1:
						selected += 1
					else:
						selected -= 1
					buttons1[selected].setChoice(True)
		
		for item in buttons1:
			print buttons1[item].getName(), buttons1[item].getChoice()
			buttons1[item].setSelect(buttons1[item].getChoice())

	pygame.display.update()

	while menu3:
		print "loop3"
		
		display.blit(back2disp, backb.getLoc())
		display.blit(screendisp, screenb.getLoc())

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
					for item in buttons2:
						if buttons2[item].getChoice():
							print buttons2[item].getName() + " has been selected."

							if buttons2[item].getName() == "screensb":
								print "scren resolution"

							elif buttons2[item].getName() == "backb2":
								print "options menu"
								display.blit(defaultdisp, default.getLoc())
								display.blit(fulldisp, full.getLoc())
								menu2 = True
								menu3 = False

				elif event.key == K_DOWN: #move down through menu
					buttons2[selected].setChoice(False)
					if selected == 1:
						selected += 1
					else:
						selected -= 1
					buttons2[selected].setChoice(True)
				
				elif event.key == K_UP: #move up through menu
					buttons2[selected].setChoice(False)
					if selected == 1:
						selected += 1
					else:
						selected -= 1
					buttons2[selected].setChoice(True)
		
		for item in buttons2:
			print buttons2[item].getName(), buttons2[item].getChoice()
			buttons2[item].setSelect(buttons2[item].getChoice())

nuclear = u'\u2622'