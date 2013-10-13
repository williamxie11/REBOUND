REBOUND!
===================

REBOUND v1.0.0
William Xie
http://xiewilliam.com

---------------------------------------------------------------------------------

## ** DESCRIPTION --

Short Gameplay:
http://www.youtube.com/watch?v=3QREB9IyM2w

A small game created for CS 125's honors add-on, CS 196.
You control two paddles on the left and right sides.
Balls of differing sizes and powerup balls will spawn based on your score.
The objective of the game is to survive as long as possible rebounding balls.
If a ball gets past your paddle, your paddle shortens.
You lose when your paddle shortens to nothing!

---------------------------------------------------------------------------------

## ** INSTALLATION --

1) Download all files into a directory

2) Download and install Python 2.7.3 (2.7.X works, but 3.0+ does not)
LINK: http://www.python.org/getit/

3) Download and install Pygame 1.9.X 
LINK: http://www.pygame.org/download.shtml

4) Run Main.py to start playing!

---------------------------------------------------------------------------------


## ** INSTRUCTIONS --

Control the left and right paddles with your mouse!

Balls of different sizes will spawn at an increasing rate!

Rebound a ball to break it into two balls of smaller size!

Rebound the smallest size ball to destroy it!

Rebound red balls to increase your paddle length!

Score will increase based on the size of the rebounded ball!

Your paddle shortens when balls are let through the edge!

You LOSE when your paddle shortens to nothing!

---------------------------------------------------------------------------------

## ** CREDITS --

Created and Programmed by: 
  William Xie

Programmed with:
  Python 2.7.3 
  Pygame 1.9

Game SFX Created From:
  www.superflashbros.net/as3sfxr/
  
Fonts:
  www.1001freefonts.com
  
Music:
  http://www.youtube.com/watch?v=CT8t_1JXWn8
  
Special Thanks:
  The Xie Family
  Lawrence Angrave
  and the UIUC Computer Science Department

---------------------------------------------------------------------------------

## ** KNOWN BUGS --

v1.0.0:
  - hitting ball off top or bottom of paddle may be detected as multiple hits
      ***SOLUTION: implementation issue of collision detection between balls and paddles. To be fixed.
  
  - powerup ball can spawn right under a normal ball making it hard to see and vice versa
      ***SOLUTION: spawn function missing a conditional statement to detect for this. To be fixed.
  
  - when switching paddles by moving the mouse, the previous paddle tends to move as well
      ***SOLUTION: this is due to mouse movement from one paddle to another. In a future version a dead zone will
                   can be implemented to resolve this.
  
  - sound and music do not play and instead a "clicking" sound is played
      ***SOLUTION: this is a known issue with sound modules in Pygame. Can be fixed by a few restarts and luck.
      
  - rebound sounds are delayed
      ***SOLUTION: this is caused by delays in the default sound modules in Pygame. Looking into this, but delays 
                   will still occur when playing.
      
---------------------------------------------------------------------------------

## ** TROUBLESHOOTING/FAQ --

Q: REBOUND! closes immediately after starting it up.
  A: Reinstall Pygame and check to see if there are any conflicts in the Python folder. Installing Py2Exe after Pygame
     can cause this issue. If nothing works, a clean installation of Python and Pygame immediately after should work.
     
Q: I can't install Python/Pygame to play REBOUND!
  A: Make sure you have administrator privileges to install Python and Pygame.
     If you are on a 64-bit OS, try installing the 32-bit Python and Pygame.
     Perhaps try the PyDev plugin for Eclipse (http://pydev.org/download.html).
     An executable (.exe) will come in the near future.
     If you still have issues feel free to contact me (contact info at end of README.txt)

Q: Where can I go to learn more about Pygame?
   A: Pygame modules are great for making small 2D games.
      Visit http://www.pygame.org/ for documentation, downloads, and community submitted games to learn off of!
      This Pygame Cheat Sheet is also quite helpful in understanding the flow of Pygame: 
      http://inventwithpython.com/blog/2011/10/07/pygame-cheat-sheet/
  
Q: Who's the guy on the bottom right in the instructions?
  A: Lawrence Angrave, an awesome Computer Science professor at UIUC. Press 'A' in the instructions screen!

---------------------------------------------------------------------------------

## ** CONTACT --

Have a bug issue? Want to offer some suggestions to improve REBOUND? Feel like getting something off your chest?

Let me know at http://xiewilliam.com/contact
I'll be glad to hear from you!

Thanks for playing!
