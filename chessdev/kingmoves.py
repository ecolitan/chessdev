from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class KingMoves(BoardRelations):
    """Calculates various King moves.
    """
            
    def PossibleSquares(self, square):
        """Returns a list of possible squares for a king to move to.
        Doesn't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each adjacent square no occupied by a friendly piece, include square
        for i in boardpos:
            if self.TestAdjacent(square, i):
                if not self.MapPiece(i) in samecolour:
                    squares.append(i)
        return squares
        
    def movelist(self, position):
        """Returns a list of legal king moves."""
        return []
        
