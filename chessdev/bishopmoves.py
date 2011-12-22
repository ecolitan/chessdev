from chessdev.data.data import *
from chessdev.customexceptions import *

class BishopMoves():
    """Calculate legal bishop moves.
    Accepts a BoardRelations object.
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
        
    def BishopSquare(self):
        """Returns a List of squares for the Bishops, for the side to move.
        Returns list
        """
        if self.sidetomove == 'w':
            return [piecesquare for piecesquare,x in enumerate(self.position.pieceplacement) if x == 'B']
        elif self.sidetomove == 'b':
            return [piecesquare for piecesquare,x in enumerate(self.position.pieceplacement) if x == 'b']
        else:
            raise PositionError(self.position, 'CantFindBishops')
            
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
            # two diagonals
            return None
