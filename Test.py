import chess
from pieces import *
from board import *

obj = Bishop(False, 1)

obj1 = Tile(63)

newboard = Board()
newboard.createBoard()


print(obj.symbol())
print(obj1.tile_name)
print(obj1.tile_ofRowIndex)
print(obj1.tile_ofColumnIndex)
print(obj1.occupiedBy)

newboard.printBoard()
