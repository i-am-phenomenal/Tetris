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

class BackGroundMusic(): 
    pygame.init()
    musicDir = os.getcwd() + "/Music/"
    kalinka = pygame.mixer.Sound(musicDir + "kalinka.ogg")
    katyusha = pygame.mixer.Sound(musicDir + "katyusha.ogg")
    korobushka = pygame.mixer.Sound(musicDir + "korobushka.ogg")
    smuglianka = pygame.mixer.Sound(musicDir + "smuglianka.ogg")

    def playRandomMusic(self): 
        music = random.choice([self.kalinka, self.katyusha, self.korobushka, self.smuglianka])
        pygame.mixer.Channel(0).play(music, -1)

class Block(GameWindow): 
    gameWindow = GameWindow()
    possibleXCoords = [x for x in range(326) if x % GameWindow.gridSize == 0]
    possibleYCoords = [y for y in range(531) if y % GameWindow.gridSize == 0]
    possibleRows = [x for x in range(15)]
    def __init__(self): 
        self.xCoord = random.choice(self.possibleXCoords)
        self.yCoord = 100
        self.shape = ""
        self.isFalling = True
        self.blockYCoordCounter = 0
        self.row = random.choice(self.possibleRows)
        self.column = 0

    def returnRandomBlockShape(self, blockShape): 
        if blockShape == "cube-block": 
            self.shape = self.gameWindow.loadImage("cube-block.png")
        elif blockShape == "i": 
            self.shape = self.gameWindow.loadImage("i-block.png")
        elif blockShape == "j":
            self.shape = self.gameWindow.loadImage("j-block.png")
        elif blockShape == "L": 
            self.shape = self.gameWindow.loadImage("L-block.png")
        elif blockShape == "rs": 
            self.shape = self.gameWindow.loadImage("r-s-block.png")
        elif blockShape == "s": 
            self.shape = self.gameWindow.loadImage("s-block.png")
        elif blockShape == "t": 
            self.shape = self.gameWindow.loadImage("t-block.png")
        else:
            raise "Invalid Value for Block Shape"


    def generateBlock(self, window): 
        return window.blit(self.shape, (self.row * GameWindow.gridSize, self.column * GameWindow.gridSize))

    def updateBlockYCoordCounter(self): 
        length = len(self.possibleYCoords) - 1
        counter = self.blockYCoordCounter
        if  counter == length: 
            self.blockYCoordCounter =  0
        elif counter < length: 
            self.blockYCoordCounter =  counter + 1
        elif counter > length: 
            self.blockYCoordCounter = 0
        else:
            self.blockYCoordCounter = counter

    def renderBlockDownwardMotion(self, window): 
        if self.isFalling:
            self.column += 1
        else: 
            pass

    def renderUpdatedPosition(self, window):
        window.blit(self.shape, (self.row * GameWindow.gridSize, self.column * GameWindow.gridSize))
