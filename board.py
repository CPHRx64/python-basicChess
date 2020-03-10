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
            empty = NullPiece(False, tile)
            self.gameTiles[tile] = Tile(tile)
            self.gameTiles[tile].getOccupied(empty)
        self.initPosition()

    def printBoard(self):
        count = 0
        for tile in range (64):
            print('|', end=self.gameTiles[tile].occupiedBy.symbol())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0

    def initPosition(self):
        self.gameTiles[0].getOccupied(Rook(False,0))
        self.gameTiles[1].getOccupied(Knight(False,1))
        self.gameTiles[2].getOccupied(Bishop(False,2))
        self.gameTiles[3].getOccupied(Queen(False,3))
        self.gameTiles[4].getOccupied(King(False,4))
        self.gameTiles[5].getOccupied(Bishop(False,5))
        self.gameTiles[6].getOccupied(Knight(False,6))
        self.gameTiles[7].getOccupied(Rook(False,7))
        self.gameTiles[8].getOccupied(Pawn(False,8))
        self.gameTiles[9].getOccupied(Pawn(False,9))
        self.gameTiles[10].getOccupied(Pawn(False,10))
        self.gameTiles[11].getOccupied(Pawn(False,11))
        self.gameTiles[12].getOccupied(Pawn(False,12))
        self.gameTiles[13].getOccupied(Pawn(False,13))
        self.gameTiles[14].getOccupied(Pawn(False,14))
        self.gameTiles[15].getOccupied(Pawn(False,15))

        self.gameTiles[48].getOccupied(Pawn(True,48))
        self.gameTiles[49].getOccupied(Pawn(True,49))
        self.gameTiles[50].getOccupied(Pawn(True,50))
        self.gameTiles[51].getOccupied(Pawn(True,51))
        self.gameTiles[52].getOccupied(Pawn(True,52))
        self.gameTiles[53].getOccupied(Pawn(True,53))
        self.gameTiles[54].getOccupied(Pawn(True,54))
        self.gameTiles[55].getOccupied(Pawn(True,55))
        self.gameTiles[56].getOccupied(Rook(True,56))
        self.gameTiles[57].getOccupied(Knight(True,57))
        self.gameTiles[58].getOccupied(Bishop(True,58))
        self.gameTiles[59].getOccupied(Queen(True,59))
        self.gameTiles[60].getOccupied(King(True,60))
        self.gameTiles[61].getOccupied(Bishop(True,61))
        self.gameTiles[62].getOccupied(Knight(True,62))
        self.gameTiles[63].getOccupied(Rook(True,63))

    def makeMove(self, move):
        validMove = True
        from_tile = move.from_tile
        to_tile = move.to_tile

        if validMove:
            currentPiece = self.gameTiles[from_tile].occupiedBy
            self.gameTiles[to_tile].getOccupied(currentPiece)
            self.gameTiles[from_tile].getOccupied(NullPiece(True,1))




###### help classes ######
class Move():
    from_tile = None
    to_tile= None


    def __init__(self, from_tile, to_tile):
        self.from_tile = from_tile
        self.to_tile = to_tile

    def isValid():
        pass
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
