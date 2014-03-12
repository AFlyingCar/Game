Game
====

######Description######
A Touhou fan-game made with Python 2.7 utilizing the Pygame 1.9.1 modules.

######Installation######
- Python 2.7 and Pygame 1.9.1 for Python 2.7 must be installed before this program can be used.

Windows:

-Check Python version:
  - Go to C:\
  - Look for a folder named Python27

-Install Python 2.7.3:
  http://www.python.org/download/releases/2.7/

-Install Pygame 1.9.1:
  http://www.pygame.org/download.shtml

MacOSX:

-Check Python version:
  - $ python --version

  -Output should say "Python 2.7.3"

-Install Python:
  http://www.python.org/download/releases/2.7/

-Install Pygame:
  - $ wget "http://pygame.org/ftp/pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg" && hdiutil attach pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg

Linux:

-Check Python version:
  - $ python --version
  -Output should say "Python 2.7.3"

-Install Python:
  - $ wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
  - $ tar -xzf Python-2.7.6.tgz
  - $ cd Python-2.7.6
  - $ ./configure
  - $ make
  - $ sudo make install

-Install Pygame:
  - $ sudo apt-get install python-pygame


######Git clone######
Download "Game/" by typing:
  -Unix:
    - $ git clone https://github.com/AFlyingCar/Game.git
  -Windows:
    https://github.com/AFlyingCar/Game/
    Click "Download as Zip."
  
  
  
  

Programmers
===========

Note: Please put your name on top of files that you are editing as a comment or say *-[Name].py, and please only edit the files with your name on it. This is to avoid merging issues.

-Sound files belong in:
  Sounds/
  - Must be *.ogg files for the program to read.
  - Sound files must be in the same folder as the program trying to read them.

-Image files belong in:
  Images/
  - Must be *.png files
