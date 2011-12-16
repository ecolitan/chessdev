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
        """Returns List of lists for each of Rank."""
        AllRanks = []
        for rank in rankpos:
            AllRanks.append(map(self.MapPieces, rank))
        return AllRanks
    
    def MapFiles(self):
        """Returns List with the lists for each File."""
        AllFiles = []
        for file in filepos:
            AllFiles.append(map(self.MapPieces, file))
        return AllFiles
    
    def MapDiagonal(self):
        """Returns List with lists of Diagonals."""
        AllDiagonals = []
        for diag in diagpos:
            AllDiagonals.append(map(self.MapPieces, diag))
    
    def ShareLine(self, square1, square2):
        """Tests if two squares share a rank, file or diagonal.
        Returns a List of three True/False: [rank,file,diag]
        """
        return [True,True,True]
    
    def TestAdjacent(self, square1, square2):
        """Tests if two squares are adjacent.
        Returns True/False.
        """
        return True
    
    def CalcDistance(self, square1, square2):
        """Calculates distance between two squares.
        Needs a definion! 
        Returns int"""
        return 0
    
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





emptytest = BoardPosition(emptyBoard)
starttest = BoardPosition(startBoard)
rooktest = BoardPosition(startwithoutrooks)

relation1 = BoardRelations(starttest.pieceplacement)

#print relation1.MapPieces(06)

def testrelations():
    print relation1.MapRanks()
    print
    for i in xrange(0, len(rankpos)):
        print relation1.MapRanks()[i]
    print
    for i in xrange(0, len(filepos)):
        print relation1.MapFiles()[i]
    print
    for i in xrange(0,len(diagpos)):
        print diagpos[i]
            
    
testrelations()
#print emptytest.MaterialCount()
#print starttest.MaterialCount()
#print rooktest.MaterialCount()
