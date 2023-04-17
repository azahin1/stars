'''
title: stars that change the chord
'''
from star import Star
from json import load

class AnchorStar(Star):
    def __init__(self, window, i):
        super().__init__(window)
        with open("loader.json") as f:
            self.data = load(f)
        self.setColour(self.data["colour"]["anchor"])
        self.setDimentions(8, 8)
        self.accValue = 2
        self.chordNum = i
        if i == 1:
            self.pos[0] += self.window.getDimentions()[0]
            self.pos[1] -= self.window.getDimentions()[1]
        if i == 2:
            self.pos[1] += self.window.getDimentions()[1]
        if i == 3:
            self.pos[0] -= self.window.getDimentions()[0]

    def bounderies(self, i):
        if self.pos[i] < -self.window.getDimentions()[i]: # start wall
            self.pos[i] = self.window.getDimentions()[i]*2 - self.getDimentions()[i]
        if self.pos[i] > self.window.getDimentions()[i]*2 - self.getDimentions()[i]: # end wall
            self.pos[i] = -self.window.getDimentions()[i]