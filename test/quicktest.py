from chessdev.boardrelations import BoardRelations
from chessdev.kingmoves import KingMoves
from chessdev.data.data import *
from chessdev.data.examples import *

def quicktest():
        
    # Tests for KingMoves 
    starttest = BoardRelations(startBoard)   # startposition
    test1 = BoardRelations(testpos1)         # no w queen
    test2 = BoardRelations(testpos2)         # king on e6 in check
    test3 = BoardRelations(testpos3)         # No white king
    test4 = BoardRelations(testpos4)         # No kings
    
    print KingMoves(starttest).kingsquare()
    print KingMoves(test1).kingsquare()
    print KingMoves(test2).kingsquare()
    print KingMoves(test3).kingsquare()
    

