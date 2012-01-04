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
        #BishopSquares method
        print test.BishopSquares('w')
        print test.BishopSquares('b')
        #Basics
        print test.sidetomove
        print test.pieceplacement[0][2]
        # PossibleSquares method
        print
        print test.PossibleSquares((3,4))
                
    def testBoardRelations(position):
        # Test BoardRelations methods
        test = BoardRelations(position)
        # MaterialCount method
        print test.MaterialCount()
        # CalculateDiags method
        print test.CalculateDiags((3,4))

    
    for position in [testpos1]:
        testBishopMoves(position)
        testBoardRelations(position)
