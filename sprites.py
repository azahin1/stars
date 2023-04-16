'''
title: Sprites abstract class
'''
from pygame import Surface, SRCALPHA

class Sprite:
    def __init__(self, window, x = 0, y = 0):
        self.window = window # the main window of the mage
        self.dimentions = [100, 100] # dimentions of the sprite
        self.sprite = Surface(self.dimentions, SRCALPHA, 32) # creating the sprite
        self.colour = (255, 255, 255)
        self.sprite.fill(self.colour) # colouring in the sprite
        self.pos = [x, y] # positioning the sprite

    ##-- modifiers
    def updateSprite(self): # updates the dimentions and colour of the sprite
        self.sprite = Surface(self.dimentions, SRCALPHA, 32)
        self.sprite.fill(self.colour)

    def setDimentions(self, width, height): # changes both width and height of the sprite
        self.dimentions = [width, height]
        self.updateSprite()

    def setColour(self, colour): # changes the colour of the sprite
        self.colour = colour
        self.updateSprite()

    def setPOS(self, x, y): # changes the position of the sprite
        self.pos = [x, y]

    ##-- accessors
    def getSprite(self): # returns the sprite
        return self.sprite

    def getDimentions(self): # gets the dimentions of the sprite
        return self.dimentions

    def getPOS(self): # gets the position of the sprite
        return self.pos

if __name__ == "__main__":
    from window import Window
    from pygame import init

    init()
    window = Window()
    sprite = Sprite(window)
    while True:
        window.getEvents()
        window.clearScreen()
        window.blitSprite(sprite)
        window.updateScreen()