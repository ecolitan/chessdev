from chessdev.boardrelations import BoardRelations
from chessdev.forwardsearch import PreSearch

#from test2 import Test2

from chessdev.data.data import *

"""
        self.position = position
        self.pieceplacement = position[0]
        self.sidetomove = position[1]
        self.castlingrights = position[2]
        self.epsquare = position[3]
        self.halfmoveclock = position[4]
        self.fullmoves = position[5]"""
        
        
def quicktest():
    
    def testpiecemoves(position):
        test = BoardRelations(position)
        for i in boardpos:
            i
            test.MapPiece(i)
            test.PossibleSquares(i)
            test.PossibleCaptures(i)
            
    def testgeneratemoves(position):
        test = BoardRelations(position)
        
        #print test.PossibleMoves(), len(test.PossibleMoves())
        
        PreSearch().GenerateBoards(test)
        #for i in PreSearch().GenerateBoards(test):
        #    print i.sidetomove
            #print i.pieceplacement
            #print
        #print len(PreSearch().GenerateBoards(test))
            
    #testpos1
    for position in [startBoard]:
        #testpiecemoves(position)
        testgeneratemoves(position)
