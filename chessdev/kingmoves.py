from chessdev.data.data import *

class KingMoves:
    """Calculates legal King moves.
    Accepts a BoardRelations Object
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
            
    def PossibleSquares(self, square):
        """Returns a list of possible squares for the king to move to.
        Doesn't worry about check, only that the square is not occupied by a piece of the same colour."""
        for i in boardpos:
            pass
        return []
        
    def movelist(self, position):
        """Returns a list of legal king moves."""
        sidetomove = fullposition.sidetomove
        return []
        
