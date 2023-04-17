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
        self.arpL = None
        self.arpR = None
        self.active = False
        self.resetTrejectory()
        self.setColour(self.data["colour"]["anchor"])
        self.frame = 0

    def resetTrejectory(self):
        if randint(0, 1):
            self.active = True

            trejectory = randint(1, 4)
            self.occulation = randint(2, 3)
            self.rate = randint(30, 60)
            [w, h] = self.window.getDimentions()
            if trejectory == 1: # up right
                self.pos = choice([[0, randint(2*h//3, h - self.dimentions[1])] , [randint(0, w//3), h - self.dimentions[1]]])
                self.speed = [randint(10, 15), randint(-12, -8)]
            if trejectory == 2: # up left
                self.pos = choice([[w - self.dimentions[0], randint(2*h//3, h - self.dimentions[1])] , [randint(2*w//3, w - self.dimentions[0]), h - self.dimentions[1]]])
                self.speed = [randint(-15, -10), randint(-12, -8)]
            if trejectory == 3: # down right
                self.pos = choice([[0, randint(0, h//3)] , [randint(0, w//3), 0]])
                self.speed = [randint(10, 15), randint(8, 12)]
            if trejectory == 4: # down left
                self.pos = choice([[w - self.dimentions[0], randint(0, h//3)] , [randint(2*w//3, w - self.dimentions[0]), 0]])
                self.speed = [randint(-15, -10), randint(8, 12)]

            r = randint(1, 2)
            self.arpL = Sound(f"media/sounds/arp_{self.chordNum}{self.occulation}{r}_left.wav")
            self.arpR = Sound(f"media/sounds/arp_{self.chordNum}{self.occulation}{r}_right.wav")
            self.arpL.set_volume(0)
            self.arpR.set_volume(0)
            self.arpL.play(-1)
            self.arpR.play(-1)

    def playSounds(self, player):
        dist = 0
        for i in range(2):
            dist += (self.pos[i] - player.getPOS()[i])**2
        dist **= (1/2)
        dist /= player.getRange()
        if dist > 1.2:
            dist = 1.2
        
        volumeMod = (self.pos[0] - player.getPOS()[0])/player.getRange()
        if self.arpL and self.arpR:
            self.arpL.set_volume(max(0.0, (1 - dist)*0.15*(volumeMod - 1)/-2))
            self.arpR.set_volume(max(0.0, (1 - dist)*0.15*(volumeMod + 1)/2))

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
        if self.pos[i] < -self.window.getDimentions()[i]//4 or self.pos[i] > int(self.window.getDimentions()[i]*1.25): # walls
            self.arpL.stop()
            self.arpR.stop()
            self.active = False

    def isActive(self):
        return self.active