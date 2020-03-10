import chess

# super class is chess.Piece from the chess lib
# att: color: True = upper-case else lower-case
# func: symbol() -> str

class NullPiece(chess.Piece):
    piece_type = 0
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position
    def symbol(self):
        return "."

class Bishop(chess.Piece):
    piece_type = chess.BISHOP
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position


class King(chess.Piece):
    piece_type = chess.KING
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position


class Knight(chess.Piece):
    piece_type = chess.KNIGHT
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position


class Pawn(chess.Piece):
    piece_type = chess.PAWN
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position


class Queen(chess.Piece):
    piece_type = chess.QUEEN
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position


class Rook(chess.Piece):
    piece_type = chess.ROOK
    position = -1

    def __init__(self, color, position):
        self.color = color
        self.position = position
