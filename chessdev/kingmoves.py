from chessdev.data.data import *
from chessdev.customexceptions import *

class KingMoves:
    """Calculates legal King moves.
    Accepts a BoardRelations Object
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
        
    def KingSquare(self):
        """Returns the square of the king, for the side to move.
        Returns list
        """
        if self.sidetomove == 'w':
            return [piecesquare for piecesquare,x in enumerate(self.position.pieceplacement) if x == 'K']
        elif self.sidetomove == 'b':
            return [piecesquare for piecesquare,x in enumerate(self.position.pieceplacement) if x == 'k']
        else:
            raise PositionError(self.position, 'CantFindKing')
            
    def PossibleSquares(self, square):
        """Returns a list of possible squares for the king to move to.
        Doesn't worry about check, only that the square is not occupied by a piece of the same colour."""
        
        def ourpieces():
            if self.sidetomove == 'w':
                return whitepieces
            else:
                return blackpieces
        
        possiblesquares = []
        for i in boardpos:
            if self.position.TestAdjacent(square, i):
                if not self.position.MapPieces(i):
                    possiblesquares.append(i)
                elif self.position.MapPieces(i) not in ourpieces():
                    possiblesquares.append(i)
        return possiblesquares
        
    def movelist(self, position):
        """Returns a list of legal king moves."""
        return []
        
