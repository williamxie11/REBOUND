#####   ---   #####
REBOUND v1.0.0
William Xie
http://xiewilliam.com
#####   ---   #####
---------------------------------------------------------------------------------

** DESCRIPTION --

Short Gameplay:
http://www.youtube.com/watch?v=3QREB9IyM2w

A small game created for CS 125's honors add-on, CS 196.
You control two paddles on the left and right sides.
Balls of differing sizes and powerup balls will spawn based on your score.
The objective of the game is to survive as long as possible rebounding balls.
If a ball gets past your paddle, your paddle shortens.
You lose when your paddle shortens to nothing!

---------------------------------------------------------------------------------

** INSTALLATION --

1) Download all files into a directory

2) Download and install Python 2.7.3 (2.7.X works, but 3.0+ does not)
LINK: http://www.python.org/getit/

3) Download and install Pygame 1.9.X 
LINK: http://www.pygame.org/download.shtml

4) Run Main.py to start playing!

---------------------------------------------------------------------------------


** INSTRUCTIONS --

Control the left and right paddles with your mouse!

Balls of different sizes will spawn at an increasing rate!

Rebound a ball to break it into two balls of smaller size!

Rebound the smallest size ball to destroy it!

Rebound red balls to increase your paddle length!

Score will increase based on the size of the rebounded ball!

Your paddle shortens when balls are let through the edge!

You LOSE when your paddle shortens to nothing!

---------------------------------------------------------------------------------

** CREDITS --

Created and Programmed by: 
  William Xie

Programmed with:
  Python 2.7.3 
  Pygame 1.9.1

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
  
  - powerup ball can spawn right under a normal ball making it hard to see and vice versa
  
  - sound and music do not play and instead a "clicking" sound is played
      ***SOLUTION: this is a known issue with sound modules in Pygame. Can be fixed by a few restarts and luck.
      
  - rebound sounds are delayed
      ***SOLUTION: this is caused by delays in the sound modules in Pygame
      
---------------------------------------------------------------------------------

## ** TROUBLESHOOTING/FAQ --

Q: REBOUND! closes immediately after starting it up.
  A: Reinstall Pygame and check to see if there are any conflicts in the Python folder. Installing Py2Exe after Pygame
     can cause this issue. If nothing works, a clean installation of Python and Pygame immediately after should work.
    
Q: Collision is a little wonky.
  A: This is due to how collision detection is implemented using Pygame for the paddles. See known bugs for issues.
  
Q: Who's the guy on the bottom right in the instructions?
  A: Lawrence Angrave, an awesome Computer Science professor at UIUC. Press 'A' in the instructions screen to hear him!





