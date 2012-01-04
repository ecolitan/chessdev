from chessdev.boardrelations import BoardRelations
from chessdev.kingmoves import KingMoves
from chessdev.rookmoves import RookMoves
from chessdev.bishopmoves import BishopMoves
import chessdev.bishopmoves

#from test2 import Test2

from chessdev.data.data import *

def quicktest():
    
    def testBishopMoves(position):
        #Test BishopMoves Methods
        test = BishopMoves(position)
        #FindPieces method
        print test.FindPieces('B')
        print test.FindPieces('n')
        #Basics
        print test.sidetomove
        print test.pieceplacement[0][2]
        # PossibleSquares method
        print
        print test.PossibleSquares(test.FindPieces('B')[0])
                
    def testBoardRelations(position):
        # Test BoardRelations methods
        test = BoardRelations(position)
        # MaterialCount method
        print test.MaterialCount()
        # CalculateDiags method
        print test.CalculateDiags((3,4))
        
    def testKingMoves(position):
        test = KingMoves(position)
        print test.FindPieces('K')
        print test.PossibleSquares(test.FindPieces('K')[0])
        
    def testRookMoves(position):
        test = RookMoves(position)
        print test.FindPieces('R')
        print
        print test.PossibleSquares(test.FindPieces('R')[1])
        

    for position in [testpos1]:
        testBishopMoves(position)
        testBoardRelations(position)
        testKingMoves(position)
        testRookMoves(position)
