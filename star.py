'''
title: Star sprite
'''
from sprites import Sprite
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d
from random import randint
from loader import *

class Star(Sprite): # inherits from Sprite class
    def __init__(self, window, x = 0, y = 0):
        Sprite.__init__(self, window, x, y)
        self.setDimentions(5, 5)
        self.setColour(STAR_COLOUR)
        self.destroyed = False
        self.spd = 5
        
    def move(self, keys): # moving the paddle with key presses
        if keys[K_LEFT] or keys[K_a]: # a key moves it left
            self.x += self.spd
        if keys[K_RIGHT] or keys[K_d]: # d key moves it right
            self.x -= self.spd
        if keys[K_UP] or keys[K_w]: # w key moves it up
            self.y += self.spd
        if keys[K_DOWN] or keys[K_s]: # s key moves it down
            self.y -= self.spd

        #-- bounderies
        if self.x > self.window.getWidth() - self.getWidth(): # right wall
            self.x = 0
            self.y = randint(0, window.getHeight() - 5)
        if self.x < 0: # left wall
            self.x = self.window.getWidth() - self.getWidth()
            self.y = randint(0, window.getHeight() - 5)
        if self.y > self.window.getHeight() - self.getHeight(): # bottom wall
            self.y = 0
            self.x = randint(0, window.getWidth() - 5)
        if self.y < 0: # top wall
            self.y = self.window.getHeight() - self.getHeight()
            self.x = randint(0, window.getWidth() - 5)

        self.pos = (self.x, self.y) # moving it based on new values

if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    stars = [Star(window, randint(0, window.getWidth() - 5), randint(0, window.getHeight() - 5)) for _ in range(120)]
    while True:
        window.getEvents()
        window.clearScreen()
        for ball in stars:
            window.blitSprite(ball)
            ball.move(window.getKeysPressed())
        window.updateScreen()