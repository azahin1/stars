'''
Sound mixer singleton class
'''
import pygame.mixer as mix
import os

class Sounds:
    __instance = None

    @staticmethod
    def getInstance():
        if Sounds.__instance == None:
            Sounds()
        return Sounds.__instance

    def __init__(self):
        if Sounds.__instance:
            raise Exception("Object Exists")
        mix.init()
        mix.set_num_channels(300)
        directory = "media/sounds"
        self.sounds = {name: mix.Sound(f"{directory}/{name}") for name in os.listdir(directory)}
        Sounds.__instance = self

    def getSounds(self):
        return self.sounds

if __name__ == "__main__":
    s = Sounds.getInstance()
    s.getSounds()["pad_3d.wav"].play()