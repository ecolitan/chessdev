from chessdev.boardrelations import BoardRelations
from chessdev.kingmoves import KingMoves
from chessdev.rookmoves import RookMoves
from chessdev.data.data import *
from chessdev.data.examples import *

def quicktest():
        
    # Testpositions objects 
    starttest = BoardRelations(startBoard)   # startposition
    test1 = BoardRelations(testpos1)         # no w queen
    test2 = BoardRelations(testpos2)         # king on e6 in check
    test3 = BoardRelations(testpos3)         # No white king
    test4 = BoardRelations(testpos4)         # No kings
    test5 = BoardRelations(testpos5)         # King on a3
    
    for boardrelations_object in [starttest, test1, test2, test5]:
    #for boardrelations_object in [starttest, test1, test2, test3, test4, test5]:
        
    #tests for kingmoves
    
        #test KingSquare method
        print KingMoves(boardrelations_object).KingSquare()
        #test PossibleSquares method
        print KingMoves(boardrelations_object).PossibleSquares(KingMoves(boardrelations_object).KingSquare())
    
    # Tests for RookMoves
        print RookMoves(starttest).sidetomove
    
