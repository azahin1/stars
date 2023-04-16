'''
title: Star sprite
'''
from sprites import Sprite
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d
from random import randint
from json import load

class Star(Sprite): # inherits from Sprite class
    def __init__(self, window):
        Sprite.__init__(self, window)
        with open("loader.json") as f:
            data = load(f)
        size = randint(1, 5)
        self.setDimentions(size, size)
        self.setPOS(randint(0, self.window.getDimentions()[0] - self.getDimentions()[0]), randint(0, self.window.getDimentions()[1] - self.getDimentions()[1]))
        self.setColour(data["colour"]["star"])
        self.sprite.set_alpha(0)
        self.accValue = (size + 2)/10
        self.friction = -0.1
        self.velocity = [0, 0]
        self.accelaration = [0, 0]
        
    def move(self, keys): # moving the paddle with key presses
        self.accelaration = [0, 0] # reset acceleration

        #-- update acceleration when keys are pressed
        if keys[K_LEFT] or keys[K_a]:
            self.accelaration[0] = self.accValue
        if keys[K_RIGHT] or keys[K_d]:
            self.accelaration[0] = -self.accValue
        if keys[K_UP] or keys[K_w]:
            self.accelaration[1] = self.accValue
        if keys[K_DOWN] or keys[K_s]:
            self.accelaration[1] = -self.accValue

        #-- update position with acceleration
        for i in range(2):
            self.accelaration[i] += self.velocity[i] * self.friction
            self.velocity[i] += self.accelaration[i]
            self.pos[i] += self.velocity[i] + self.accelaration[i]/2

            #-- bounderies
            j = (i + 1)%2
            if self.pos[i] < 0: # start wall
                self.pos[i] = self.window.getDimentions()[i] - self.getDimentions()[i]
                self.pos[j] = randint(0, self.window.getDimentions()[j] - self.getDimentions()[j])
            if self.pos[i] > self.window.getDimentions()[i] - self.getDimentions()[i]: # end wall
                self.pos[i] = 0
                self.pos[j] = randint(0, self.window.getDimentions()[j] - self.getDimentions()[j])

    def proximity(self, player):
        dist = 0
        for i in range(2):
            dist += (self.pos[i] - player.getPOS()[i])**2
        dist **= (1/2)

        brightness = max(0, int(255*((player.getRange() - dist)/player.getRange())))
        self.sprite.set_alpha(brightness)
    
if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    stars = [Star(window) for _ in range(300)]
    player = Star(window, 10, 10)
    player.setPOS(window.getDimentions()[0]/2 - player.getDimentions()[0]/2, window.getDimentions()[1]/2 - player.getDimentions()[1]/2)
    while True:
        window.getEvents()
        window.clearScreen()
        window.blitSprite(player)
        for star in stars:
            star.move(window.getKeysPressed())
            window.blitSprite(star)
        window.updateScreen()