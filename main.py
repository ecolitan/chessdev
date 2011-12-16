#!/usr/bin/env python

from data import *
from collections import Counter

class BoardPosition:
    """A single board position.
    Position format: ( [ a1, b1, ... , h1, a2, ... , h8 ] ,          # Piece placement or None,
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
    
    def IsLegal(self):
        """Returns True|False for position legality."""
        return True

emptytest = BoardPosition(emptyBoard)
starttest = BoardPosition(startBoard)
rooktest = BoardPosition(startwithoutrooks)

print emptytest.MaterialCount()
print starttest.MaterialCount()
print rooktest.MaterialCount()
