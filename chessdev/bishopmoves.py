from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class BishopMoves(BoardRelations):
    """Calculate various bishop moves.
    """
        
    def BishopSquares(self, colour):
        """Returns a List of squares for the Bishops, for the given colour.
        Accepts colour String.
        Returns List or None.
        """
        squares = []
        if colour == 'w':
            for i in boardpos:
                if self.MapPiece(i) == 'B':
                    squares.append(i)
        elif colour == 'b':
            for i in boardpos:
                if self.MapPiece(i) == 'b':
                    squares.append(i)
        else:
            squares = None
        return squares
        
    def PossibleSquares(self, square):
        """Returns a list of possible moves for a bishop to move to.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        # Colour of bishop
        if self.MapPiece(square) in whitepieces:
            samecolour = whitepieces
        elif self.MapPiece(square) in blackpieces:
            samecolour = blackpieces
        else:
            raise PositionError(self.position, 'BishopNotFound')
        
        #for each diagonal, step along until edge or a piece is reached. If enemy piece, include square.
        for diag in self.CalculateDiags(square):
            if diag:
                for square in diag:
                    if not self.MapPiece(square):
                        squares.append(square)
                    elif self.MapPiece(square) not in samecolour:
                        squares.append(square)
                    else:
                        break
        return squares
                
