'''
title: stars that pluck
'''
from star import Star
from json import load
from sounds import Sounds
from random import choice, randint

class PluckStar(Star):
    def __init__(self, window):
        Star.__init__(self, window)
        with open("loader.json") as f:
            self.data = load(f)
        self.size = randint(3, 6)
        self.accValue = (self.size + 2)/10
        self.setDimentions(self.size, self.size)
        self.setColour(self.data["colour"]["player"])
        note = f"pluck_{choice(self.data['notes']['pluck'])}"
        loader = Sounds.getInstance()
        self.noteL = loader.getSounds()[note + "_left.wav"]
        self.noteR = loader.getSounds()[note + "_right.wav"]
        self.frameCount = 0
        self.alpha = 0
        self.rate = self.size*self.data["fps"] + randint(0, 15)

    def playSounds(self, player):
        if self.frameCount == self.rate:
            self.frameCount = 0
            dist = 0
            for i in range(2):
                dist += (self.pos[i] - player.getPOS()[i])**2
            dist **= (1/2)
            dist /= player.getRange()
            if dist > 1:
                dist = 1
            
            self.alpha = int((1 - 0.8*dist)*255)
            volumeMod = (self.pos[0] - player.getPOS()[0])/player.getRange()

            self.noteL.set_volume((1 - dist)*0.2*(volumeMod - 1)/-2)
            self.noteR.set_volume((1 - dist)*0.2*(volumeMod + 1)/2)
            self.noteL.play(maxtime = 1000)
            self.noteR.play(maxtime = 1000)

        self.alpha -= 2
        if self.alpha < 0:
            self.alpha = 0
        self.sprite.set_alpha(self.alpha)
        self.frameCount += 1

    def getRange(self):
        return self.range