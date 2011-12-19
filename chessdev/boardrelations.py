from chessdev.data.data import *

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
    
    def ShareDiag(self, square1, square2):
        """Tests if two squares share a diagonal.
        Returns True/False.
        """
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
            raise RelationError('SameSquare')
            return False
            
        if self.TestAdjacent(square1, square2):
            return True
            
        if square1 > square2:
            bigger == square1
            smaller == square2
        else:
            bigger == square2
            smaller == square1
            
        if self.RankSeparation(square1, square2) == 0:
            for rank in rankpos:
                if square1 in rank:
                    smalllist = rank[smaller+1:bigger]
            
        if self.FileSeparation(square1, square2) == 0:
            for file in filepos:
                if square1 in file:
                    smalllist = file[smaller+1:bigger]
            
        if self.ShareDiag(square1, square2):
            for diag in diagpos:
                if square1 in diag:
                    smalllist = diag[smaller+1:bigger]
        
        for i in smalllist:
            if self.MapPieces(i):
                return False
        
        if not (self.TestAdjacent(square1, square2) or
                self.RankSeparation(square1, square2) == 0 or
                self.FileSeparation(square1, square2) == 0 or
                self.ShareDiag(square1, square2)):
                    raise RelationError('NotSameLine')
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
