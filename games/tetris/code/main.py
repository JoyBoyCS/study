import pygame, sys,os
from pygame.locals import *
from block import *
from const import *
import random

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))


blocks = []
for i in range(GAME_ROW):
    b = []
    for j in range(GAME_COL):
        b.append( Block(random.randint(0,BlockType.BLOCKMAX-1), i, j, 32, 32, (240, 50)) )
    blocks.append(b)
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    for i in range(GAME_ROW):
        for j in range(GAME_COL):
            blocks[i][j].update()
            
    DISPLAYSURF.fill((0,0,0))
    
    for i in range(GAME_ROW):
        for j in range(GAME_COL):
            blocks[i][j].draw(DISPLAYSURF)
  
    pygame.display.update()
