from collections import Counter
from chessdev.data.data import *
from chessdev.customexceptions import *

class BoardRelations:
    """The relationships between the elements of a board position.
    Accepts a board position List.
    A single board position:
    Position format: [ [[a1, b1, ... , h1],
                        [a2, b2, ... , h2],
                        ... ,
                        [a8, b8, ... , h8] ]                         # Piece placement or None,
                       'w' | 'b',                                    # Side to move.
                       ['K', 'Q', 'k', 'q'],                         # Castling rights True or False.
                       (n,m),                                        # en passant square or None.
                       int,                                          # half move clock - since last pawn advance or capture.
                       int,                                          # fullmove number.
                    ]
    This object is called a boardobject once created,
    it has all the methods needed to find out all possible
    things to do with a particular board position.
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
        """Returns a tuple with a dictionary of the counts of each piece, and total number of pieces."""
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
        [[1],[2],[3],[4]] -> 
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
                if (a == 7 or b == 7):
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
                if (a == 7 or b == 0):
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
                if (a == 0 or b == 7):
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
                if (a == 0 or b == 0):
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
        #broken
        """Tests if two squares are the same colour.
        if (rankseparation + filesepatation)/2 has 0 remainder, the squares are the same colour
        Returns True/False.
        """
        if (self.RankSeparation(square1, square2) + self.FileSeparation(square1, square2)) % 2 == 0:
            return True
        return False
        
    def CentralValue(self, square1):
        #broken
        """Tests how central a square is.#broken
        Return int
        """
        return centraldict[maparrayindex[square]]
        
    def FindPieces(self, piece):
        """Returns a List of squares for the piece given, Colour sensitive.
        Accepts piece String.
        Returns List.
        """
        squares = []
        for i in boardpos:
            if self.MapPiece(i) == piece:
                squares.append(i)
        return squares
        
    def PieceColour(self, square):
        """Returns the List of pieces, the same colour as the piece on a given square.
        Accepts square position Tuple.
        Returns List.
        """
        if self.MapPiece(square) in whitepieces:
            return whitepieces
        elif self.MapPiece(square) in blackpieces:
            return blackpieces
        else:
            raise PositionError(self.position, 'NoPieceFound')
    
    def CalculateFiles(self, square):
        """Calculates files expanding outwards from a square.
        Accepts tuple for the square position.
        Returns List of 2 Lists
        
        There are 1,2 ranks depending on where the square is.
        [[1],[2]] -> 
            1. Towards the top.
            2. Towards the bottom.
        Empty lists occur when the position in on a board edge.
        Index position 0 in each non-empty list is at distance 1 (adjacent).
        The following members are consequtively one further square away.
        """            
        #import pdb; pdb.set_trace()
        def totop(square):
            n,m = square
            A = []
            while not n >= 7:
                n += 1
                A.append((n,m))
            return A
        
        def tobottom(square):
            n,m = square
            A = []
            while not n <= 0:
                n -= 1
                A.append((n,m))
            return A
        
        return [totop(square), tobottom(square)]
    
    def CalculateRanks(self, square):
        """Calculates ranks expanding outwards from a square.
        Accepts tuple for the square position.
        Returns List of 2 Lists
        
        There are 1,2 ranks depending on where the square is.
        [[1],[2]] -> 
            1. Towards the right.
            2. Towards the left.
        Empty lists occur when the position in on a board edge.
        Index position 0 in each non-empty list is at distance 1 (adjacent).
        The following members are consequtively one further square away.
        """
        #import pdb; pdb.set_trace()
        def toright(square):
            n,m = square
            A = []
            while not m >= 7:
                m += 1
                A.append((n,m))
            return A
        
        def toleft(square):
            n,m = square
            A = []
            while not m <= 0:
                m -= 1
                A.append((n,m))
            return A
        
        return [toright(square), toleft(square)]
        
    def BishopSquares(self, square):
        """Returns a list of possible squares for a bishop to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List of squares.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each diagonal, step along until edge or a piece is reached. If enemy piece, include square.
        for diag in self.CalculateDiags(square):
            if diag:
                for i in diag:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        return squares
        
    def KingSquares(self, square):
        """Returns a list of possible squares for a king to move to.
        Doesn't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each adjacent square no occupied by a friendly piece, include square
        for i in boardpos:
            if self.TestAdjacent(square, i):
                if not self.MapPiece(i) in samecolour:
                    squares.append(i)
        return squares
        
    def KnightSquares(self, square):
        """Returns a list of possible moves for a knight to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)

        #squares at distance=2
        for i in boardpos:
            if self.CalcDistance(square, i) == 2:
                if self.MapPiece(i) not in samecolour:
                    squares.append(i)
        
        #for each rank, file and diagonal, remove the second entry if exists (index 1).
        for rank in self.CalculateRanks(square):
            if len(rank) >= 2:
                if rank[1] in squares:
                    squares.remove(rank[1])
                
        for file in self.CalculateFiles(square):
            if len(file) >= 2:
                if file[1] in squares:
                    squares.remove(file[1])

        for diag in self.CalculateDiags(square):
            if len(diag) >= 2:
                if diag[1] in squares:
                    squares.remove(diag[1])
                
        return squares
        
    def PawnSquares(self, square):
        """Returns a list of possible moves for a pawn to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        #import pdb; pdb.set_trace()
        squares = []
        samecolour = self.PieceColour(square)
        unmoved = False
        n,m = square

        #white pawns go to higher numbers, black pawns to lower
        if self.MapPiece(square) == 'P':
            if n == 1:
                unmoved = True
            # Straight pawn push
            if self.MapPiece((n+1,m)) is None:
                squares.append((n+1,m))
                if unmoved is True:
                    if self.MapPiece((n+2,m)) is None:
                        squares.append((n+2,m))
            # Pawn Captures
            if m+1 != 8:
                if (self.MapPiece((n+1,m+1)) not in samecolour and self.MapPiece((n+1,m+1)) is not None):
                    squares.append((n+1,m+1))
            if m-1 != -1:
                if (self.MapPiece((n+1,m-1)) not in samecolour and self.MapPiece((n+1,m-1)) is not None):
                    squares.append((n+1,m-1))
            if self.epsquare:
                if (n+1,m-1) == self.epsquare or (n+1,m+1) == self.epsquare:
                    squares.append(self.epsquare)
                
        if self.MapPiece(square) == 'p':
            if n == 6:
                unmoved = True
            if self.MapPiece((n-1,m)) is not None:
                squares.append((n-1,m))
                if unmoved:
                    if self.MapPiece((n-2,m)) is not None:
                        squares.append((n-2,m))
            if m+1 != 8:
                if self.MapPiece((n-1,m+1)) not in samecolour:
                    squares.append((n-1,m+1))
            if m-1 != -1:
                if self.MapPiece((n-1,m-1)) not in samecolour:
                    squares.append((n-1,m-1))
            if self.epsquare:
                if (n-1,m-1) == self.epsquare or (n-1,m+1) == self.epsquare:
                    squares.append(self.epsquare)

        return squares
        
    def QueenSquares(self, square):
        """Returns a list of possible moves for a queen to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each rank and file, step along until edge or a piece is reached. If enemy piece, include square.
        for rank in self.CalculateRanks(square):
            if rank:
                for i in rank:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        for file in self.CalculateFiles(square):
            if file:
                for i in file:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break

        #for each diagonal, step along until edge or a piece is reached. If enemy piece, include square.
        for diag in self.CalculateDiags(square):
            if diag:
                for i in diag:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        return squares
        
    def RookSquares(self, square):
        """Returns a list of possible moves for a rook to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each rank and file, step along until edge or a piece is reached. If enemy piece, include square.
        for rank in self.CalculateRanks(square):
            if rank:
                for i in rank:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        for file in self.CalculateFiles(square):
            if file:
                for i in file:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        return squares

    def PossibleSquares(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        if self.MapPiece(square) == None:
            pass
            #TODO Sensible errors for this type of thing.
        elif self.MapPiece(square) in ['R', 'r']:
            squares = self.RookSquares(square)
        elif self.MapPiece(square) in ['N', 'n']:
            squares = self.KnightSquares(square)
        elif self.MapPiece(square) in ['B', 'b']:
            squares = self.BishopSquares(square)
        elif self.MapPiece(square) in ['Q', 'q']:
            squares = self.QueenSquares(square)
        elif self.MapPiece(square) in ['K', 'k']:
            squares = self.KingSquares(square)
        elif self.MapPiece(square) in ['P', 'p']:
            squares = self.PawnSquares(square)
        return squares
        
    def PossibleMoves(self):
        """Returns a list of possible moves, only for the pieces on the side to move.
        The resulting moves are in the form of two square tuples:
            e.g a1 -> d1 : ((0,0),(0,3))
        Returns List.
        """
        movelist = []
        
        if self.sidetomove == 'w':
            samecolour = whitepieces
        if self.sidetomove == 'b':
            samecolour = blackpieces
        
        for i in boardpos:
            if self.MapPiece(i) in samecolour:
                for j in self.PossibleSquares(i):
                    movelist.append((i,j))
        return movelist
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares
        
    def PossibleCastle(self):
        """Returns list of possible castling for the side to move.
        We check the squares are free, castling rights are present, the king is not in check,
        the square the rook lands on not in check, the square the king lands on not in check.
        The castling rights are a list of True|False flags which keep track if the king or rook have been moved.
        self.castlingrights = ['K', 'Q', 'k', 'q']
        return [True|False(kingside), True,False(queenside)]
        Returns List.
        """
        def wks():
            #white king side
            if not self.castlingrights[0]:
                return False
            if self.MapPiece((0,5)) or self.MapPiece((0,6)):
                return False
            if self.isCheck((0,5), 'w') or self.isCheck((0,6), 'w'):
                return False
            return True
            
        def bks():
            #black king side
            if not self.castlingrights[2]:
                return False
            if self.MapPiece((7,5)) or self.MapPiece((7,6)):
                return False
            if self.isCheck((7,5), 'b') or self.isCheck((7,6), 'b'):
                return False
            return True
            
        def wqs():
            #white queen side
            if not self.castlingrights[1]:
                return False
            if self.MapPiece((0,3)) or self.MapPiece((0,2)):
                return False
            if self.isCheck((0,3), 'w') or self.isCheck((0,2), 'w'):
                return False
            return True
            
        def bqs():
            #black queen side
            if not self.castlingrights[2]:
                return False
            if self.MapPiece((7,3)) or self.MapPiece((7,2)):
                return False
            if self.isCheck((7,3), 'b') or self.isCheck((7,2), 'b'):
                return False
            return True
        
        if self.sidetomove == 'w':
            if self.isCheck((0,4), 'w'):
                return [False,False]
            else:
                return [wks(),wqs()]
            
        elif self.sidetomove == 'b':
            if self.isCheck((7,4), 'b'):
                return [False,False]
            else:
                return [bks(),bqs()]
        
    def isCheck(self, square, colour):
        """Returns True or False for if a square is attacked or not for a given colour.
        The colour means, if a king of that colour would be on the square, would it be in check.
        Default colour is the sidetomove.
        Accepts a square tuple, and a colour string.
        Returns True or False.
        """
        if self.sidetomove == 'w':
            enemypieces = blackpieces
        if self.sidetomove == 'b':
            enemypieces = whitepieces
            
        for i in boardpos:
            if self.MapPiece(i) in enemypieces:
                if square in self.PossibleSquares(i):
                    return True
        return False
            
    def isLegal(self):
        """Returns True if the position meets basic requirements of being legal.
        King not on move must not be in check.
        Returns True or False
        """
        if self.sidetomove == 'w':
            otherking = self.FindPieces('k')
            waitcolour = 'b'
        elif self.sidetomove == 'b':
            otherking = self.FindPieces('K')
            waitcolour = 'w'
        
        if self.isCheck(otherking, waitcolour):
            return False
        return True
