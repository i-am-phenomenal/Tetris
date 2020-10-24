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
    print(len(blocksOnScreen))
    for block in blocksOnScreen:
        block.renderBlockDownwardMotion()
        # print(block.yCoord)

def renderDownwardMotion(currentBlock):
    global blocksOnScreen
    if currentBlock.yCoord < 525:
        currentBlock.renderBlockDownwardMotion()
    elif currentBlock.yCoord >= 525: 
        currentBlock.yCoord = 525
        

def generateBlock(window): 
    global blocksOnScreen
    block = Block()
    block.generateBlock(window)
    blocksOnScreen.append(block)
    return block

def gameLoop(): 
    pygame.init()
    gameWindow = GameWindow()
    clock = pygame.time.Clock()
    window = gameWindow.setMode()
    backGroundMusic = BackGroundMusic()
    backGroundMusic.playRandomMusic()

    while gameWindow.windowRunning: 
        renderCollapsedBlocks(window)
        currentBlock = generateBlock(window)
        renderDownwardMotion(currentBlock)
        clock.tick(8)
        gameWindow.renderGameBackground(window)
        gameWindow.renderGrid(window)
        gameWindow.renderScoreBoard(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameWindow.windowRunning = False
                sys.exit()
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    gameWindow.windowRunning = False
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)