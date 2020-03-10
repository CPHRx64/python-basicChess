import chess
from pieces import *


# Arrays
tile_names = chess.SQUARE_NAMES
columns = chess.FILE_NAMES
rows = chess.RANK_NAMES

class Board(chess.Board):
    # Fields
    gameTiles = {}

    # Constructor
    def __init__(self):
        pass

    # Functions
    def createBoard(self):
        for tile in range(64):
            empty = NullPiece(True, tile)
            self.gameTiles[tile] = Tile(tile)
            self.gameTiles[tile].getOccupied(empty)


    def printBoard(self):
        count = 0
        for tile in range (64):
            print('|', end=self.gameTiles[tile].occupiedBy.symbol())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0




###### help classes ######
class Move(chess.Move):
    from_square = None
    to_square = None
    promotion = None
    drop = None

    def __init__(self, from_square, to_square, promotion, drop):
        super()

    #uci()->str
    #from_uci(uci: str)->chess.Move
    #null()->chess.Move

class Tile():
    tile_index = None
    tile_name = None
    tile_ofRowIndex = None #rank
    tile_ofColumnIndex = None #file
    occupiedBy = None

    def __init__(self, index):
        self.tile_index = index
        self.tile_name = chess.SQUARE_NAMES[index]

        self.tile_ofRowIndex = chess.square_rank(index)
        self.tile_ofRowName = chess.square_rank(index)

        self.tile_ofColumnIndex = chess.square_file(index)

    def getOccupied(self, piece):
        self.occupiedBy = piece

    def tile_OfColumnName(self):
        return chess.FILE_NAMES[tile_ofColumnIndex]
