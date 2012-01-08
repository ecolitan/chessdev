from chessdev.data.data import *
from chessdev.customexceptions import *
from chessdev.boardrelations import *

class BishopMoves(BoardRelations):
    """Calculate various bishop moves.
    """
        
    def PossibleSquares(self, square):
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
                
    def PossibleMoves(self, square):
        """Returns list of possible moves for a bishop on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a bishop on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares

class KingMoves(BoardRelations):
    """Calculates various King moves.
    """
            
    def PossibleSquares(self, square):
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
        
    def PossibleMoves(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares

class KnightMoves(BoardRelations):
    """Calculate various knight moves.
    """

    def PossibleSquares(self, square):
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
            if len(rank) >= 1:
                squares.remove(rank[1])
                
        for file in self.CalculateFiles(square):
            if len(file) >= 1:
                squares.remove(file[1])

        for diag in self.CalculateDiags(square):
            if len(diag) >= 1:
                squares.remove(diag[1])
                
        return squares

    def PossibleMoves(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares

class PawnMoves(BoardRelations):
    """Calculate various pawn moves.
    """

    def PossibleSquares(self, square):
        """Returns a list of possible moves for a pawn to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        unmoved = False
        n,m = square
        
        #white pawns go to higher numbers, black pawns to lower
        if self.MapPiece(square) == 'P':
            if n==1:
                unmoved = True
            if self.MapPiece(n+1,m):
                squares.append(n+1,m)
                if unmoved:
                    if self.MapPiece(n+2,m):
                        squares.append(n+2,m)
            if m+1 != 8:
                if self.MapPiece(n+1,m+1) not in samecolour:
                    squares.append(n+1,m+1)
            if m-1 != -1:
                if self.MapPiece(n+1,m-1) not in samecolour:
                    squares.append(n+1,m-1)
            if self.epsquare:
                if (n+1,m-1) == self.epsquare or (n+1,m+1) == self.epsquare:
                    squares.append(self.epsquare)
                
        if self.MapPiece(square) == 'p':
            if n==6:
                unmoved = True
            if self.MapPiece(n-1,m):
                squares.append(n-1,m)
                if unmoved:
                    if self.MapPiece(n-2,m):
                        squares.append(n-2,m)
            if m+1 != 8:
                if self.MapPiece(n-1,m+1) not in samecolour:
                    squares.append(n-1,m+1)
            if m-1 != -1:
                if self.MapPiece(n-1,m-1) not in samecolour:
                    squares.append(n-1,m-1)
            if self.epsquare:
                if (n-1,m-1) == self.epsquare or (n-1,m+1) == self.epsquare:
                    squares.append(self.epsquare)

        return squares

    def PossibleMoves(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares

class QueenMoves(BoardRelations):
    """Calculates various queen moves.
    """
    
    def PossibleSquares(self, square):
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

    def PossibleMoves(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares

class RookMoves(BoardRelations):
    """Calculate various rook moves.
    """
    
    def PossibleSquares(self, square):
        """Returns a list of possible moves for a rook to move to.
        Don't worry about check, only that the square is not occupied by a piece of the same colour.
        Accepts square Tuple.
        Returns List.
        """
        squares = []
        samecolour = self.PieceColour(square)
        
        #for each rank and file, step along until edge or a piece is reached. If enemy piece, include square.
        print square
        for rank in self.CalculateRanks(square):
            if rank:
                for i in rank:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        print square
        for file in self.CalculateFiles(square):
            if file:
                for i in file:
                    if self.MapPiece(i) not in samecolour:
                        squares.append(i)
                    else:
                        break
        return squares

    def PossibleMoves(self, square):
        """Returns list of possible moves for a piece on a given square.
        Accepts square Tuple.
        Returns List of two-square Tuples.
        """
        moves = []
        for i in self.PossibleSquares(square):
            moves.append((square,i))
        return moves
        
    def PossibleCaptures(self, square):
        """Returns list of possible captures for a piece on a given square.
        Accepts square Tuple.
        Returns List of squares."""
        squares = []
        for i in self.PossibleSquares(square):
            if self.MapPiece(i):
                squares.append(i)
        return squares
