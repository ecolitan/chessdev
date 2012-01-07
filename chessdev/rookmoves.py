from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class RookMoves(BoardRelations):
    """Calculate various rook moves.
    """
    
    def PossibleSquares(self, square):
        """Returns a list of possible moves for a rook to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each rank and file, step along until edge or a piece is reached. If enemy piece, include square.
        print square
        for rank in self.CalculateRanks(square):
            if rank:
                for i in rank:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        print square
        for file in self.CalculateFiles(square):
            if file:
                for i in file:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
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
