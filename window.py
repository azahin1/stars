'''
Title: Window frame
'''
import pygame
from loader import *

class Window:
    def __init__(self):
        self.title = TITLE # title of the window
        self.fps = FPS # frames per second
        self.width = WIDTH
        self.height = HEIGHT
        self.dimentions = (self.width, self.height) # dimentions of the window
        self.background = BACKGROUND_COLOUR # colour of the window
        self.frame = pygame.time.Clock() # updates the window in a frame
        self.screen = pygame.display.set_mode(self.dimentions)
        self.screen.fill(self.background) # colours the window
        self.caption = pygame.display.set_caption(self.title) # sets the title of the window
        self.keysPressed = None # the keys pressed in a keyboard

    ##-- modifiers
    def clearScreen(self): # fills the window back up
        self.screen.fill(self.background)

    def updateScreen(self): # updates the window
        self.frame.tick(self.fps)
        pygame.display.flip()

    def blitSprite(self, sprite): # draws a sprite into the window
        self.screen.blit(sprite.getSprite(), sprite.getPOS())

    ##-- accessors
    def getEvents(self): # inputs in a window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.keysPressed = pygame.key.get_pressed()

    def getWidth(self): # gets the width of the window
        return self.width

    def getHeight(self): # gets the height of the window
        return self.height

    def getKeysPressed(self): # gets the keys pressed in the window
        return self.keysPressed

if __name__ == "__main__":
    pygame.init()
    window = Window()

    while True:
        window.getEvents()
        window.clearScreen()
        window.updateScreen()