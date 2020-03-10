import chess
from pieces import *
from board import *

obj = Bishop(False, 1)

obj1 = Tile(63)

newboard = Board()
newboard.createBoard()
newboard.printBoard()

#input:
move = Move(1,2)
newboard.makeMove(move)
print("move made")
newboard.printBoard()
