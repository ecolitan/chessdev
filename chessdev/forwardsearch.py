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
            
        def isKingMove(move):
            """Check if a move is a king move.
            Return True or False.
            """
            if boardobject.MapPiece(move[0]) in ['K', 'k']:
                return True
            return False
            
        def isDoublePawnMove(move):
            """Check if a pawn is moving two squares.
            Needed to calculate EP Square.
            Return True or False.
            """
            if boardobject.MapPiece(move[0]) in ['P', 'p']:
                if (move[0][0] in [1, 6]) and (move[1][0] in [2, 5]):
                    return True
            return False
            
        def isCapture(move):
            """Check if a move is a capture."""
            if boardobject.MapPiece(move[1]) not None:
                return True
            return False
            
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
            if boardobject.sidetomove == 'w':
                if movetype == "castle":
                    newboardposition[2][0] = False
                    newboardposition[2][1] = False
                elif isKingMove(move):
                    newboardposition[2][0] = False
                    newboardposition[2][1] = False
                elif move[0] == (0, 0) or move[1] == (0, 0):
                    newboardposition[2][1] = False
                elif move[0] == (0, 7) or move[1] == (0, 7):
                    newboardposition[2][0] = False
            if boardobject.sidetomove == 'b':
                if movetype == "castle":
                    newboardposition[2][2] = False
                    newboardposition[2][3] = False
                elif isKingMove(move):
                    newboardposition[2][2] = False
                    newboardposition[2][3] = False
                elif move[0] == (7, 0) or move[1] == (7, 0):
                    newboardposition[2][3] = False
                elif move[0] == (7, 7) or move[1] == (7, 7):
                    newboardposition[2][2] = False   
            
            # Update EP Square
            if isDoublePawnMove(move):
                newboardposition[3] = ((move[0][0])+(move[1][0]))/2
            else:
                newboardposition[3] = None
            
            # Update Halfmoveclock
            if isPawnMove(move):
                newboardposition[4] = 0
            elif isCapture(move):
                newboardposition[4] = 0
            else:
                newboardposition[4] += 1
            
            # Update fullmove
            if boardobject.sidetomove == 'b':
                newboardposition[5] += 1
            
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
