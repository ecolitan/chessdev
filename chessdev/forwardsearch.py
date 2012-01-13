from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class PreSearch():
    """Presearch methods."""
    
    def __init__(self):
        pass
    
    def GenerateBoards(self, boardobject):
        """Returns a List of boardobjects, showing all possible positions arising from a given boardobject.
        Many boardobjects created will have illegal position!
        Boardobjects created must be for:
            all possible moves
            after castling if possible
            after EP capture if possible
            after all possible promotions
        Important to update in position:
            EP Square created
            Castling rights changed
            increment or reset halfmoveclock
            increment fullmoves
            update sidetomove
        Return List
        
        self.position = position
        self.pieceplacement = position[0]
        self.sidetomove = position[1]
        self.castlingrights = position[2]
        self.epsquare = position[3]
        self.halfmoveclock = position[4]
        self.fullmoves = position[5]
        move ((0,0),(0,3)) 
        """
        objectlist = []
        moveslist = boardobject.PossibleMoves()
        castlelist = boardobject.PossibleCastle()
        
        def isPawnMove(move):
            """Check if a move is a pawn move.
            Return True or False.
            """
            if boardobject.MapPiece(move[0]) in ['P', 'p']:
                return True
            return False
            
        def isDoublePawnMove(move):
            """Check if a pawn is moving two squares.
            Needed to calculate EP Square.
            Move must already be a know pawn move.
            Return True or False.
            """
            pass
            
        def isCapture(move):
            """Check if a move is a capture."""
            pass
            
        def isPromotion(move):
            """Check if a move is a pawn promotion."""
            #check if destination square is first or last rank
            if move[1][0] not in [0, 7]:
                return False
            #check if pawn
            if boardobject.MapPiece(move[0]) not in ['P', 'p']:
                return False
            return True
        
        def createBoardPosition(move, movetype, promoteto=None):
            """Create a new boardposition.
            if movetype = "simple", move must be a move tuple.
            if movetype = "castle", move must be either "k" or "q" to denote the side.
            if movetype = "promotion", move must be a move tuple, and promoteto must be a Piece.
            """
            newboardposition = list(boardobject.position)
            # Update pieceplacement
            if movetype = "simple":
                newboardposition[0][move[0][0]][move[0][1]] = None
                newboardposition[0][move[1][0]][move[1][1]] = boardobject.MapPiece(move[0])
            
            # Update sidetomove
            if boardobject.sidetomove == 'w':
                newboardposition[1] = 'b'
            if boardobject.sidetomove == 'b':
                newboardposition[1] = 'w'
            
            # Update Castling Rights
            #if movetype == "castle" PUT inside pieceplacement update.
            
            # Update EP Square
            #if isDoublePawnMove; create EP Square behind pawn.
            
            # Update Halfmoveclock
            #if last move by pawn or capture, reset to 0
            #else increment by 1
            
            # Update fullmove
            #if now wtm; increment
            
        pass
    
    def isMate(self):
        """Returns True or False for if a position is a checkmate.
            if king in check AND
                every possible move creates a position where the king is still in check.
        Returns True or False.
        """
        if self.sidetomove == 'w':
            kingsquare = self.FindPieces('K')
        elif self.sidetomove == 'b':
            kingsquare = self.FindPieces('k')
        
        if not self.isCheck(kingsquare):
            return False
        
        for square in self.KingSquares(kingsquare):
            if not isCheck(square, self.sidetomove):
                return False      
            #TODO

    def isStale(self):
        """Returns True or False for if a position is a stalemate.
        King is not in check AND
            if there are no legal moves
        Returns True or False."""
        return False
        #TODO
