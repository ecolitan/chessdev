from chessdev.boardrelations import BoardRelations

#from test2 import Test2

from chessdev.data.data import *

def quicktest():
    
    def testpiecemoves(position):
        test = BoardRelations(position)
        for i in boardpos:
            i
            test.MapPiece(i)
            test.PossibleSquares(i)
            test.PossibleCaptures(i)
            
    for position in [testpos1]:
        testpiecemoves(position)
