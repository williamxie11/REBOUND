import sys, pygame
from pygame.locals import *


class Menu:

    def __init__(self, width, height, titleFont, subtitleFont, textFont, picture):
        self.id = 0
        self.width = width
        self.height = height
        self.titleFont = titleFont
        self.subtitleFont = subtitleFont
        self.textFont = textFont
        self.picture = picture
    
    def showMenu(self, background):
        # Title and Prompts!
        title = self.titleFont.render("REBOUND!", True, (255, 255, 255))
        showMeInstr = self.textFont.render("Press 'I' for Instructions!", True, (255, 255, 255))
        showMeCreds = self.textFont.render("Press 'C' for Credits!", True, (255, 255, 255))
        play = self.subtitleFont.render("Press 'P' to Play!", True, (255, 255, 255))
        background.blit(title, (60, 55))
        background.blit(showMeInstr, (self.width/4+110, 7*self.height/8 - 150))
        background.blit(showMeCreds, (self.width/4+130, 7*self.height/8 - 100))
        background.blit(play, (self.width/4+20, 7*self.height/8))

        # Quit Statement
        ret1 = self.textFont.render("QUIT GAME",
                                    False, (255, 255, 255))
        background.blit(ret1, (self.width - 120, 33))
        
        ret2 = self.textFont.render("Press 'ESC'",
                                    False, (255, 255, 255))
        background.blit(ret2, (self.width - 125, 63))

        ret3 = self.textFont.render("<---",
                                        False, (255, 255, 255))
        background.blit(ret3, (self.width - 95, 7))
        
    def showInstructions(self, background):
        # Instructions!
        instrTitle = self.subtitleFont.render("INSTRUCTIONS!", True, (255, 255, 255))
        background.blit(instrTitle, (50, 30))
        
        line1 = self.textFont.render("Control the left and right paddles with your mouse!",
                                     False, (255, 255, 255))
        background.blit(line1, (100, 100))
        
        line2 = self.textFont.render("Balls of different sizes will spawn at an increasing rate!",
                                     False, (255, 255, 255))
        background.blit(line2, (100, 130))

        #
        
        line3 = self.textFont.render("Rebound a ball to break it into two balls of smaller size!",
                                     False, (255, 255, 255))
        background.blit(line3, (100, 260))

        line4 = self.textFont.render("Rebound the smallest size ball to destroy it!",
                                     False, (255, 255, 255))
        background.blit(line4, (100, 290))

        line5 = self.textFont.render("Score will increase based on the size of the rebounded ball!",
                                     False, (255, 255, 255))
        background.blit(line5, (100, 320))

        #

        line6 = self.textFont.render("Your paddle shortens when balls are let through the edge!",
                                     False, (255, 255, 255))
        background.blit(line6, (100, 435))

        line7 = self.textFont.render("You LOSE when your paddle shortens to nothing!",
                                     False, (255, 255, 255))
        background.blit(line7, (100, 465))

        # Return Statement
        ret1 = self.textFont.render("BACK TO MENU",
                                    False, (255, 255, 255))
        background.blit(ret1, (self.width - 150, 33))
        
        ret2 = self.textFont.render("Press 'I'",
                                    False, (255, 255, 255))
        background.blit(ret2, (self.width - 125, 63))

        ret3 = self.textFont.render("<---",
                                        False, (255, 255, 255))
        background.blit(ret3, (self.width - 115, 7))

        # Angrave !
        background.blit(self.picture, (self.width-140, self.height-140))

        # Ball Size Display!
        ballTitle = self.textFont.render("ball",
                                         True, (255, 255, 255))
        background.blit(ballTitle, (115, 180))
        
        sizeTitle = self.textFont.render("size",
                                     True, (255, 255, 255))
        background.blit(sizeTitle, (115, 220))
        
        pygame.draw.circle(background, (240, 240, 240), (215, 190), 5, 0)
        size5  = self.textFont.render("5",
                                      True, (255, 255, 255))
        background.blit(size5, (210, 220))
        
        pygame.draw.circle(background, (240, 240, 240), (285, 190), 10, 0)
        size10 = self.textFont.render("10",
                                      True, (255, 255, 255))
        background.blit(size10, (277, 220))
        
        pygame.draw.circle(background, (240, 240, 240), (368, 190), 15, 0)
        size15 = self.textFont.render("15",
                                      True, (255, 255, 255))
        background.blit(size15, (360, 220))
        
        pygame.draw.circle(background, (240, 240, 240), (459, 190), 20, 0)
        size20 = self.textFont.render("20",
                                      True, (255, 255, 255))
        background.blit(size20, (449, 220))
        
        pygame.draw.circle(background, (240, 240, 240), (555, 190), 25, 0)
        size25 = self.textFont.render("25",
                                      True, (255, 255, 255))
        background.blit(size25, (545, 220))

        # Powerup Display

        powerUpLine = self.textFont.render("Rebound red balls to increase your paddle length!",
                                        False, (255, 255, 255))
        background.blit(powerUpLine, (100, 348))

            # Graphical Powerup Display
        
        hp = self.textFont.render("HP",
                                  True, (255, 255, 255))
        background.blit(hp, (195, 386))

        pygame.draw.circle(background, (169, 32, 0), (300, 390), 5, 0)
        plus5 = self.textFont.render("+20",
                                    True, (255, 255, 255))
        background.blit(plus5,(280, 410))

        pygame.draw.circle(background, (169, 32, 0), (400, 390), 10, 0) 
        plus10 = self.textFont.render("+15",
                                      True, (255, 255, 255))
        background.blit(plus10,(380, 410))
        
        pygame.draw.circle(background, (169, 32, 0), (500, 390), 15, 0) 
        plus15 = self.textFont.render("+10",
                                      True, (255, 255, 255))
        background.blit(plus15,(480, 410))
        

    def showCredits(self, background):
        # Title
        credTitle = self.subtitleFont.render("CREDITS!",
                                             True, (255, 255, 255))
        background.blit(credTitle, (50, 30))

        # Created and Programmed by: William Xie
        category1 = self.textFont.render("Created and Programmed by:",
                                         True, (255, 255, 255))
        background.blit(category1, (100, 100))

        myName = self.textFont.render("William Xie",
                                      False, (255, 255, 255))
        background.blit(myName, (145, 125))

        # Programmed with: Python 2.7.3 // Pygame (www.pygame.org)
        category2 = self.textFont.render("Programmed with:",
                                         True, (255, 255, 255))
        background.blit(category2, (105, 190))

        py1 = self.textFont.render("Python 2.7.3",
                                   False, (255, 255, 255))
        background.blit(py1, (145, 215))

        py2 = self.textFont.render("Pygame (www.pygame.org)",
                                   False, (255, 255, 255))
        background.blit(py2, (145, 240))

        # Game SFX: www.superflashbros.net/as3sfxr/ // 
        category3 = self.textFont.render("Game SFX:",
                                         True, (255, 255, 255))
        background.blit(category3, (110, 300))

        supf = self.textFont.render("www.superflashbros.net/as3sfxr/",
                                    False, (255, 255, 255))
        background.blit(supf, (145, 325))

        # Fonts: www.1001freefonts.com
        category4 = self.textFont.render("Fonts:",
                                         True, (255, 255, 255))
        background.blit(category4, (115, 375))

        freef = self.textFont.render("www.1001freefonts.com",
                                     False, (255, 255, 255))
        background.blit(freef, (145, 400))

        # What Is Love 8-bit: http://www.youtube.com/watch?v=CT8t_1JXWn8
        category5 = self.textFont.render("What Is Love 8-bit:",
                                         True, (255, 255, 255))
        background.blit(category5, (self.width/2-5, 100))

        compSong = self.textFont.render("http://www.youtube.com/watch?v=CT8t_1JXWn8",
                                        False, (255, 255, 255))
        background.blit(compSong, (self.width/2+20, 125))

        # Special Thanks:
        category6 = self.textFont.render("Special Thanks:",
                                         True, (255, 255, 255))
        background.blit(category6, (self.width/2+10, 200))

        name1 = self.textFont.render("The Xie Family",
                                     False, (255, 255, 255))
        background.blit(name1, (self.width/2+30, 225))

        name2 = self.textFont.render("Lawrence Angrave",
                                     False, (255, 255, 255))
        background.blit(name2, (self.width/2+30, 250))

        name3 = self.textFont.render("and the UIUC Computer Science Department",
                                     False, (255, 255, 255))
        background.blit(name3, (self.width/2+30, 275))
        

        # Thanks!
        thanks = self.textFont.render("Thanks for playing! Press 'A' in the Instructions screen for a surprise ...",
                                      True, (242, 192, 232))
        background.blit(thanks, (self.width/6-20, self.height - 35))
        
    
        # Return Statement
        ret1 = self.textFont.render("BACK TO MENU",
                                    False, (255, 255, 255))
        background.blit(ret1, (self.width - 150, 33))
        
        ret2 = self.textFont.render("Press 'C'",
                                    False, (255, 255, 255))
        background.blit(ret2, (self.width - 125, 63))

        ret3 = self.textFont.render("<---",
                                        False, (255, 255, 255))
        background.blit(ret3, (self.width - 115, 7))

    def showStats(self, background, score, highBalls, maxBalls, b5, b10, b15, b20, b25, pows):
        loseBackground = pygame.display.set_mode((1024, 500))
        loseBackground.fill((0,0,0))
        background.blit(loseBackground, (0,0))

        loseNotif = self.subtitleFont.render("YOU LOST!", True, (255, 255, 255))
        loseBackground.blit(loseNotif, (380, 40))

        # Stats
        levelStat = self.textFont.render("LEVEL: "+str(maxBalls-1), False, (255, 255, 255))
        loseBackground.blit(levelStat, (220, 125))

        scoreStat = self.textFont.render("SCORE: "+str(score), False, (255, 255, 255))
        loseBackground.blit(scoreStat, (220, 175))

        highestBallsStat = self.textFont.render("HIGHEST NUMBER OF BALLS IN PLAY: "+str(highBalls),
                                                False, (255, 255, 255))
        loseBackground.blit(highestBallsStat, (540, 125))
        
        highestBallsStat = self.textFont.render("POWERUPS COLLECTED: "+str(pows),
                                                False, (255, 255, 255))
        loseBackground.blit(highestBallsStat, (600, 175))

        # Kill Count

        killNotif = self.subtitleFont.render("REBOUNDS", True, (255, 255, 255))
        loseBackground.blit(killNotif, (380, 250))

        pygame.draw.circle(background, (240, 240, 240), (295, 350), 5, 0)
        size5  = self.textFont.render(str(b5),
                                      True, (255, 255, 255))
        background.blit(size5, (285, 400))
        
        pygame.draw.circle(background, (240, 240, 240), (395, 350), 10, 0)
        size10 = self.textFont.render(str(b10),
                                      True, (255, 255, 255))
        background.blit(size10, (385, 400))
        
        pygame.draw.circle(background, (240, 240, 240), (495, 350), 15, 0)
        size15 = self.textFont.render(str(b15),
                                      True, (255, 255, 255))
        background.blit(size15, (485, 400))
        
        pygame.draw.circle(background, (240, 240, 240), (595, 350), 20, 0)
        size20 = self.textFont.render(str(b20),
                                      True, (255, 255, 255))
        background.blit(size20, (585, 400))
        
        pygame.draw.circle(background, (240, 240, 240), (695, 350), 25, 0)
        size25 = self.textFont.render(str(b20),
                                      True, (255, 255, 255))
        background.blit(size25, (685, 400))
        
        # Thank You
        thanks = self.subtitleFont.render("THANKS FOR PLAYING!", True, (255, 255, 255))
        loseBackground.blit(thanks, (260, 450))

