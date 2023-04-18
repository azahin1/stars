'''
Title: Window frame
'''
import pygame
from json import load
from sys import exit

class Window:
    def __init__(self):
        with open("loader.json") as f:
            data = load(f)
        self.title = data["title"] # title of the window
        self.fps = data["fps"] # frames per second
        self.dimentions = data["dimentions"] # dimentions of the window
        self.background = data["colour"]["background"] # colour of the window
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
                pygame.mixer.quit()
                pygame.quit()
                exit()
        self.keysPressed = pygame.key.get_pressed()

    def getDimentions(self): # gets the dimentions of the window
        return self.dimentions

    def getKeysPressed(self): # gets the keys pressed in the window
        return self.keysPressed

if __name__ == "__main__":
    pygame.init()
    window = Window()

    while True:
        window.getEvents()
        window.clearScreen()
        window.updateScreen()