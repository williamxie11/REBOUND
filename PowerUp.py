import sys, pygame
from pygame.locals import *

class PowerUp:

    def __init__(self, x, y, dx, dy, radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        
        self.color = (169, 32, 0)
        self.Rect = pygame.Rect(self.x - self.radius, self.y - self.radius, radius*2, radius*2)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius, 0)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy


    # GET & SET #
    # -------------------- #
    def getX(self):
        return self.x

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def getY(self):
        return self.y

    def getdx(self):
        return self.dx

    def setdx(self, newdx):
        self.dx = newdx

    def getdy(self):
        return self.dy

    def setdy(self, newdy):
        self.dy = newdy
