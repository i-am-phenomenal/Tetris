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
            print((block.row, block.column))
            block.renderUpdatedPosition(window)

def renderDownWardMotionForAllBlocks():
    global blocksOnScreen
    for block in blocksOnScreen:
        block.renderBlockDownwardMotion()

def renderDownwardMotion(currentBlock):
    global blocksOnScreen
    if currentBlock.yCoord < 525:
        currentBlock.renderBlockDownwardMotion()
    elif currentBlock.yCoord >= 525: 
        currentBlock.yCoord = 525
        
def spawnBlock(window): 
    global blocksOnScreen, possibleBlockShapes
    block = Block()
    blockShape = random.choice(possibleBlockShapes)
    block.returnRandomBlockShape(blockShape)
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
    collapsedBlocks = renderBlocksForTesting(window)
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