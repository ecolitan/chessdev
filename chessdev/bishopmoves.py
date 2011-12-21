from chessdev.data.data import *
from chessdev.customexceptions import *

class BishopMoves():
    """Calculate legal bishop moves.
    Accepts a BoardRelations object.
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
