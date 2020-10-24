import pygame
import os 
import random
import math 
import time


class GameWindow():
    windowHeight = 600
    windowWidth = 575
    windowRunning = True
    imagesDir = os.getcwd() +  "/Images/"
    

    def setMode(self): 
        return pygame.display.set_mode((self.windowHeight, self.windowWidth))

    def loadImage(self, imageName): 
        return pygame.image.load(self.imagesDir + imageName)

        
