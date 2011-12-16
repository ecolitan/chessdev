emptyBoard = ([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 'w', [None,None,None,None],None,0,0)
startBoard = (['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
startwithoutrooks = ([None, 'N', 'B', 'Q', 'K', 'B', 'N', None, 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', None,  'n',  'b',  'q',  'k',  'b',  'n',  None],'w',['K','Q','k','q'],None,0,0)
piecetypes = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p']

"""
a8 b8 c8 d8 e8 f8 g8 h8
a7 b7 c7 d7 e7 f7 g7 h7
a6 b6 c6 d6 e6 f6 g6 h6
a5 b5 c5 d5 e5 f5 g5 h5
a4 b4 c4 d4 e4 f4 g4 h4
a3 b3 c3 d3 e3 f3 g3 h3
a2 b2 c2 d2 e2 f2 g2 h2
a1 b1 c1 d1 h1 f1 g1 h1

56 57 58 59 60 61 62 63
48 49 50 51 52 53 54 55
40 41 42 43 44 45 46 47
32 33 34 35 36 37 38 39
24 25 26 27 28 29 30 31
16 17 18 19 20 21 22 23
08 09 10 11 12 13 14 15
00 01 02 03 04 05 06 07

The numbers correspond directly to the position in the pieceplacement List, ie. list[25] = b4
"""

rank1pos = range(0,8)
rank2pos = range(8,16)
rank3pos = range(16,24)
rank4pos = range(24,32)
rank5pos = range(32,40)
rank6pos = range(40,48)
rank7pos = range(48,56)
rank8pos = range(56,64)
