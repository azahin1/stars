'''
title: stars that change the chord
'''
from star import Star
from json import load
from random import randint, choice
from math import sin, cos, radians

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
        self.occulation = randint(1, 4)
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
        pass # empty