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
        unmoved = False
        n,m = square
        
        #white pawns go to higher numbers, black pawns to lower
        if self.MapPiece(square) == 'P':
            if n=1:
                unmoved = True
            if self.MapPiece(n+1,m):
                squares.append(n+1,m)
                if unmoved:
                    if self.MapPiece(n+2,m):
                        squares.append(n+2,m)
            if m+1 != 8:
                if self.MapPiece(n+1,m+1) not in samecolour:
                    squares.append(n+1,m+1)
            if m-1 != -1:
                if self.MapPiece(n+1,m-1) not in samecolour:
                    squares.append(n+1,m-1)
            if self.epsquare:
                if (n+1,m-1) == self.epsquare or (n+1,m+1) == self.epsquare:
                    squares.append(self.epsquare)
                
        if self.MapPiece(square) == 'p':
            if n=6:
                unmoved = True
            if self.MapPiece(n-1,m):
                squares.append(n-1,m)
                if unmoved:
                    if self.MapPiece(n-2,m):
                        squares.append(n-2,m)
            if m+1 != 8:
                if self.MapPiece(n-1,m+1) not in samecolour:
                    squares.append(n-1,m+1)
            if m-1 != -1:
                if self.MapPiece(n-1,m-1) not in samecolour:
                    squares.append(n-1,m-1)
            if self.epsquare:
                if (n-1,m-1) == self.epsquare or (n-1,m+1) == self.epsquare:
                    squares.append(self.epsquare)

        return squares
