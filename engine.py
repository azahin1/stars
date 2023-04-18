'''
title: Engine (the main game)
'''
from pygame import init, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d
from window import Window
from star import Star
from playerStar import PlayerStar
from pluckStar import PluckStar
from anchorStar import AnchorStar
from shootingStar import ShootingStar
from text import Text
import pygame.mixer as mix

class Engine:
    def __init__(self):
        init()
        mix.init()
        mix.set_num_channels(50)

        #-- Game trackers
        self.window = Window() # game window
        self.frameCount = 0
        self.chordNum = 0
        self.phase = 0

        #-- Sprites
        self.player = PlayerStar(self.window) # player sprite
        self.backgroundStars = [Star(self.window) for _ in range(300)]
        self.shootingStars = [ShootingStar(self.window) for _ in range(4)]

        #-- Texts
        self.tutorialText2 = Text(self.window, "Move using Arrow Keys")
        self.tutorialText2.setPOS(self.window.getDimentions()[0] - self.tutorialText2.getDimentions()[0] - 10, self.window.getDimentions()[1] - self.tutorialText2.getDimentions()[1] - 5)
        
        self.title = Text(self.window, "Stars", 100)
        self.title.setPOS(self.window.getDimentions()[0]//2 - self.title.getDimentions()[0]//2, self.window.getDimentions()[1]//2 - self.title.getDimentions()[0] - 20)
        self.subtitle = Text(self.window, "Abrar Zahin", 15)
        self.subtitle.setPOS(self.window.getDimentions()[0]//2 - self.subtitle.getDimentions()[0]//2, self.title.getPOS()[1] + self.title.getDimentions()[1])

        self.tutorialText3 = Text(self.window, "Press Enter to finish")
        self.tutorialText3.setPOS(10, self.window.getDimentions()[1] - self.tutorialText3.getDimentions()[1] - 5)

    def run(self):
        while True:
            self.window.getEvents()
            
            phases = { # cheeky pythonic switch statement
                0: self.phase0,
                1: self.phase1,
                2: self.phase2
            }

            if self.phase in phases:
                phases[self.phase]()

            self.frameCount += 1
            self.updateScreen()

    def phase0(self):
        if self.frameCount == 0 or self.frameCount == 1:
            self.anchorStars = [AnchorStar(self.window, i + 1) for i in range(5)]

        self.title.modAlpha(8)
        self.subtitle.modAlpha(8)
        self.tutorialText2.modAlpha(8)

        self.player.setColour([253, 253, 151])
        self.player.glow(True)
        self.player.playSounds()

        self.pluckStars = []
        for star in self.backgroundStars:
            star.proximity(self.player)

        for key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d]:
            if self.window.getKeysPressed()[key]:
                self.frameCount = -1
                self.phase = 1

    def phase1(self):
        #-- Background Stars
        for star in self.backgroundStars: # moving background stars
            star.proximity(self.player)
            star.move(self.window.getKeysPressed())

        #-- Pluck Stars
        if not self.frameCount % 60 and len(self.pluckStars) < 15: # adds a pluck star every 2 sec
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

        #-- Player Star
        self.player.setBass(True)
        self.player.setChordNum(self.chordNum)
        self.player.playSounds()
        cont = self.player.move(self.window.getKeysPressed())

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

        #-- Tutorial Texts
        self.title.modAlpha(-18)
        self.subtitle.modAlpha(-18)
        self.tutorialText3.modAlpha(8)

        if cont:
            self.player.setBass(False)
            self.frameCount = 0
            self.phase = 2

    def phase2(self):
        if self.frameCount == 1:
            end = mix.Sound("media/sounds/end_swell.wav")
            for shot in self.shootingStars:
                shot.stop()
            end.set_volume(0.8)
            end.play()

        if self.frameCount > 120 and self.frameCount < 150:
            #-- Background Stars
            for star in self.backgroundStars:
                star.proximity(self.player)

            #-- Player Star
            self.player.fade()

            #-- Pluck Stars
            for pluck in self.pluckStars:
                pluck.fade()

            #-- Anchor Stars
            for anchor in self.anchorStars:
                anchor.fade()

            #-- Shooting Stars
            for shot in self.shootingStars:
                shot.fade()

            #-- Texts
            self.tutorialText2.modAlpha(-18)
            self.tutorialText3.modAlpha(-18)

        if self.frameCount == 180:
            self.player.setColour([253, 253, 151])
            self.player.glow(False)
            end = mix.Sound("media/sounds/end_pluck.wav")
            end.set_volume(0.25)
            end.play()

        if self.frameCount > 240:
            self.frameCount = 0
            self.phase = 0

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

        #-- Texts
        self.window.blitSprite(self.title)
        self.window.blitSprite(self.subtitle)
        self.window.blitSprite(self.tutorialText2)
        self.window.blitSprite(self.tutorialText3)

        self.window.updateScreen()

if __name__ == "__main__":
    game = Engine()
    game.run()