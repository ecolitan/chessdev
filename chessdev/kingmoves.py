from chessdev.data.data import *
from chessdev import *

class KingMoves:
    """Calculates legal King moves.
    Accepts a BoardPosition Object
    """
    
    def __init__(self, position):
        self.position = position
        
    def kingsquare(self):
        """Returns the square of the king, for the side to move.
        Returns int
        """
        sidetomove = self.position.sidetomove
        if sidetomove == 'w':
            for i in [kingsquare for kingsquare,x in enumerate(self.position.pieceplacement) if x == 'K']:
                return i
        elif sidetomove == 'b':
            for i in [kingsquare for kingsquare,x in enumerate(self.position.pieceplacement) if x == 'k']:
                return i
        else:
            raise PositionError('CantFindKing')
            
    def movelist(self, position):
        """Returns a list of legal king moves."""
        sidetomove = fullposition.sidetomove
        
        
