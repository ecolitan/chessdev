import sys
import copy
import threading
import Queue

from chessdev.boardrelations import BoardRelations
from chessdev.forwardsearch import PreSearch
from chessdev.data.data import *

class BasicWrapper():
    """provide a very basic wrapper for cli testing."""
    
    def __init__(self):
        pass
        
    def PrintBoard(self, boardobject):
        """Print the position of a boardobject to stdout.
        Make it look like a board.
        """
        _position = copy.deepcopy(boardobject.pieceplacement) 
        for square in boardpos:
            if _position[square[0]][square[1]] is None:
                _position[square[0]][square[1]] = ' '
        _position.reverse()
        for i in _position:
            print i
        print boardobject.sidetomove
        
    def InputMove(self):
        """Wait for player to input a move.
        
        When xboard sends your engine a move, it normally sends coordinate algebraic notation. Examples:

        Normal moves:	e2e4
        Pawn promotion:	e7e8q
        Castling:	e1g1, e1c1, e8g8, e8c8

        returns move as list
        return [(square1, square2), promotepiece]
        """
        
        shortprompt = """-> """
        prompt = """Input your move as start and destination square.
If castling simply input the start square and the desination square for the king.
e.g. e1g1
For pawn promotion, give the move, followed by the piece to promote to.
<<<<<<< HEAD
e.g. h7h8q
=======
e.g. h7h8Q
>>>>>>> 8a02754587dab8a65c4c7687561bef6d8eaf44aa
"""
#TODO Fix coordinate notation 
        def convert_move(alg_move):
            #import pdb; pdb.set_trace()
            _hmap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
            _vmap = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
            _lmove = list(alg_move)
            chars = len(_lmove)
            if chars not in [4,5]:
                print "Invalid move entry!"
                return None
            if _lmove[0] not in _hmap:
                print "Invalid move entry!"
                return None
            if _lmove[1] not in _vmap:
                print "Invalid move entry!"
                return None
            if _lmove[2] not in _hmap:
                print "Invalid move entry!"
                return None
            if _lmove[3] not in _vmap:
                print "Invalid move entry!"
                return None
            if chars == 5:
                if (_lmove[4] not in whitepromotions or _lmove[4] not in blackpromotions):
                    print "Invalid move entry!"
                    return None
               
            square1 = (_vmap[_lmove[1]],_hmap[_lmove[0]])
            square2 = (_vmap[_lmove[3]],_hmap[_lmove[2]])
            if chars == 7:
                promotepiece = _lmove[4]
            else:
                promotepiece = None
            return ((square1,square2), promotepiece)
        
        raw_move = raw_input(shortprompt)
        if raw_move in ["exit","quit"]:
            sys.exit(0)
        if raw_move == "debug":
            return raw_move
        while convert_move(raw_move) is None:
            raw_move = raw_input(prompt)
            if raw_move in ["exit","quit"]:
                sys.exit(0)
            if raw_move == "debug":
                return raw_move
        return convert_move(raw_move)

class SimpleGame():
    """Interface to play a simple cli game."""
    
    def __init__(self):
        pass
        
    def CreateGame(self, gamestartpos, playmode=None, human=None):
        """Create a game from a starting position.
        Accepts start position as list.
        Accepts playmode as a string
        playmode is either "hh,hc,cc" human-human, human-computer, computer-computer
        If playmode is hc, human must be either "w" or "b" to indicate what colour the human is playing.
        Game continues until an error or mate.
        """
        currentobject = BoardRelations(gamestartpos)

        if not currentobject.isLegal():
            sys.exit("Invalid starting position")
        
        #TODO Test and play various playmodes 
                
        # human-human
        BasicWrapper().PrintBoard(currentobject)
        
        while True:
            fullmove = BasicWrapper().InputMove()
            
            # Move given must be in the list of possible moves for a position and create a legal position
            
            if fullmove[0][1] not in currentobject.PossibleSquares(fullmove[0][0]):
                print "Illegal move!"
                print fullmove[0]
                print currentobject.PossibleSquares(fullmove[0][0])
                sys.exit(1)
            
            currentobject = PreSearch().GenerateBoard(currentobject, fullmove[0], fullmove[1])
            if PreSearch().isMate(currentobject):
                print "Checkmate"
                break
            
            BasicWrapper().PrintBoard(currentobject)
