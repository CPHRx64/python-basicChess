import pygame
from board import *



pygame.init()
gameDisplay = pygame.display.set_mode((400,400))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

chesssboard = Board()
chesssboard.createBoard()


gameEnds = False

while not gameEnds:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame()

    pygame.display.update()
    clock.init(60)



#game quit function
def quitGame() :
    gameEnds = True
    pygame.quit() #quit pygame
    quit() #quit python
