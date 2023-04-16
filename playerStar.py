'''
title: Player's star sprite
'''
from star import Star
from json import load
from sounds import Sounds
from random import choice, randrange

class PlayerStar(Star):
    def __init__(self, window):
        Star.__init__(self, window)
        with open("loader.json") as f:
            self.data = load(f)
        self.setDimentions(12, 12)
        self.setPOS( # middle of the screen
            self.window.getDimentions()[0]/2 - self.getDimentions()[0]/2,
            self.window.getDimentions()[1]/2 - self.getDimentions()[1]/2
        )
        self.setColour(self.data["colour"]["player"])
        self.range = int(self.window.getDimentions()[1]*0.7)

    def playSounds(self, frames):
        loader = Sounds.getInstance()
        if not frames % randrange(self.data["fps"], 6*self.data["fps"], self.data["fps"]//2):
            note = loader.getSounds()[choice(self.data["notes"]["drone"])]
            note.set_volume(0.3)
            # note.play()

    def getRange(self):
        return self.range