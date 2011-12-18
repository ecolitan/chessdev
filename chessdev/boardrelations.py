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
    
    def RankSeparation(self, square1, square2):
        """Caclulates rank separation between two squares.
        If both squares on same rank, RankSeparation(n,m)=0
        Returns int"""
        return 0
    
    def FileSeparation(self, square1, square2):
        """Calculates file separation between two squares.
        Returns int"""
        return 0
        
    def CalcDistance(self, square1, square2):
        """Calculates distance between two squares.
        Distance is the greater from RankSeparation and FileSeparation. 
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
