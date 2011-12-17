#!/usr/bin/env python

from data import *
from collections import Counter
import sys

class BoardPosition:
    """A single board position.
    Position format: ( [ 01, 02, ... , 63],                          # Piece placement or None,
                       'w' | 'b',                                    # Side to move.
                       [ 'K', 'Q', 'k', 'q' ],                       # Castling rights or None.
                       int,                                          # en passant square or None.
                       int,                                          # half move clock - since last pawn advance or capture.
                       int,                                          # fullmove number.
                    )"""
                            
    def __init__(self,  position):
        self.position = position
        self.pieceplacement = position[0]
        self.sidetomove = position[1]
        self.castlingrights = position[2]
        self.epsquare = position[3]
        self.halfmoveclock = position[4]
        self.fullmoves = position[5]
    
    def MaterialCount(self):
        """Returns a tuple with a dictionary of the counts of each piece, and total number of pieces"""
        piececount = Counter()
        for piece in self.pieceplacement:
            if piece:
                piececount[piece] += 1
        piecetotal = sum(piececount.values())
        return ((dict(piececount),  piecetotal))

class BoardRelations:
    """The relationships between the elements of a board position.
    Accepts a pieceplacement list.
    """
    
    def __init__(self, pieceplacement):
        self.pieceplacement = pieceplacement
    
    def MapPieces(self, square):
        """Returns string of what stands on a square.
        Accepts an integer for the square name.
        """
        return self.pieceplacement[square]
    
    def MapRanks(self):
        """Returns List of lists for pieces on each Rank."""
        AllRanks = []
        for rank in rankpos:
            AllRanks.append(map(self.MapPieces, rank))
        return AllRanks
    
    def MapFiles(self):
        """Returns List of lists for pieces on each File."""
        AllFiles = []
        for file in filepos:
            AllFiles.append(map(self.MapPieces, file))
        return AllFiles
    
    def MapDiagonal(self):
        """Returns List with lists for pieces on each Diagonal."""
        AllDiagonals = []
        for diag in diagpos:
            AllDiagonals.append(map(self.MapPieces, diag))
    
    def ShareRank(self, square1, square2):
        """Tests if two squares share a rank.
        Returns True/False.
        """
        for rank in rankpos:
            if square1 in rank and square2 in rank:
                return True
        return False
        
    def ShareFile(self, square1, square2):
        """Tests if two squares share a file.
        Returns True/False.
        """
        for file in filepos:
            if (square1 and square2) in file:
                return True
        return False
    
    def ShareDiag(self, square1, square2):
        """Tests if two squares share a diagonal.
        Returns True/False.
        """
        for diag in diagpos:
            if (square1 and square2) in diag:
                return True
        return False
    
    def CalcDistance(self, square1, square2):
        """Calculates distance between two squares.
        Needs a definion! 
        Returns int"""
        return 0
        
    def TestAdjacent(self, square1, square2):
        """Tests if two squares are adjacent.
        Returns True/False.
        """
        # Adjacent is simply distance = 1
        return True
    
    def ClearLine(self, square1, square2):
        """Tests if two squares on a line have any pieces between them.
        Returns True/False.
        """
        return True

    def TestSameColour(self, square1, square2):
        """Tests if two squares are the same colour.
        Returns True/False.
        """
        return True






# Some testing, still need to learn how to test correctly.

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
    
#testBoardPosition()
testBoardRelations()
