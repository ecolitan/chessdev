from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class PawnMoves(BoardRelations):
    """Calculate various pawn moves.
    """

    def PossibleSquares(self, square):
        """Returns a list of possible moves for a pawn to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #if pawn unmoved, can move one or two squares.
        if square[0] == 1 or square[0] == 6:
            unmoved = True
        
        #white pawns go to higher numbers, black pawns to lower
        if self.MapPiece(square) == 'P':
            if unmoved:
                pass
        
        
        
        #for each diagonal, look forwards one square. If enemy piece, include square.
        for diag in self.CalculateDiags(square):
            if diag:
                for square in diag:
                    if self.MapPiece(square) not in samecolour:
                        squares.append(square)
                    else:
                        break
        return squares
