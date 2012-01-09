from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class PieceMoves(BoardRelations):
    """Calculate how the various pieces can move."""
    
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
        #TODO Castling?
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
        #TODO Untested
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
        #TODO Untested
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
            if self.MapPiece((n+1,m)) is None:
                squares.append((n+1,m))
                if unmoved is True:
                    if self.MapPiece((n+2,m)) is None:
                        squares.append((n+2,m))
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
        #TODO Untested
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
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares
