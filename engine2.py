import pygame
import os 
import random
import math 
import time
from classes import GameWindow

def gameLoop(): 
    gameWindow = GameWindow()
    window = gameWindow.setMode()
    clock = pygame.time.Clock()
    pygame.init()
    
    grid = gameWindow.loadImage("grid.jpg")
    window.blit(grid, (0,0))
    pygame.display.flip()
    while gameWindow.windowRunning: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameWindow.windowRunning = False
        pygame.display.update()
        clock.tick(60)


gameLoop()      