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
    blackColor = (0, 0, 0)
    whiteColor = (200, 200, 200)
    gridSize = windowHeight // 24
    

    def setMode(self): 
        return pygame.display.set_mode((self.windowHeight, self.windowWidth))

    def loadImage(self, imageName): 
        return pygame.image.load(self.imagesDir + imageName)

    def renderGameBackground(self, window):
        backGroundImage = self.loadImage("grid.jpg")
        window.blit(backGroundImage, (0,0))

    def renderGrid(self, window): 
        for i in range(15):
            pygame.draw.line(window, self.blackColor, (i * self.gridSize, 0), (i * self.gridSize, self.windowHeight), 1)
        for i in range(24): 
            pygame.draw.line(window, self.blackColor, (0, i * self.gridSize), (self.gridSize * 24, i * self.gridSize), 1)

    def renderScoreBoard(self, window): 
        scoreBoard = self.loadImage("score_board.jpg")
        window.blit(scoreBoard, (375, 0))


        
