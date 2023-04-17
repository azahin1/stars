'''
title: Engine (the main game)
'''
from pygame import init
from window import Window
from star import Star
from playerStar import PlayerStar
from pluckStar import PluckStar
import pygame.mixer as mix

class Engine:
    def __init__(self):
        init()
        mix.init()
        mix.set_num_channels(300)
        self.window = Window() # game window
        self.player = PlayerStar(self.window) # player sprite
        self.backgroundStars = [Star(self.window) for _ in range(240)]
        self.pluckStars = []
        self.frameCount = 0
        self.chordNum = 1

    def run(self):
        while True:
            self.window.getEvents()
            self.window.clearScreen()

            self.window.blitSprite(self.player)
            self.player.setChordNum(self.chordNum)
            self.player.playSounds()

            if not self.frameCount % 600:
                self.chordNum = self.chordNum%2 + 1

            if not self.frameCount % 60 and len(self.pluckStars) < 20:
                self.pluckStars.append(PluckStar(self.window))
            
            for pluck in self.pluckStars:
                pluck.proximity(self.player)
                pluck.playSounds(self.player)
                pluck.setChordNum(self.chordNum)
                pluck.move(self.window.getKeysPressed())
                self.window.blitSprite(pluck)

            for star in self.backgroundStars:
                star.proximity(self.player)
                star.move(self.window.getKeysPressed())
                self.window.blitSprite(star)

            self.window.updateScreen()
            self.frameCount += 1

if __name__ == "__main__":
    game = Engine()
    game.run()