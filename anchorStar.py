'''
title: stars that change the chord
'''
from star import Star
from json import load
from random import randint
from math import sin, radians

class AnchorStar(Star):
    def __init__(self, window, i):
        super().__init__(window)
        with open("loader.json") as f:
            self.data = load(f)
        self.setColour(self.data["colour"]["anchor"][i])
        self.setDimentions(8, 8)
        [w, h] = self.window.getDimentions()
        self.setPOS(randint(w//3, 2*w//3), randint(h//3, 2*h//3))
        self.accValue = 2
        self.frameCount = 0
        self.chordNum = i
        # player chord is C6
        if i == 1: # Dsus4(add6)
            self.pos[0] -= self.window.getDimentions()[0]
        if i == 2: # Emin7
            self.pos[0] += self.window.getDimentions()[0]
            self.pos[1] += self.window.getDimentions()[1]
        if i == 3: # Emin/F
            self.pos[1] -= self.window.getDimentions()[1]
        if i == 4: # G7
            self.pos[0] += self.window.getDimentions()[0]
        if i == 5: # Csus2/A
            self.pos[0] -= self.window.getDimentions()[0]
            self.pos[1] += self.window.getDimentions()[1]

    def bounderies(self, i):
        if self.pos[i] < -self.window.getDimentions()[i]: # start wall
            self.pos[i] = self.window.getDimentions()[i]*2 - self.getDimentions()[i]
        if self.pos[i] > self.window.getDimentions()[i]*2 - self.getDimentions()[i]: # end wall
            self.pos[i] = -self.window.getDimentions()[i]

    def inRange(self, player):
        dist = 0
        for i in range(2):
            dist += (self.pos[i] - player.getPOS()[i])**2
        dist **= (1/2)

        return dist < player.getRange()*(0.5)

    def move(self, keys):
        super().move(keys)
        self.sprite.set_alpha(200 + int(55*sin(radians(self.frameCount))))
        self.frameCount = (self.frameCount + 10) % 360

    def getChordNum(self):
        return self.chordNum