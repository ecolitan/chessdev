from chessdev.boardrelations import BoardRelations

#from test2 import Test2

from chessdev.data.data import *

def quicktest():
    
    def testpiecemoves(position):
        test = BoardRelations(position)
        for i in boardpos:
            print i
            print test.MapPiece(i)
            print test.PossibleSquares(i)
            print test.PossibleCaptures(i)
            print
            
    for position in [testpos1]:
        testpiecemoves(position)
