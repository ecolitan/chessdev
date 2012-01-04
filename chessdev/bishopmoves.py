from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class BishopMoves(BoardRelations):
    """Calculate various bishop moves.
    """
        
    def PossibleSquares(self, square):
        """Returns a list of possible moves for a bishop to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each diagonal, step along until edge or a piece is reached. If enemy piece, include square.
        for diag in self.CalculateDiags(square):
            if diag:
                for square in diag:
                    if self.MapPiece(square) not in samecolour:
                        squares.append(square)
                    else:
                        break
        return squares
                
