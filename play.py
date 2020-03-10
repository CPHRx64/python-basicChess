from board import *
import ches

# game loop
chesssboard = Board()
chesssboard.createBoard()

gameEnds = False

while not gameEnds:

    userInput = input()
    move = chess.Move.from_uci(userInput)
    print(userInput)





#game quit function
def quitGame() :
    gameEnds = True
    pygame.quit() #quit pygame
    quit() #quit python
