'''
title: stars that pluck
'''
from star import Star
from json import load
from random import choice, randint
from pygame.mixer import Sound

class PluckStar(Star):
    def __init__(self, window):
        Star.__init__(self, window)
        with open("loader.json") as f:
            self.data = load(f)
        self.size = choice([1, 2, 3, 4, 5, 5, 6, 7])
        self.accValue = (self.size + 2)/10
        self.setDimentions(self.size, self.size)
        self.setColour(self.data["colour"]["pluck"])
        self.setChord()
        self.frameCount = 0
        self.alpha = 0
        self.rate = self.size*self.data["fps"] + randint(0, 15)

    def playSounds(self, player):
        dist = 0
        for i in range(2):
            dist += (self.pos[i] - player.getPOS()[i])**2
        dist **= (1/2)
        dist /= player.getRange()
        if dist > 1:
            dist = 1
        
        volumeMod = (self.pos[0] - player.getPOS()[0])/player.getRange()

        self.noteL.set_volume((1 - dist)*0.2*(volumeMod - 1)/-2)
        self.noteR.set_volume((1 - dist)*0.2*(volumeMod + 1)/2)

        if self.frameCount == self.rate:
            self.frameCount = 0
            self.alpha = int((1 - 0.8*dist)*255)
            self.noteL.play(maxtime = 1000)
            self.noteR.play(maxtime = 1000)

        self.alpha -= 2
        if self.alpha < 0:
            self.alpha = 0
        self.sprite.set_alpha(self.alpha)
        self.frameCount += 1
    
    def bounderies(self, i):
        j = (i + 1)%2
        if self.pos[i] < 0: # start wall
            self.pos[i] = self.window.getDimentions()[i] - self.getDimentions()[i]
            self.pos[j] = randint(0, self.window.getDimentions()[j] - self.getDimentions()[j])
            self.setChord()
        if self.pos[i] > self.window.getDimentions()[i] - self.getDimentions()[i]: # end wall
            self.pos[i] = 0
            self.pos[j] = randint(0, self.window.getDimentions()[j] - self.getDimentions()[j])
            self.setChord()

    def setChord(self):
        note = f"pluck_{choice(self.data['chord' + str(self.chordNum)]['pluck'])}"
        self.noteL = Sound("media/sounds/" + note + "_left.mp3")
        self.noteR = Sound("media/sounds/" + note + "_right.mp3")

    def setChordNum(self, num):
        self.chordNum = num
        self.setChord()