import pygame
import os 
import random
import math 
import time
from classes import GameWindow, BackGroundMusic

def gameLoop(): 
    pygame.init()
    gameWindow = GameWindow()
    window = gameWindow.setMode()
    backGroundMusic = BackGroundMusic()
    clock = pygame.time.Clock()

    gameWindow.renderGameBackground(window)
    gameWindow.renderGrid(window)
    gameWindow.renderScoreBoard(window)
    backGroundMusic.playRandomMusic()
    pygame.display.flip()

    while gameWindow.windowRunning: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameWindow.windowRunning = False
                sys.exit()
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    gameWindow.windowRunning = False
        pygame.display.update()
        clock.tick(60)