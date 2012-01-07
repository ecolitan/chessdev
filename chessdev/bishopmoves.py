from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class BishopMoves(BoardRelations):
    """Calculate various bishop moves.
    """
        
    def PossibleSquares(self, square):
        """Returns a list of possible squares for a bishop to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List of squares.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each diagonal, step along until edge or a piece is reached. If enemy piece, include square.
        for diag in self.CalculateDiags(square):
            if diag:
                for i in diag:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        return squares
                
    def PossibleMoves(self, square):
        """Returns list of possible moves for a bishop on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self.square):
        """Returns list of possible captures for a bishop on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares
