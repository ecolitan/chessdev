from chessdev.data.data import *
from chessdev.customexceptions import *

class KnightMoves():
    """Calculate legal knight moves.
    Accepts a BoardRelations object.
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
