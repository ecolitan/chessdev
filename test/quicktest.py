from chessdev.boardrelations import BoardRelations
from chessdev.forwardsearch import PreSearch
from chessdev.basicwrapper import BasicWrapper, SimpleGame

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
            print i
            print test.MapPiece(i)
            print test.PossibleSquares(i)
            print test.PossibleCaptures(i)
                   
    def testwrapper(position):
        
        object1 = BoardRelations(position)
        print "object1: ",object1
        BasicWrapper().PrintBoard(object1)
        
        fullmove = BasicWrapper().InputMove()
        print fullmove
        
        object2 = PreSearch().GenerateBoard(object1, fullmove[0], fullmove[1])
        print "object2: ", object2
        BasicWrapper().PrintBoard(object2)
        
        fullmove2 = BasicWrapper().InputMove()
        print fullmove
        
        object3 = PreSearch().GenerateBoard(object2, fullmove2[0], fullmove2[1])
        BasicWrapper().PrintBoard(object3)
        
    #testpos1
    for position in [startBoard]:
        #testpiecemoves(position)
        #testwrapper(position)
        pass
    
    SimpleGame().CreateGame(startBoard)
