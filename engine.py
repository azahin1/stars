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
        self.frameCount = 0

    def run(self):
        while True:
            self.window.getEvents()
            self.window.clearScreen()

            self.window.blitSprite(self.player)
            self.player.playSounds(self.frameCount)

            for star in self.backgroundStars:
                star.move(self.window.getKeysPressed())
                star.proximity(self.player)
                self.window.blitSprite(star)

            self.window.updateScreen()
            self.frameCount += 1

if __name__ == "__main__":
    game = Engine()
    game.run()