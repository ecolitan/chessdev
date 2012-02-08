import copy
from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class PreSearch():
    """Presearch methods."""
    
    def __init__(self):
        pass
    
    def GenerateBoard(self, boardobject, move, promoteto=None):
        """Returns legal BoardRelations object for a given move.
        If move is not Legal, return Error
        Return BoardRelations Object
        """
        def isOurPiece(move):
            """Check that piece being moved is ours.
            Return True or False
            """
            #TODO write isOurPiece method
            return True
            
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
            if boardobject.MapPiece(move[1]):
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
        
        def createBoardPosition(move, promoteto=None):
            """Create a new boardposition.
            Accept move tuple and optional promotion piece.
            return boardposition as list.
            """
            # Check if move is castling.
            if (isKingMove(move) and (move[0] in [(0,4),(7,4)] and move[1] in [(0,6),(7,6)])):
                movetype = 'castle'
                cside = 'k'
            elif (isKingMove(move) and (move[0] in [(0,4),(7,4)] and move[1] in [(0,2),(7,2)])):
                movetype = 'castle'
                cside = 'q'
            # Check if move is promotion.
            elif isPromotion(move):
                movetype = 'promotion'
                if promoteto is None:
                    if boardobject.sidetomove == 'w':
                        promoteto = 'Q'
                    if boardobject.sidetomove == 'b':
                        promoteto = 'q'
            # Otherwise its just a simple move.
            else:
                movetype = 'simple'
            
            # Copy the position
            #newboardposition = list(boardobject.position)
            newboardposition = copy.deepcopy(boardobject.position)

            # Update pieceplacement
            if movetype == "simple":
                newboardposition[0][move[0][0]][move[0][1]] = None
                newboardposition[0][move[1][0]][move[1][1]] = boardobject.MapPiece(move[0])
            if movetype == "castle":
                if cside == "k":
                    if boardobject.sidetomove == 'w':
                        #white kingside castle
                        newboardposition[0][0][4] = None
                        newboardposition[0][0][7] = None
                        newboardposition[0][0][5] = 'R'
                        newboardposition[0][0][6] = 'K'
                    if boardobject.sidetomove == 'b':
                        #black kingside castle
                        newboardposition[0][7][4] = None
                        newboardposition[0][7][7] = None
                        newboardposition[0][7][5] = 'R'
                        newboardposition[0][7][6] = 'K'
                if cside == "q":
                    if boardobject.sidetomove == 'w':
                        #white queenside castle
                        newboardposition[0][0][4] = None
                        newboardposition[0][0][0] = None
                        newboardposition[0][0][3] = 'R'
                        newboardposition[0][0][2] = 'K'
                    if boardobject.sidetomove == 'b':
                        #black queenside castle
                        newboardposition[0][7][4] = None
                        newboardposition[0][7][0] = None
                        newboardposition[0][7][3] = 'R'
                        newboardposition[0][7][2] = 'K'
            if movetype == "promotion":
                newboardposition[0][move[0][0]][move[0][1]] = None
                newboardposition[0][move[1][0]][move[1][1]] = promoteto
            
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
            
            return newboardposition
        
        if not isOurPiece(move):
            raise DeadlyError(None,"not side to move")
        
        # Generate the BoardRelations object
        newposition = createBoardPosition(move, promoteto)
        newobj = BoardRelations(newposition)
        return newobj
        
    def GenerateAllBoards(self, boardobject):
        """Generate a list of all legal BoardRelations objects for a given boardobject.
        Accepts BoardRelations object
        Returns List of BoardRelations objects
        """
        objectlist = []
        moveslist = boardobject.PossibleMoves()
        castlelist = boardobject.PossibleCastle()
        
        if castlelist[0] is True:
            if boardobject.sidetomove == 'w':
                moveslist.append(((0,4),(0,6)))
            if boardobject.sidetomove == 'b':
                moveslist.append(((7,4),(7,6)))
        if castlelist[1] is True:
            if boardobject.sidetomove == 'w':
                moveslist.append(((0,4),(0,2)))
            if boardobject.sidetomove == 'b':
                moveslist.append(((7,4),(7,2)))
                
        for move in moveslist:
            if self.GenerateBoard(boardobject, move).isPromotion(move):
                if boardobject.sidetomove == 'w':
                    promotions = whitepromotions
                if boardobject.sidetomove == 'b':
                    promotions = blackpromotions
                for promotionpiece in promotions:
                    _object = BoardRelations(self.GenerateBoard(boardobject,move,promotionpiece))
                    if _object.isLegal():
                        objectlist.append(_object)
            else:
                _object = BoardRelations(self.GenerateBoard(boardobject,move,promotionpiece))
                if _object.isLegal():
                    objectlist.append(_object)

        return objectlist
        
        
    def isMate(self, boardobject):
        """Returns True or False for if a position is a checkmate.
        If king in check AND
            every possible move creates a position where the king is still in check.
        Returns True or False.
        """
        if boardobject.sidetomove == 'w':
            kingsquare = boardobject.FindPieces('K')
        elif boardobject.sidetomove == 'b':
            kingsquare = boardobject.FindPieces('k')
        
        if not boardobject.isCheck(kingsquare, boardobject.sidetomove):
            return False
        
        for square in boardobject.KingSquares(kingsquare):
            if not isCheck(square, boardobject.sidetomove):
                return False
            #TODO finish isMate method

    def isStale(self):
        """Returns True or False for if a position is a stalemate.
        King is not in check AND
            if there are no legal moves
        Returns True or False."""
        return False
        #TODO finish isStale method
