'''
title: stars that change the chord
'''
from star import Star
from json import load
from random import randint, choice
from math import sin, cos, radians
from pygame.mixer import Sound

class ShootingStar(Star):
    def __init__(self, window):
        super().__init__(window)
        with open("loader.json") as f:
            self.data = load(f)
        self.resetTrejectory()
        self.setDimentions(5, 5)
        self.setColour(self.data["colour"]["anchor"])
        self.frame = 0

    def resetTrejectory(self):
        trejectory = randint(1, 4)
        # self.occulation = randint(1, 4)
        self.occulation = 2
        self.rate = randint(30, 60)
        [w, h] = self.window.getDimentions()
        if trejectory == 1: # up right
            self.pos = choice([[0, randint(h//2, h - self.dimentions[1])] , [randint(0, w//2), h - self.dimentions[1]]])
            self.speed = [randint(10, 15), randint(-15, -10)]
        if trejectory == 2: # up left
            self.pos = choice([[w - self.dimentions[0], randint(h//2, h - self.dimentions[1])] , [randint(w//2, w - self.dimentions[0]), h - self.dimentions[1]]])
            self.speed = [randint(-15, -10), randint(-15, -10)]
        if trejectory == 3: # down right
            self.pos = choice([[0, randint(0, h//2)] , [randint(0, w//2), 0]])
            self.speed = [randint(10, 15), randint(10, 15)]
        if trejectory == 4: # down left
            self.pos = choice([[w - self.dimentions[0], randint(0, h//2)] , [randint(w//2, w - self.dimentions[0]), 0]])
            self.speed = [randint(-15, -10), randint(10, 15)]

        r = randint(1, 2)
        self.arpL = Sound(f"media/sounds/arp_{self.chordNum}{self.occulation}{r}_left.wav")
        self.arpR = Sound(f"media/sounds/arp_{self.chordNum}{self.occulation}{r}_right.wav")
        self.arpL.set_volume(0)
        self.arpR.set_volume(0)
        self.arpL.play(-1)
        self.arpR.play(-1)
        print(f"media/sounds/arp_{self.chordNum}{self.occulation}{r}")

    def playSounds(self, player):
        dist = 0
        for i in range(2):
            dist += (self.pos[i] - player.getPOS()[i])**2
        dist **= (1/2)
        dist /= player.getRange()
        if dist > 1:
            dist = 1
        
        volumeMod = (self.pos[0] - player.getPOS()[0])/player.getRange()

        self.arpL.set_volume(max(0.0, (1 - 1*dist)*0.2*(volumeMod - 1)/-2))
        self.arpR.set_volume(max(0.0, (1 - 1*dist)*0.2*(volumeMod + 1)/2))

    def move(self, keys):
        super().move(keys)
        for i in range(2):
            self.pos[i] += (self.speed[i])
        if self.occulation == 2: # vertical
            self.pos[1] += int(sin(radians(self.frame*self.rate)) * self.rate//4)
        if self.occulation == 3: # horizontal
            self.pos[0] += int(cos(radians(self.frame*self.rate)) * self.rate//4)
        if self.occulation == 4: # circular
            self.pos[1] += int(sin(radians(self.frame*self.rate//2)) * self.rate//2)
            self.pos[0] += int(cos(radians(self.frame*self.rate//2)) * self.rate//2)
        self.frame += 1

    def bounderies(self, i):
        if self.pos[i] < 0 or self.pos[i] > self.window.getDimentions()[i] - self.getDimentions()[i]: # walls
            self.arpL.fadeout(100)
            self.arpR.fadeout(100)