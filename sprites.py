'''
title: Sprites abstract class
'''
from pygame import Surface, SRCALPHA

class Sprite:
    def __init__(self, window, x = 0, y = 0):
        self.window = window # the main window of the mage
        self.width = 100
        self.height = 100
        self.dimentions = (self.width, self.height) # dimentions of the sprite
        self.sprite = Surface(self.dimentions, SRCALPHA, 32) # creating the sprite
        self.colour = (255, 255, 255)
        self.sprite.fill(self.colour) # colouring in the sprite
        self.x = x
        self.y = y
        self.pos = (self.x, self.y) # positioning the sprite

    ##-- modifiers
    def updateSprite(self): # updates the dimentions and colour of the sprite
        self.dimentions = (self.width, self.height)
        self.sprite = Surface(self.dimentions, SRCALPHA, 32)
        self.sprite.fill(self.colour)

    def setWidth(self, width): # changes the width of the sprite
        self.width = width
        self.updateSprite()

    def setHeight(self, height): # changes the height of the sprite
        self.height = height
        self.updateSprite()

    def setDimentions(self, width, height): # changes both width and height of the sprite
        self.width = width
        self.height = height
        self.updateSprite()

    def setColour(self, colour): # changes the colour of the sprite
        self.colour = colour
        self.updateSprite()

    def setX(self, x): # changes the x position of the sprite
        self.x = x
        self.pos = (self.x, self.y)

    def setY(self, y): # changes the y position of the sprite
        self.y = y
        self.pos = (self.x, self.y)

    def setPOS(self, x, y): # changes the position of the sprite
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    ##-- accessors
    def getSprite(self): # returns the sprite
        return self.sprite

    def getWidth(self): # gets the width og the sprite
        return self.width

    def getHeight(self): # gets the height of the sprite
        return self.height

    def getX(self): # gets the x position of the sprite
        return self.x

    def getY(self): # gets the y position of the sprite
        return self.y

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