from chessdev.boardposition import BoardPosition
from chessdev.boardrelations import BoardRelations
from chessdev.data.data import *
from chessdev.data.examples import *

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


    
    testBoardPosition()
    testBoardRelations()
