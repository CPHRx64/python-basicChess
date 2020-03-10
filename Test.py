import chess
from pieces import *
from board import *

obj = Bishop(False, 1)

obj1 = Tile(63)

newboard = Board()
newboard.createBoard()

while True:
    newboard.printBoard()
    print(" ")
    print("from: ")
    moveFrom = input()
    print("to: ")
    moveTo = input()
    print(" ")
    move = Move(int(moveFrom), int(moveTo))
    print("move made from " + str(move.from_tile) + " to " + str(move.to_tile))
    
    newboard.makeMove(move)
