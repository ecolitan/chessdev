from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class BishopMoves(BoardRelations):
    """Calculate legal bishop moves.
    Accepts a BoardRelations object.
    """
        
    def BishopSquares(self, colour):
        """Returns a List of squares for the Bishops, for the given colour.
        Returns List or None
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
        Returns List
        """
        def ourpieces():
            if self.sidetomove == 'w':
                return whitepieces
            else:
                return blackpieces
            possiblesquares = []
            # two diagonals
            return None
        return self.CalculateDiags(square)
