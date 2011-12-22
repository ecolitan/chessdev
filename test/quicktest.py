from chessdev.boardrelations import BoardRelations
from chessdev.kingmoves import KingMoves
from chessdev.rookmoves import RookMoves
from chessdev.bishopmoves import BishopMoves
import chessdev.bishopmoves

from test2 import Test2

from chessdev.data.data import *
from chessdev.data.examples import *

def quicktest():
    
    test1 = BishopMoves(startBoard)
    print test1.sidetomove
    
