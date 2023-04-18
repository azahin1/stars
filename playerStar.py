'''
title: Player's star sprite
'''
from star import Star
from json import load
from random import choice, randint
from pygame.mixer import Sound
from pygame import K_SPACE, K_RETURN

class PlayerStar(Star):
    def __init__(self, window):
        Star.__init__(self, window)
        with open("loader.json") as f:
            self.data = load(f)
        self.setDimentions(8, 8)
        self.setPOS( # middle of the screen
            self.window.getDimentions()[0]/2 - self.getDimentions()[0]/2,
            self.window.getDimentions()[1]/2 - self.getDimentions()[1]/2
        )
        self.maxRange = int(self.window.getDimentions()[1]*0.7)
        self.colour = [253, 253, 151]
        self.range = self.maxRange
        self.brightness = 200
        self.frames = 0
        self.bass = False

    def playSounds(self):
        if not self.frames % self.data["fps"]//6 and not randint(0, 3):
            note = Sound("media/sounds/" + choice(self.data["chord" + str(self.chordNum)]["drone"]))
            note.set_volume(0.1)
            note.play()
        if not self.frames % (self.data["fps"]*5) and not randint(0, 1) and self.bass:
            note = Sound("media/sounds/" + choice(self.data["chord" + str(self.chordNum)]["bass"]))
            note.set_volume(0.25)
            note.play()
        self.frames += 1

    def move(self, keys):
        newColour = self.data["colour"]["anchor"][self.chordNum]
        for i in range(len(self.colour)):
            diff = newColour[i] - self.colour[i]
            if diff < -10:
                diff = -10
            if diff > 10:
                diff = 10
            self.colour[i] += diff
        self.setColour(self.colour)
        self.glow()

        return keys[K_RETURN] or keys[K_SPACE]

    def glow(self, span = True):
        self.sprite.set_alpha(self.brightness)
        if span:
            self.range += 20
            if self.range > self.maxRange:
                self.range = self.maxRange

    def fade(self):
        super().fade()
        self.range -= 50
        if self.range < 1:
            self.range = 1

    def setBass(self, bul):
        self.bass = bul

    def getRange(self):
        return self.range