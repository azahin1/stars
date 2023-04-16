'''
title: Engine (the main game)
'''
from pygame import init
from window import Window
from star import Star
from playerStar import PlayerStar

class Engine:
    def __init__(self):
        init()
        self.window = Window() # game window
        self.player = PlayerStar(self.window) # player sprite
        self.backgroundStars = [Star(self.window) for _ in range(300)]

    def run(self):
        while True:
            self.window.getEvents()
            self.window.clearScreen()

            self.window.blitSprite(self.player)
            for star in self.backgroundStars:
                star.move(self.window.getKeysPressed())
                star.proximity(self.player)
                self.window.blitSprite(star)

            self.window.updateScreen()

if __name__ == "__main__":
    game = Engine()
    game.run()