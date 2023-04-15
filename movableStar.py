'''
title: paddle (player) sprite
'''
from star import Star
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT
from loader import *

class MovableStar(Star): # inherits from the Sprite class
    def __init__(self, window):
        Star.__init__(self, window)
        self.setDimentions(50, 50)
        self.setPOS(self.window.getWidth()/2 - self.getWidth()/2, self.window.getHeight()/2 - self.getHeight()/2)
        self.setColour(STAR_COLOUR)
        self.spd = 8 # speed of the star

    def move(self, keys): # moving the paddle with key presses
        if keys[K_LEFT]: # a key moves it left
            self.x -= self.spd
        if keys[K_RIGHT]: # d key moves it right
            self.x += self.spd
        if keys[K_UP]: # a key moves it left
            self.y -= self.spd
        if keys[K_DOWN]: # d key moves it right
            self.y += self.spd

        #-- bounderies
        if self.x > self.window.getWidth() - self.getWidth(): # right wall
            self.x = self.window.getWidth() - self.getWidth()
        if self.x < 0: # left wall
            self.x = 0
        if self.y > self.window.getHeight() - self.getHeight(): # bottom wall
            self.y = self.window.getHeight() - self.getHeight()
        if self.y < 0: # top wall
            self.y = 0

        self.pos = (self.x, self.y) # moving it based on new values
        self.spd = 8 # keeping the speed the same

if __name__ == "__main__":
    from window import Window
    from pygame import init

    init()
    window = Window()
    player = MovableStar(window)

    while True:
        window.getEvents()
        window.clearScreen()
        window.blitSprite(player)
        player.move(window.getKeysPressed())
        window.updateScreen()