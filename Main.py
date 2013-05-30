import sys, pygame, math, random, Menu, Paddle, Ball, PowerUp
from pygame.locals import *

# Bounce bounce!

# ----- ----- ----- ----- -----#


########  ########  ########    ########    #      #    #       #    # #        #
#      #  #         #      #    #      #    #      #    ##      #    #   #      #
#      #  #         #      #    #      #    #      #    # #     #    #    #     #
#      #  #         #     ##    #      #    #      #    #  #    #    #     #    #
########  ####      ######      #      #    #      #    #   #   #    #     #    #
##        #         #     ##    #      #    #      #    #    #  #    #     #    #
#  #      #         #      #    #      #    #      #    #     # #    #    #     
#    #    #         #      #    #      #    #      #    #      ##    #   #      
#      #  ########  ########    ########    ########    #       #    # #        #

""" By William Xie """
""" for CS 125 Honors """


# ----- ----- ----- ----- ----- #
# Methods #

"""
# Moves all the balls in the ball list by their corresponding dx, dy
#   - collision detection with walls and paddle; calls split method if collision occurs
#   - checks if ball is off the playing field 
"""

def move():
    global balls, maxBalls, length, pows
    
    # Paddles!
    leftPaddle = Paddle.Paddle(10, lmouseY, length)
    leftRect = pygame.Rect(leftPaddle.x, leftPaddle.y, 10, leftPaddle.length)
    leftPaddle.draw(background, (255, 255, 255), (0, 0, 0))
    
    rightPaddle = Paddle.Paddle(width-20, rmouseY, length)
    rightRect = pygame.Rect(rightPaddle.x, rightPaddle.y, 10, rightPaddle.length)
    rightPaddle.draw(background, (255, 255, 255), (0, 0, 0))
    
    # Add Ball!
    if (len(balls) < maxBalls):
        addBall(balls)

    for b in balls:
        b.move()
        
        # Ball!
        b.draw(background)
        
        # Collisions !
        if (b.y <= 60):
            b.setdy(-b.dy)
            if (b.dx < 0):
                b.setdx(b.dx-1)
            else:
                b.setdx(b.dx+1)
        elif (b.y >= height - 60):
            b.setdy(-b.dy)

        bRect = pygame.Rect(b.x - b.radius, b.y - b.radius, b.radius*2, b.radius*2)
                
        if (bRect.colliderect(leftRect)):
            if (b.color == (169, 32, 0)):
                if (b.radius == 5):
                    length += 20
                elif (b.radius == 10):
                    length += 15
                elif (b.radius == 15):
                    length += 10
                balls.remove(b)
                hpSound.play()
            else:
                hitPaddleSound.play()
                split(b, "right")
                
        if (bRect.colliderect(rightRect)):
            if (b.color == (169, 32, 0)):
                if (b.radius == 5):
                    length += 50
                elif (b.radius == 10):
                    length += 25
                elif (b.radius == 15):
                    length += 10
                balls.remove(b)
                hpSound.play()
            else:
                hitPaddleSound.play()
                split(b, "left")

        # Out of Bounds !
        if (b.x < -15 or b.x > width+15):
            shortSound.play()
            length -= b.radius
            balls.remove(b)

"""
# Takes in current maxBalls and current score
# Calculates if can increase max and returns max amount
"""
def canAddMax(maxBalls, score):
    global pows
    newMaxBalls = score/500 + 2
    if (newMaxBalls > maxBalls):
        addPowerUp(balls, maxBalls)
        pows += 1
    return newMaxBalls

"""
# Takes in list of balls
# Appends a ball with random coordinates and dx,dy to the balls list
"""
def addBall(ballsList):
    size = getRandomSize()
    x = width/2
    y = height/2
    if (random.randint(0, 101) <= 50):
        dx = 1
    else:
        dx = -1
    if (random.randint(0, 101) <= 50):
        dy = 1
    else:
        dy = -1
    ball = Ball.Ball(x, y, dx, dy, size)
    ballsList.append(ball)

"""
# Takes in balls list and current level
# Appends a powerUp ball with random coordinates and dx,dy to balls list
"""
def addPowerUp(ballsList, level):
    if (level%5 == 0):
        size = 15
    elif (level%3 == 0):
        size = 10
    else:
        size = 5
    x = width/2
    y = height/2
    if (random.randint(0, 101) <= 50):
        dx = 1
    else:
        dx = -1
    if (random.randint(0, 101) <= 50):
        dy = 1
    else:
        dy = -1
    ball = PowerUp.PowerUp(x, y, dx, dy, size)
    ballsList.append(ball)
    
"""
# Calculates using random a size of ball and returns size
"""
def getRandomSize():
    randInt = random.randint(0, 100)
    if (randInt >= 90):
        size = 25
    elif (randInt >= 75):
        size = 20
    elif (randInt >= 40):
        size = 15
    elif (randInt >= 10):
        size = 10
    else:
        size = 5
    return size

"""
# Takes in a ball and the new direction
# Increases score and creates split effect
# Removes ball if ball size = 5
"""
def split(ball, newDirection):
    global balls, b5, b10, b15, b20, b25, score, pows
    # Score and Counters
    if (ball.radius == 25):
        score += 10
        b25 += 1
    elif (ball.radius == 20):
        score += 15
        b20 += 1
    elif (ball.radius == 15):
        score += 20
        b15 += 1
    elif (ball.radius == 10):
        score += 25
        b10 += 1
    else:
        score += 50
        b5 += 1

    # New Balls
    if (ball.radius - 5 == 0):
        balls.remove(ball)
    else:
        if (newDirection == "right"):
            balls.remove(ball)
            newBall1 = Ball.Ball(ball.x, ball.y, 1, 1, ball.radius - 5)
            newBall2 = Ball.Ball(ball.x, ball.y, 1, -1, ball.radius - 5)
            balls.append(newBall1)
            balls.append(newBall2)
        elif (newDirection == "left"):
            balls.remove(ball)
            newBall1 = Ball.Ball(ball.x, ball.y, -1, 1, ball.radius - 5)
            newBall2 = Ball.Ball(ball.x, ball.y, -2, -1, ball.radius - 5)
            balls.append(newBall1)
            balls.append(newBall2)


# ----- ----- ----- ----- ----- #

" # Initializations # "

pygame.init()
frames = pygame.time.Clock()

width = 1024
height = 500

background = pygame.display.set_mode((width, height))
pygame.display.set_caption("R E B O U N D !  -  v.1.0.0  -  WILLIAM XIE")

# Stats !
pows = 0
b5 = 0
b10 = 0
b15 = 0
b20 = 0
b25 = 0
score = 0
highBalls = 0

# Variables !
mouseX = 0
mouseY = 0

lmouseY = 0
rmouseY = 0
left = True

length = 100

pause = True
instructions = False
creds = False

maxBalls = 2

ball1 = Ball.Ball(600, 400, 1, 1, 15)
ball2 = Ball.Ball(400, 400, 1, 1, 10)
balls = []
balls.append(ball1)
balls.append(ball2)


# Sound Initialization !
pygame.mixer.init(0)
clickSound = pygame.mixer.Sound("sfx\click.wav")
clickBackSound = pygame.mixer.Sound("sfx\clickback.wav")
hitWallSound = pygame.mixer.Sound("sfx\hitWall.wav")
hitPaddleSound = pygame.mixer.Sound("sfx\hitPaddle.wav")
shortSound = pygame.mixer.Sound("sfx\short.wav")
hpSound = pygame.mixer.Sound("sfx\easteregg.wav")
dangerSound = pygame.mixer.Sound("sfx\danger.wav")
angraveSound = pygame.mixer.Sound("angrave.ogg")

# Font Initialization !
titleFont = pygame.font.Font("fonts\ArcadeClassic.ttf", 180)
subtitleFont = pygame.font.Font("fonts\zig.ttf", 32)
textFont = pygame.font.Font("fonts\DisposableDroid.ttf", 24)

# Picture Initialization !
angrave = pygame.image.load("angrave.png")


# Music Initialization !
pygame.mixer.init(22050, -16, 1, 0)
if (pause):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("fillerlove.ogg")
    pygame.mixer.music.play(-1)


pygame.key.set_repeat(100, 5)


    
# ----- ----- ----- ----- ----- #


"# Game Loop #"
while True:
    
    # Menu/Pause #
    if (pause):
        background.fill((25, 25, 25))
        menu = Menu.Menu(width, height, titleFont, subtitleFont, textFont, angrave)
        if (instructions):
            menu.showInstructions(background)
        elif (creds):
            menu.showCredits(background)
        else:
            menu.showMenu(background)
        

    # Game #
    else:
        
        # Background!
        background.fill((30, 30, 30))

        # Top/Bottom Walls!
        pygame.draw.rect(background, (25, 25, 25), (0, 0, width, 40), 0)
        pygame.draw.rect(background, (240, 240, 240), (0, 0, width, 40), 2)
        pygame.draw.rect(background, (25, 25, 25), (0, height - 40, width, 40), 0)
        pygame.draw.rect(background, (240, 240, 240), (0, height - 40, width, 40), 2)
        
        # Ball!
        maxBalls = canAddMax(maxBalls, score)
        if (highBalls < len(balls)):
            highBalls = len(balls)
            
        move()
            
        # Scoreboard
        scoreboard = textFont.render("SCORE: "+str(score), False, (255, 255, 255))
        background.blit(scoreboard, (150, 10))
        levelNotif = textFont.render("LEVEL: "+str(maxBalls - 1), False, (255, 255, 255))
        background.blit(levelNotif, (350, 10))
        spawnNotif = textFont.render("BALLS: "+str(len(balls)), False, (255, 255, 255))
        background.blit(spawnNotif, (550, 10))
        spawnNotif = textFont.render("LENGTH: "+str(length), False, (255, 255, 255))
        background.blit(spawnNotif, (740, 10))
        pauseNotif = textFont.render("'P' to Pause!", False, (255, 255, 255))
        background.blit(pauseNotif, (415, height-35))
    
    # Event Handler #
    for event in pygame.event.get():
        # Quit! 
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()
        # Pause!
        elif (event.type == KEYDOWN):
            # Quit Key!
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # Pause Key!
            if (event.key == K_p):
                if (instructions == False and creds == False):
                    pause = not pause
                if (pause):
                    print "Pause!"
                    clickBackSound.play()
                else:
                    print "Resume!"
                    clickSound.play()
            # Instructions
            if (event.key == K_i and creds == False):
                if (pause == True):
                    instructions = not instructions
                if (instructions == False):
                    clickBackSound.play()
                else:
                    clickSound.play()
                print "Instructions!"
            # Angrave
            if (event.key == K_a and instructions):
                angraveSound.play()
                print "Angrave Activated!"
            # Credits
            if (event.key == K_c and instructions == False):
                if (pause == True):
                    creds = not creds
                if (creds == False):
                    clickBackSound.play()
                else:
                    clickSound.play()
                print "Credits!"
            """
            # Keyboard Controls
            if (event.key == K_w):
                lmouseY -= 5
            if (event.key == K_s):
                lmouseY += 5
            if (event.key == K_t):
                rmouseY -= 5
            if (event.key == K_g):
                rmouseY += 5
            """

            
        # Mouse Position!
        mouseX, mouseY = pygame.mouse.get_pos()
        if (left):
            lmouseY = mouseY
        else:
            rmouseY = mouseY
        
        if (mouseX <= width/2):
            left = True
        else:
            left = False
    
        # Top Boundary!
        if (lmouseY < 50):
            lmouseY = 50
        if(rmouseY < 50):
            rmouseY = 50
            
        # Bottom Boundary!
        if (lmouseY > height - length - 50):
            lmouseY = height - length - 50
            
        if (rmouseY > height - length - 50):
            rmouseY = height - length - 50
        
    # Length Paddle Boundary!
    if (length >= 200):
        length = 200
    if (length > 0 and length <= 25):
        dangerSound.play()
    if (length <= 0):
        menu = Menu.Menu(width, height, titleFont, subtitleFont, textFont, angrave)
        # Show stat window / losing screen
        pause = True
        menu.showStats(background, score, highBalls, maxBalls, b5, b10, b15, b20, b25, pows)
    
            
    pygame.display.update()
    frames.tick(100)


# ----- ----- ----- ----- ----- #
