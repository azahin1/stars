'''
title: Star sprite
'''
from sprites import Sprite
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d
from random import randint
from loader import *

class Star(Sprite): # inherits from Sprite class
    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimentions(2, 2)
        self.setPOS(randint(0, self.window.getWidth() - self.getWidth()), randint(0, self.window.getHeight() - self.getHeight()))
        self.setColour(STAR_COLOUR)
        self.destroyed = False
        self.accValue = 0.5
        self.friction = -0.1
        self.velocity = [0, 0]
        self.accelaration = [0, 0]
        
    def move(self, keys): # moving the paddle with key presses
        self.accelaration = [0, 0]
        if keys[K_LEFT] or keys[K_a]:
            self.accelaration[0] = self.accValue
        if keys[K_RIGHT] or keys[K_d]:
            self.accelaration[0] = -self.accValue
        if keys[K_UP] or keys[K_w]:
            self.accelaration[1] = self.accValue
        if keys[K_DOWN] or keys[K_s]:
            self.accelaration[1] = -self.accValue

        self.accelaration[0] += self.velocity[0] * self.friction
        self.accelaration[1] += self.velocity[1] * self.friction
        self.velocity[0] += self.accelaration[0]
        self.velocity[1] += self.accelaration[1]
        self.x += self.velocity[0] + self.accelaration[0]/2
        self.y += self.velocity[1] + self.accelaration[1]/2

        #-- bounderies
        if self.x > self.window.getWidth() - self.getWidth(): # right wall
            self.x = 0
            self.y = randint(0, self.window.getHeight() - self.getHeight())
        if self.x < 0: # left wall
            self.x = self.window.getWidth() - self.getWidth()
            self.y = randint(0, self.window.getHeight() - self.getHeight())
        if self.y > self.window.getHeight() - self.getHeight(): # bottom wall
            self.y = 0
            self.x = randint(0, self.window.getWidth() - self.getWidth())
        if self.y < 0: # top wall
            self.y = self.window.getHeight() - self.getHeight()
            self.x = randint(0, self.window.getWidth() - self.getWidth())

        self.pos = (self.x, self.y) # moving it based on new values

if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    stars = [Star(window) for _ in range(300)]
    while True:
        window.getEvents()
        window.clearScreen()
        for ball in stars:
            window.blitSprite(ball)
            ball.move(window.getKeysPressed())
        window.updateScreen()