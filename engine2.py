import pygame
import os 
import random
import math 
import time
from classes import GameWindow, BackGroundMusic, Block

blocksOnScreen = []
collapsedBlocks = []

def renderCollapsedBlocks(window): 
    global collapsedBlocks
    if collapsedBlocks == []: 
        return
    else: 
        for block in collapsedBlocks: 
            window.blit(block, (block.xCoord, block.yCoord))

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
    global blocksOnScreen
    block = Block()
    block.generateBlock(window)
    blocksOnScreen.append(block)
    return block 

def generateBlock(window):
    global blocksOnScreen
    if blocksOnScreen == []:
        block = spawnBlock(window)
        return block
    else:
        currentBlock = blocksOnScreen[len(blocksOnScreen) - 1]
        if currentBlock.row == 24:
            currentBlock.isFalling = False
            newBlock = spawnBlock(window)
            return newBlock
        else: 
            return currentBlock

def gameLoop(): 
    pygame.init()
    gameWindow = GameWindow()
    clock = pygame.time.Clock()
    window = gameWindow.setMode()
    backGroundMusic = BackGroundMusic()
    backGroundMusic.playRandomMusic()
    gameWindow.renderGameBackground(window)
    gameWindow.renderGrid(window)
    while gameWindow.windowRunning: 
        renderCollapsedBlocks(window)
        currentBlock = generateBlock(window)
        currentBlock.renderBlockDownwardMotion()
        currentBlock.renderUpdatedPosition(window)
        # clock.tick(8)
        gameWindow.renderScoreBoard(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameWindow.windowRunning = False
                sys.exit()
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    gameWindow.windowRunning = False
        # pygame.display.update()
        # pygame.display.flip()
        # clock.tick(60)