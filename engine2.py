import pygame
import os 
import random
import math 
import time
from classes import GameWindow, BackGroundMusic, Block

blocksOnScreen = []

def generateBlock(window): 
    global blocksOnScreen
    block = Block()
    # block.updateBlockYCoordCounter()
    block.renderBlockDownwardMotion()
    # print("Y -> ", block.yCoord)
    blocksOnScreen.append(block.generateBlock(window))

def gameLoop(): 
    pygame.init()
    gameWindow = GameWindow()
    window = gameWindow.setMode()
    backGroundMusic = BackGroundMusic()
    backGroundMusic.playRandomMusic()

    while gameWindow.windowRunning: 
        generateBlock(window)
        clock = pygame.time.Clock()
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