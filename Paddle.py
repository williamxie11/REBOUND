import sys, pygame
from pygame.locals import *

class Paddle:

    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        
        self.Rect = pygame.Rect(self.x, self.y, 10, self.length)

    def draw(self, surface, baseColor, glowColor):
        pygame.draw.rect(surface, baseColor, self.Rect,0)
        pygame.draw.rect(surface, glowColor, self.Rect,2)


    # GET & SET #
    # --------------------#
    def getX(self):
        return self.x

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def getY(self):
        return self.y

    def getLength(self):
        return self.length
    
    def decrease(self, amount):
        self.length -= amount

    def increase(self, amount):
        self.length += amount


    
        
