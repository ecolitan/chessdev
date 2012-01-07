from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class KnightMoves(BoardRelations):
    """Calculate various knight moves.
    """

    def PossibleSquares(self, square):
        """Returns a list of possible moves for a knight to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)

        #squares at distance=2
        for i in boardpos:
            if self.CalcDistance(square, i) == 2:
                if self.MapPiece(i) not in samecolour:
                    squares.append(i)
        
        #for each rank, file and diagonal, remove the second entry if exists (index 1).
        for rank in self.CalculateRanks(square):
            if len(rank) >= 1:
                squares.remove(rank[1])
                
        for file in self.CalculateFiles(square):
            if len(file) >= 1:
                squares.remove(file[1])

        for diag in self.CalculateDiags(square):
            if len(diag) >= 1:
                squares.remove(diag[1])
                
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
