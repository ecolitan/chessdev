import sys

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
        _position = list(boardobject.pieceplacement) 
        for square in boardpos:
            if _position[square[0]][square[1]] is None:
                _position[square[0]][square[1]] = ' '
        _position.reverse()
        for i in _position:
            print i
        print boardobject.sidetomove
        
    def InputMove(self):
        """Wait for player to input a move.
        returns move as list
        return [(square1, square2), promotepiece]
        """
        
        prompt = """Input your move as start and destination square.
If castling simply input the start square and the desination square for the king.
e.g. e1 g1
For pawn promotion, give the move, followed by the piece to promote to.
e.g. h7 h8 Q
"""
        def convert_move(alg_move):
            #import pdb; pdb.set_trace()
            _hmap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
            _vmap = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':6,'7':6,'8':7}
            _lmove = list(alg_move)
            chars = len(_lmove)
            if chars not in [5,7]:
                print "Invalid move entry!"
                return None
            if _lmove[0] not in _hmap:
                print "Invalid move entry!"
                return None
            if _lmove[1] not in _vmap:
                print "Invalid move entry!"
                return None
            if _lmove[2] is not ' ':
                print "Invalid move entry!"
                return None
            if _lmove[3] not in _hmap:
                print "Invalid move entry!"
                return None
            if _lmove[4] not in _vmap:
                print "Invalid move entry!"
                return None
            if chars == 7:
                if _lmove[5] is not ' ':
                    print "Invalid move entry!"
                    return None
                if (_lmove[6] not in whitepromotions or _lmove[6] not in blackpromotions):
                    print "Invalid move entry!"
                    return None
               
            square1 = (_vmap[_lmove[1]],_hmap[_lmove[0]])
            square2 = (_vmap[_lmove[4]],_hmap[_lmove[3]])
            if chars == 7:
                promotepiece = _lmove[6]
            else:
                promotepiece = None
            return ((square1,square2), promotepiece)
            
        raw_move = raw_input(prompt)
        while convert_move(raw_move) is None:
            raw_move = raw_input(prompt)
            if raw_move in ["exit","quit"]:
                sys.exit(0)
        
        return convert_move(raw_move)

        
