from collections import Counter
from chessdev.data.data import *
from chessdev.customexceptions import *

class BoardRelations:
    """The relationships between the elements of a board position.
    Accepts a BoardPosition.
    A single board position.
    Position format: ( [ 01, 02, ... , 63],                          # Piece placement or None,
                       'w' | 'b',                                    # Side to move.
                       [ 'K', 'Q', 'k', 'q' ],                       # Castling rights or None.
                       int,                                          # en passant square or None.
                       int,                                          # half move clock - since last pawn advance or capture.
                       int,                                          # fullmove number.
                    )
    """
    
    def __init__(self, position):
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
 
    def MapPieces(self, square):
        """Returns string of what stands on a square.
        Accepts an integer for the square name.
        """
        return self.pieceplacement[square]
    
    def MapList(self, inlist):
        """Returns List of with pieces for a given list."""
        outlist = []
        for square in inlist:
            outlist.append(self.MapPieces(square))
        return outlist
    
    def ShareDiag(self, square1, square2):
        """Tests if two squares share a diagonal.
        Returns True/False.
        """
        for diagdict in alldiagdict:
            if (diagdict[square1] == diagdict[square2]):
                return True
        return False
        
    def RankSeparation(self, square1, square2):
        """Caclulates rank separation between two squares.
        If both squares on same rank, RankSeparation(n,m)=0
        Returns int"""
        return abs(rankdict[square1] - rankdict[square2])
        
    def FileSeparation(self, square1, square2):
        """Calculates file separation between two squares.
        Returns int"""
        return abs(filedict[square1] - filedict[square2])
        
    def CalcDistance(self, square1, square2):
        """Calculates distance between two squares.
        Distance is the greater from RankSeparation and FileSeparation. 
        Returns int"""
        if (abs(filedict[square1] - filedict[square2]) >= abs(rankdict[square1] - rankdict[square2])):
            return abs(filedict[square1] - filedict[square2])
        else:
            return abs(rankdict[square1] - rankdict[square2])
        
    def TestAdjacent(self, square1, square2):
        """Tests if two squares are adjacent.
        Returns True/False.
        """
        if (self.CalcDistance(square1, square2) == 1):
            return True
        return False
    
    def ClearLine(self, square1, square2):
        """Tests if two squares on a line have any pieces between them.
        Returns True/False.
        """
        
        if square1 == square2:
            raise RelationError(square1, square2, 'SameSquare')
            return False
            
        if self.TestAdjacent(square1, square2):
            return True
            
        if square1 > square2:
            bigger = square1
            smaller = square2
        else:
            bigger = square2
            smaller = square1
            
        if self.RankSeparation(square1, square2) == 0:
            for rank in rankpos:
                if square1 in rank:
                    smalllist = rank[smaller+1:bigger]
            
        if self.FileSeparation(square1, square2) == 0:
            for file in filepos:
                if square1 in file:
                    smalllist = file[smaller+1:bigger]
            
        if self.ShareDiag(square1, square2):
            for diagpos in [whitediagpos, blackdiagpos]:
                for diag in diagpos:
                    if (square1 in diag and square2 in diag):
                        smalllist = diag[diag.index(smaller)+1:diag.index(bigger)]
        
        for i in smalllist:
            if self.MapPieces(i):
                return False
        
        if not (self.TestAdjacent(square1, square2) or
                self.RankSeparation(square1, square2) == 0 or
                self.FileSeparation(square1, square2) == 0 or
                self.ShareDiag(square1, square2)):
                    raise RelationError(square1, square2, 'NotSameLine')
                    return False
        
        return True

    def TestSameColour(self, square1, square2):
        """Tests if two squares are the same colour.
        if (rankseparation + filesepatation)/2 has 0 remainder, the squares are the same colour
        Returns True/False.
        """
        if (self.RankSeparation(square1, square2) + self.FileSeparation(square1, square2)) % 2 == 0:
            return True
        return False
        
    def CentralValue(self, square1):
        """Tests how central a square is.
        Return int
        """
        return centraldict[square]
        
