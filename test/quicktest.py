from chessdev.boardposition import BoardPosition
from chessdev.boardrelations import BoardRelations
from chessdev.kingmoves import KingMoves
from chessdev.data.data import *
from chessdev.data.examples import *

def quicktest():

        
    def testBoardRelations():
        """Tests for BoardRelations Objects."""
        emptytest = BoardRelations(emptyBoard[0])
        starttest = BoardRelations(startBoard[0])
        rooktest = BoardRelations(startBoardnorooks[0])
        return True
        
    # Tests for KingMoves 
    starttest = BoardPosition(startBoard)   # startposition
    test1 = BoardPosition(testpos1)         # no w queen
    test2 = BoardPosition(testpos2)         # king on e6 in check
    test3 = BoardPosition(testpos3)         # No white king
    test4 = BoardPosition(testpos4)         # No kings
    
    print KingMoves(starttest).kingsquare()
    print KingMoves(test1).kingsquare()
    print KingMoves(test2).kingsquare()
    print KingMoves(test3).kingsquare()
    
    testBoardRelations()
