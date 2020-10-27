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
    currentlyPlaying = None
    pause = False

    def playRandomMusic(self): 
        music = random.choice([self.kalinka, self.katyusha, self.korobushka, self.smuglianka])
        self.currentlyPlaying = music
        pygame.mixer.Channel(0).play(music, -1)

    def togglePauseUnPause(self): 
        if not self.pause: 
            pygame.mixer.Channel(0).pause()
            self.pause = True
        else: 
            pygame.mixer.Channel(0).unpause()
            self.pause = False

class GameStats(): 
    def __init__(self): 
        self.isPaused = False  
        self.score = 0
        self.highScore = 0
        self.level = 0

    def pauseGame(self): 
        if self.isPaused: 
            pygame.time.wait(9999)
        else:
            pass

    def unpauseGame(self): 
        if not self.isPaused:
            pygame.time.wait(0)
        else: 
            pass



class Block(GameWindow): 
    gameWindow = GameWindow()
    possibleXCoords = [x for x in range(326) if x % GameWindow.gridSize == 0]
    possibleYCoords = [y for y in range(531) if y % GameWindow.gridSize == 0]
    possibleRows = [x for x in range(15)]

    def __init__(self): 
        self.xCoord = random.choice(self.possibleXCoords)
        self.yCoord = 100
        self.shape = ""
        self.blockShape = ""
        self.isFalling = True
        self.blockYCoordCounter = 0
        self.column = random.choice(self.possibleRows)
        self.row = 0

    def returnRandomBlockShape(self, blockShape): 
        if blockShape == "cube-block": 
            self.shape = self.gameWindow.loadImage("cube-block.png")
            self.blockShape = "cube"
        elif blockShape == "i": 
            self.shape = self.gameWindow.loadImage("i-block.png")
            self.blockShape = "i"
        elif blockShape == "j":
            self.shape = self.gameWindow.loadImage("j-block.png")
            self.blockShape = "j"
        elif blockShape == "L": 
            self.shape = self.gameWindow.loadImage("L-block.png")
            self.blockShape = "L"
        elif blockShape == "rs": 
            self.shape = self.gameWindow.loadImage("r-s-block.png")
            self.blockShape = "rs"
        elif blockShape == "s": 
            self.shape = self.gameWindow.loadImage("s-block.png")
            self.blockShape = "s"
        elif blockShape == "t": 
            self.shape = self.gameWindow.loadImage("t-block.png")
            self.blockShape = "t"
        else:
            raise "Invalid Value for Block Shape"

    def renderBlockAtPosition(self, window, row, col): 
        gridSize = GameWindow.gridSize
        print((row * gridSize, col * gridSize) )
        window.blit(self.shape, (30 * gridSize, 18 * gridSize))
    
    def renderBlocksForTesting(self, window):
        gridSize = GameWindow.gridSize
        cubeShape = self.gameWindow.loadImage("cube-block.png")
        jShape = self.gameWindow.loadImage("j-block.png")
        lShape = self.gameWindow.loadImage("L-block.png")
        window.blit(cubeShape, (0, 21 * gridSize))
        window.blit(jShape, (2 * gridSize, 21 * gridSize))
        window.blit(lShape, (4 * gridSize, 21 * gridSize))

    def generateBlock(self, window):
        # need to remove
        self.shape = self.gameWindow.loadImage("cube-block.png")
        self.blockShape = "cube"
        return window.blit(self.shape, (self.column * GameWindow.gridSize, self.row * GameWindow.gridSize))

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
            self.row += 1
        else: 
            pass

    def renderUpdatedPosition(self, window):
        window.blit(self.shape, (self.column * GameWindow.gridSize, self.row * GameWindow.gridSize))

    def moveLeft(self): 
        if self.isFalling: 
            self.column -= 1
        else: 
            pass

    def moveRight(self): 
        if self.isFalling:
            self.column += 1
        else: 
            pass

    def checkCollisionForCube(self, collapsedBlocks, currentBlock): 
        for collapsedBlock in collapsedBlocks: 
            columnCondition = abs(collapsedBlock.column - currentBlock.column) < 2
            if collapsedBlock.row == currentBlock.row + 2 and columnCondition:
                currentBlock.isFalling= False
                return True
            else:
                pass
        return False