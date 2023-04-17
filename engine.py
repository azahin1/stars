'''
title: Engine (the main game)
'''
from pygame import init
from window import Window
from star import Star
from playerStar import PlayerStar
from pluckStar import PluckStar
from anchorStar import AnchorStar
from shootingStar import ShootingStar
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
        self.anchorStars = [AnchorStar(self.window, i + 1) for i in range(5)]
        self.shootingStars = [ShootingStar(self.window) for _ in range(3)]
        self.frameCount = 0
        self.chordNum = 0

    def run(self):
        while True:
            self.window.getEvents()
            self.window.clearScreen()

            if not self.frameCount % 60 and len(self.pluckStars) < 30:
                self.pluckStars.append(PluckStar(self.window))
            
            #-- Background Stars
            for star in self.backgroundStars:
                star.proximity(self.player)
                star.move(self.window.getKeysPressed())
                self.window.blitSprite(star)
    
            #-- Player Star
            self.player.setChordNum(self.chordNum)
            self.player.playSounds()
            self.window.blitSprite(self.player)

            #-- Pluck Stars
            for pluck in self.pluckStars:
                pluck.proximity(self.player)
                pluck.playSounds(self.player)
                pluck.setChordNum(self.chordNum)
                pluck.move(self.window.getKeysPressed())
                self.window.blitSprite(pluck)

            #-- Anchor Stars
            self.chordNum = 0
            for anchor in self.anchorStars:
                anchor.move(self.window.getKeysPressed())
                self.window.blitSprite(anchor)
                if anchor.inRange(self.player):
                    self.chordNum = anchor.getChordNum()

            #-- Shooting Stars
            for i, shooting in enumerate(self.shootingStars):
                shooting.proximity(self.player)
                if not (self.frameCount + 15*i) % 90 and not shooting.isActive():
                    shooting.resetTrejectory()
                if shooting.isActive():
                    shooting.setChordNum(self.chordNum)
                    shooting.playSounds(self.player)
                    shooting.move(self.window.getKeysPressed())
                    self.window.blitSprite(shooting)

            self.window.updateScreen()
            self.frameCount += 1

if __name__ == "__main__":
    game = Engine()
    game.run()