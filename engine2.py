import pygame
import os 
import random
import math 
import time
from classes import GameWindow, BackGroundMusic, Block, GameStats

blocksOnScreen = []
collapsedBlocks = []
possibleBlockShapes = [
    "cube-block",
    "i",
    "j",
    "L",
    "rs",
    "s",
    "t"
]

# 23 rows and 15 cols
grid =  [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]

def printGrid():
    global grid
    for row in grid:
        print(row)
    print("\n")

def updateGrid(collapsedBlocks): 
    global grid
    for block in collapsedBlocks: 
        if block.blockShape == "cube": 
            for rowIter in range(block.row, (block.row + 2)):
                for colIter in range(block.column, (block.column + 2)): 
                    grid[rowIter][colIter] = 1
        elif block.blockShape == "i":
            print((block.row, block.column))
            # WIP. Need to resolve an error over here somewhere.
            for rowIter in range(block.row, (block.row + 4)):
                for colIter in range(block.column, (block.column + 1)):
                    grid[rowIter][colIter] = 1
            printGrid()



def renderBlocksForTesting(window): 
    global collapsedBlocks
    cubeBlock = Block()
    jBlock = Block()
    lBlock = Block()
    cubeBlock.shape = cubeBlock.gameWindow.loadImage("cube-block.png")
    cubeBlock.blockShape = "cube"
    cubeBlock.row = 21
    cubeBlock.column = 2
    cubeBlock.isFalling = False
    jBlock.shape = jBlock.gameWindow.loadImage("j-block.png")
    jBlock.blockShape = "j"
    jBlock.isFalling = False
    jBlock.row = 18
    jBlock.column = 5
    lBlock.shape = lBlock.gameWindow.loadImage("L-block.png")
    lBlock.blockShape = "L"
    lBlock.isFalling = False
    lBlock.row = 21
    lBlock.column = 6
    collapsedBlocks.append(cubeBlock)
    collapsedBlocks.append(jBlock)
    collapsedBlocks.append(lBlock)
    return collapsedBlocks


def checkForCollision(currentBlock, window): 
    global collapsedBlocks
    # if currentBlock.blockShape == "cube": 
    if currentBlock.checkCollisionForCube(collapsedBlocks, currentBlock):
        collapsedBlocks.append(currentBlock)
        updateGrid(collapsedBlocks)
        newBlock = spawnBlock(window)
        return newBlock
    else: 
        return currentBlock
    # elif currentBlock == ""

def renderCollapsedBlocks(window): 
    global collapsedBlocks
    if collapsedBlocks == []: 
        return
    else: 
        for block in collapsedBlocks: 
            block.renderUpdatedPosition(window)

def renderDownWardMotionForAllBlocks():
    global blocksOnScreen
    for block in blocksOnScreen:
        block.renderBlockDownwardMotion()

def getColumnUpperLimit(blockShape): 
    if blockShape == "cube-block": 
        return 13
    elif blockShape == "i": 
        return 11
    elif blockShape == "j" or blockShape == "s" or blockShape == "L" or blockShape == "t" or blockShape == "rs": 
        return 12

def spawnBlock(window): 
    global blocksOnScreen, possibleBlockShapes
    block = Block()
    blockShape = random.choice(possibleBlockShapes)
    columnUpperLimit = getColumnUpperLimit(blockShape)
    block.returnRandomBlockShape(blockShape, columnUpperLimit)
    block.generateBlock(window)
    blocksOnScreen.append(block)
    return block 

def generateBlock(window):
    global blocksOnScreen, collapsedBlocks
    if blocksOnScreen == []:
        block = spawnBlock(window)
        return block
    else:
        currentBlock = blocksOnScreen[len(blocksOnScreen) - 1]
        if currentBlock.blockShape == "i": 
            if currentBlock.row == 22:
                currentBlock.isFalling = False 
                collapsedBlocks.append(currentBlock)
                newBlock = spawnBlock(window)
                return newBlock
            else:
                return currentBlock
        else: 
            if currentBlock.row == 21:
                currentBlock.isFalling = False
                collapsedBlocks.append(currentBlock)
                newBlock = spawnBlock(window)
                return newBlock
            else: 
                return currentBlock

def gameLoop(): 
    global collapsedBlocks
    pygame.init()
    gameWindow = GameWindow()
    clock = pygame.time.Clock()
    window = gameWindow.setMode()
    gameWindow.setCaption("Tetris - Aditya Chaturvedi")
    # collapsedBlocks = renderBlocksForTesting(window)
    backGroundMusic = BackGroundMusic()
    backGroundMusic.playRandomMusic()
    gameStats = GameStats()
    
    while gameWindow.windowRunning: 
        gameWindow.renderGameBackground(window)
        gameWindow.renderGrid(window)
        gameWindow.renderScoreBoard(window)
        renderCollapsedBlocks(window)
        currentBlock = generateBlock(window)
        currentBlock.renderBlockDownwardMotion(window)
        currentBlock.renderUpdatedPosition(window)
        currentBlock = checkForCollision(currentBlock, window)
        clock.tick(8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameWindow.windowRunning = False
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    gameWindow.windowRunning = False
                if event.key == pygame.K_LEFT and currentBlock.column > 0: 
                    currentBlock.moveLeft()
                if event.key == pygame.K_RIGHT and currentBlock.column < 12: 
                    currentBlock.moveRight()
                if event.key == pygame.K_m: 
                        backGroundMusic.togglePauseUnPause()
                if event.key == pygame.K_p: 
                    if not gameStats.isPaused: 
                        gameStats.isPaused = True
                        gameStats.pauseGame()
                    else: 
                        gameStats.isPaused = False
                        gameStats.unpauseGame()

        pygame.display.update()
        clock.tick(60)