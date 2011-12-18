emptyBoard = ([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 'w', [None,None,None,None],None,0,0)
startBoard = (['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
startBoardnorooks = ([None, 'N', 'B', 'Q', 'K', 'B', 'N', None, 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', None,  'n',  'b',  'q',  'k',  'b',  'n',  None],'w',['K','Q','k','q'],None,0,0)
piecetypes = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p']

rankpos = [
    range(0,8),
    range(8,16),
    range(16,24),
    range(24,32),
    range(32,40),
    range(40,48),
    range(48,56),
    range(56,64)]

filepos = [
    [0, 8, 16, 24, 32, 40, 48, 56],
    [1, 9, 17, 25, 33, 41, 49, 57],
    [2, 10, 18, 26, 34, 42, 50, 58],
    [3, 11, 19, 27, 35, 43, 51, 59],
    [4, 12, 20, 28, 36, 44, 52, 60],
    [5, 13, 21, 29, 37, 45, 53, 61],
    [6, 14, 22, 30, 38, 46, 54, 62],
    [7, 15, 23, 31, 39, 47, 55, 63],]

diagpos = [
    [48, 57],
    [40, 49, 58],
    [32, 41, 50, 59],
    [24, 33, 42, 51, 60],
    [16, 25, 34, 43, 52, 61],
    [8, 17, 26, 35, 44, 53, 62],
    [0, 9, 18, 27, 36, 45, 54, 63],
    [1, 10, 19, 28, 37, 46, 55],
    [2, 11, 20, 29, 38, 47],
    [3, 12, 21, 30, 39],
    [4, 13, 22, 31],
    [5, 14, 23],
    [6, 15],
    [1, 8],
    [2, 9, 16],
    [3, 10, 17, 24],
    [4, 11, 18, 25, 32],
    [5, 12, 19, 26, 33, 40],
    [6, 13, 20, 27, 34, 41, 48],
    [7, 14, 21, 28, 35, 42, 49, 56],
    [15, 22, 29, 36, 43, 50, 57],
    [23, 30, 37, 44, 51, 58],
    [31, 38, 45, 52, 59],
    [39, 46, 53, 60],
    [47, 54, 61],
    [55, 62],]

