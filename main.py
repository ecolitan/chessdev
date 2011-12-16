#!/usr/bin/env python

from data import *
from collections import Counter

class BoardPosition:
    """A single board position.
    Position format: ( [ a1, b1, ... , h1, a2, ... , h8 ] ,          # Piece placement or None,
                       [ w | b ],                                    # Side to move.
                       [ 'K', 'Q', 'k', 'q' ],                       # Castling rights or None.
                       int,                                          # en passant square ot None.
                       int,                                          # half move clock - since last pawn advance or capture.
                       int,                                          # fullmove number.
                    )"""
                            
    def __init__(self,  position):
        self.position = position
    
    def MaterialCount(self):
        """Returns a tuple with a dictionary of the counts of each piece, and total number of pieces"""
        piececount = Counter()
        for piece in self.position:
            piececount[piece] += 1
        piecetotal = (sum(piececount.values()) - 32)
        return (dict(piececount),  piecetotal)
    
    def IsLegal(self):
        """Tests if the Position is Legal."""
        return True

emptytest = BoardPosition(emptyBoard)
starttest = BoardPosition(startBoard)

print emptytest.MaterialCount()
print starttest.MaterialCount()
