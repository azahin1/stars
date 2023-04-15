'''
title: Star sprite
'''
from sprites import Sprite
from loader import *

class Star(Sprite): # inherits from Sprite class
    def __init__(self, window, x = 0, y = 0):
        Sprite.__init__(self, window, x, y)
        self.setDimentions(30, 30)
        self.setColour(STAR_COLOUR)
        self.spdX = 5 # horrizontal speed
        self.spdY = 4 # vertical speed
        self.dirX = 1 # starting horizontal direction
        self.dirY = -1 # starting vertical direction
        self.destroyed = False

    def move(self):
        self.x += self.spdX * self.dirX # moves it horizontally
        self.y += self.spdY * self.dirY # moves it vertically

        #-- Bounderies and bouncing
        if self.x < 0: # left wall
            self.x = 0
            self.dirX = 1
        if self.x > self.window.getWidth() - self.getWidth(): # right wall
            self.x = self.window.getWidth() - self.getWidth()
            self.dirX = -1
        if self.y < 0: # top wall
            self.y = 0
            self.dirY = 1
        if self.y > self.window.getHeight() - self.getHeight(): # bottom wall
            self.y = self.window.getHeight() - self.getHeight()
            self.dirY = -1

        self.setPOS(self.x, self.y) # changes the position of the ball
        return self.destroyed

if __name__ == "__main__":
    from pygame import init
    from window import Window
    from random import randint

    init()
    window = Window()
    stars = [Star(window, randint(0, window.getWidth() - 30), randint(0, window.getHeight() - 30)) for _ in range(10)]
    while True:
        window.getEvents()
        window.clearScreen()
        for ball in stars:
            window.blitSprite(ball)
            ball.move()
        window.updateScreen()