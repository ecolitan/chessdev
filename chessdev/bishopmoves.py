from chessdev.data.data import *
from chessdev.customexceptions import *

class BishopMoves():
    """Calculate legal bishop moves.
    Accepts a BoardRelations object.
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
        
    def PossibleSquares(self, square):
        """Returns a list of possible moves for a bishop to move to.
        Returns List
        """
        def ourpieces():
            if self.sidetomove == 'w':
                return whitepieces
            else:
                return blackpieces
            
            possiblesquares = []
            
            return possiblesquares
        
