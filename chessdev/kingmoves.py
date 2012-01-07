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
        
    def PossibleMoves(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self.square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares
