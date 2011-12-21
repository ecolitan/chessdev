from chessdev.data.data import *
from chessdev.customexceptions import *


class RookMoves():
    """Calculate legal rook moves.
    Accepts a BoardRelations object.
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
