from chessdev.data.data import *

class KingMoves:
    """Calculates legal King moves.
    Accepts a BoardRelations Object
    """
    
    def __init__(self, position):
        self.position = position
        self.sidetomove = position.sidetomove
        
    def KingSquare(self):
        """Returns the square of the king, for the side to move.
        Returns int
        """
        
        if self.sidetomove == 'w':
            for i in [kingsquare for kingsquare,x in enumerate(self.position.pieceplacement) if x == 'K']:
                return i
        elif self.sidetomove == 'b':
            for i in [kingsquare for kingsquare,x in enumerate(self.position.pieceplacement) if x == 'k']:
                return i
        else:
            raise PositionError('CantFindKing')
            
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
        
