'''
title: Player's star sprite
'''
from star import Star
from json import load
from random import choice, randint
from pygame.mixer import Sound

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
        self.setColour(self.data["colour"]["anchor"])
        self.range = int(self.window.getDimentions()[1]*0.7)
        self.frames = 0

    def playSounds(self):
        if not self.frames % self.data["fps"]//6 and not randint(0, 1):
            note = Sound("media/sounds/" + choice(self.data["chord" + str(self.chordNum)]["drone"]))
            note.set_volume(0.1)
            note.play()
        if not self.frames % (self.data["fps"]*5) and not randint(0, 1):
            note = Sound("media/sounds/" + choice(self.data["chord" + str(self.chordNum)]["bass"]))
            note.set_volume(0.25)
            note.play()
        self.frames += 1

    def getRange(self):
        return self.range