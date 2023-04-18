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
        self.backgroundStars = [Star(self.window) for _ in range(300)]
        self.pluckStars = []
        self.anchorStars = [AnchorStar(self.window, i + 1) for i in range(5)]
        self.shootingStars = [ShootingStar(self.window) for _ in range(4)]
        self.frameCount = 0
        self.chordNum = 0
        self.phase = 1

    def run(self):
        while True:
            self.window.getEvents()
            
            { # cheeky pythonic switch statement
                1: self.phase1
            }[self.phase]()

            self.frameCount += 1
            self.updateScreen()

    def phase1(self):
        #-- Background Stars
        for star in self.backgroundStars: # moving background stars
            star.proximity(self.player)
            star.move(self.window.getKeysPressed())

        #-- Player Star
        self.player.setChordNum(self.chordNum)
        self.player.playSounds()

        #-- Pluck Stars
        if not self.frameCount % 60 and len(self.pluckStars) < 30: # adds a pluck star every 2 sec
            self.pluckStars.append(PluckStar(self.window))

        for pluck in self.pluckStars: # moving and playing pluck stars
            pluck.proximity(self.player)
            pluck.playSounds(self.player)
            pluck.setChordNum(self.chordNum)
            pluck.move(self.window.getKeysPressed())

        #-- Anchor Stars
        self.chordNum = 0
        for anchor in self.anchorStars:
            anchor.move(self.window.getKeysPressed())
            if anchor.inRange(self.player): # changes chord of the song based on which anchor star is near
                self.chordNum = anchor.getChordNum()

        #-- Shooting Stars
        for i, shot in enumerate(self.shootingStars):
            shot.proximity(self.player)
            if not self.frameCount % 250: # makes the shooting stars appear more often as time goes on
                shot.decreaseFreq()
            if not (self.frameCount + 30*i) % 150 and not shot.isActive(): # resets trajectory when the shooting star is inactive
                shot.resetTrejectory()
            if shot.isActive(): # making it do things
                shot.setChordNum(self.chordNum)
                shot.playSounds(self.player)
                shot.move(self.window.getKeysPressed())

    def updateScreen(self):
        self.window.clearScreen()

        #-- Background Stars
        for star in self.backgroundStars:
            self.window.blitSprite(star)

        #-- Player Star
        self.window.blitSprite(self.player)

        #-- Pluck Stars
        for pluck in self.pluckStars:
            self.window.blitSprite(pluck)

        #-- Anchor Stars
        for anchor in self.anchorStars:
            self.window.blitSprite(anchor)

        #-- Shooting Stars
        for shot in self.shootingStars:
            if shot.isActive():
                self.window.blitSprite(shot)

        self.window.updateScreen()

if __name__ == "__main__":
    game = Engine()
    game.run()