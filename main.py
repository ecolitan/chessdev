#!/usr/bin/env python

from data import *
from collections import Counter

class BoardPosition:
    """A single board position.
    Position format: ( [ a1, b1, ... , h1, a2, ... , h8 ],           # Piece placement or None,
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
        """Returns tuplet with lists for each of a Rank."""
        Rank1, Rank2, Rank3, Rank4, Rank5, Rank6, Rank7, Rank8 = ([], [], [], [], [], [], [], [])
        for i in rank1pos:
            Rank1.append(self.pieceplacement[i])
        for i in rank2pos:
            Rank2.append(self.pieceplacement[i])
        for i in rank3pos:
            Rank3.append(self.pieceplacement[i])
        for i in rank4pos:
            Rank4.append(self.pieceplacement[i])
        for i in rank5pos:
            Rank5.append(self.pieceplacement[i])
        for i in rank6pos:
            Rank6.append(self.pieceplacement[i])
        for i in rank7pos:
            Rank7.append(self.pieceplacement[i])
        for i in rank8pos:
            Rank8.append(self.pieceplacement[i])
                        
        return (Rank1, Rank2, Rank3, Rank4, Rank5, Rank6, Rank7, Rank8)
    
    def MapFiles(self):
        """Returns tuplet with the lists for each File."""
        return True

emptytest = BoardPosition(emptyBoard)
starttest = BoardPosition(startBoard)
rooktest = BoardPosition(startwithoutrooks)

relation1 = BoardRelations(starttest.pieceplacement)

print relation1.MapPieces(06)
print relation1.MapRanks()[7]

#print emptytest.MaterialCount()
#print starttest.MaterialCount()
#print rooktest.MaterialCount()
