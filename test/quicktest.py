from chessdev.boardposition import BoardPosition
from chessdev.boardrelations import BoardRelations
from chessdev.data.data import *


def quicktest():
    def testBoardPosition():
        """Tests for BoardPosition Objects."""
        emptytest = BoardPosition(emptyBoard)
        starttest = BoardPosition(startBoard)
        rooktest = BoardPosition(startBoardnorooks)
        
        print emptytest.MaterialCount()
        print starttest.MaterialCount()
        print rooktest.MaterialCount()
        return True
        
    def testBoardRelations():
        """Tests for BoardRelations Objects."""
        emptytest = BoardRelations(emptyBoard[0])
        starttest = BoardRelations(startBoard[0])
        rooktest = BoardRelations(startBoardnorooks[0])

        #print starttest.MapPieces(06)
        
        #print starttest.MapRanks()
        #print
        #for i in xrange(0, len(rankpos)):
            #print starttest.MapRanks()[i]
        #print
        #for i in xrange(0, len(filepos)):
            #print starttest.MapFiles()[i]
        #print
        #for i in xrange(0,len(diagpos)):
            #print diagpos[i]
        
        print "  test if 8 15 share rank: True"
        print starttest.ShareRank(8,15)     #true
        print "  test 17 35 share rank: False"
        print starttest.ShareRank(17,35)    #false
    
    testBoardPosition()
    testBoardRelations()
