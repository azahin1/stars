'''
title: Player's star sprite
'''
from star import Star
from json import load

class PlayerStar(Star):
    def __init__(self, window):
        Star.__init__(self, window)
        with open("loader.json") as f:
            data = load(f)
        self.setDimentions(12, 12)
        self.setPOS( # middle of the screen
            self.window.getDimentions()[0]/2 - self.getDimentions()[0]/2,
            self.window.getDimentions()[1]/2 - self.getDimentions()[1]/2
        )
        self.setColour(data["colour"]["player"])