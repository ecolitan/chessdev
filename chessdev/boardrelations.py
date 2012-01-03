from collections import Counter
from chessdev.data.data import *
from chessdev.customexceptions import *

class BoardRelations:
    """The relationships between the elements of a board position.
    Accepts a BoardPosition.
    A single board position.
    Position format: ( [[a1, b1, ... , h1],
                        [a2, b2, ... , h2],
                        ... ,
                        [a8, b8, ... , h8] ]                         # Piece placement or None,
                       'w' | 'b',                                    # Side to move.
                       ['K', 'Q', 'k', 'q'],                         # Castling rights or None.
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
        for square in boardpos:
            if self.MapPiece(square):
                piececount[self.MapPiece(square)] += 1
        piecetotal = sum(piececount.values())
        return ((dict(piececount),  piecetotal))
 
    def MapPiece(self, square):
        """Returns the piece standing on a square.
        Accepts tuple for the square position.
        Returns string or None
        """
        return self.pieceplacement[square[0]][square[1]]
        
    def CalculateDiags(self, square):
        """Calculates diagonals expanding outwards from a square.
        Accepts tuple for the square position.
        Returns List of 4 Lists
        
        There are 1,2,3 or 4 diagonals depending on where the square is.
        ([1],[2],[3],[4]) -> 
            1. Up and towards the right.
            2. Down and towards the right.
            3. Up and towards the left.
            4. Down and towards the left.
        Empty lists occur when the position in on a board edge.
        Index position 0 in each non-empty list is at distance 1 (adjacent).
        The following members are consequtively one further square away.
        """
        
        # Up and towards the right.
        def upright(square):
            n, m = square
            A = []
            def testend(a, b):
                if (a == 8 or b == 8):
                    return True
                return False
            while not testend(n, m):
                n += 1
                m += 1
                A.append((n,m))
            return A
            
        # Down and towards the right.
        def downright(square):
            n, m = square
            A = []
            def testend(a, b):
                if (a == 8 or b == 1):
                    return True
                return False
            while not testend(n, m):
                n += 1
                m -= 1
                A.append((n,m))
            return A
            
        # Up and towards the left.
        def upleft(square):
            n, m = square
            A = []
            def testend(a, b):
                if (a == 1 or b == 8):
                    return True
                return False
            while not testend(n, m):
                n -= 1
                m += 1
                A.append((n,m))
            return A
            
        # Down and towards the left.
        def downleft(square):
            n, m = square
            A = []
            def testend(a, b):
                if (a == 1 or b == 1):
                    return True
                return False
            while not testend(n, m):
                n -= 1
                m -= 1
                A.append((n,m))
            return A
        
        return [upright(square), downright(square), upleft(square), downleft(square)]
          
    def RankSeparation(self, square1, square2):
        """Caclulates rank separation between two squares.
        Accepts two square position Tuples.
        Returns int
        
        If both squares on same rank, RankSeparation=0
        """
        return abs(square1[1] - square2[1])
        
    def FileSeparation(self, square1, square2):
        """Calculates file separation between two squares.
        Accepts two square position Tuples.
        Returns int
        """
        return abs(square1[0] - square2[0])
        
    def CalcDistance(self, square1, square2):
        """Calculates distance between two squares.
        Distance is the greater from RankSeparation and FileSeparation. 
        Returns int"""
        if self.RankSeparation(square1, square2) >= self.FileSeparation(square1, square2):
            return self.RankSeparation(square1, square2)
        else:
            return self.FileSeparation(square1, square2)
        
    def TestAdjacent(self, square1, square2):
        """Tests if two squares are adjacent.
        Returns True/False.
        """
        if (self.CalcDistance(square1, square2) == 1):
            return True
        return False

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
        return centraldict[maparrayindex[square]]
        
