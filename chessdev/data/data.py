emptyBoard = ([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 'w', [None,None,None,None],None,0,0)
startBoard = (['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
testpos1 = (['R', 'N', 'B', None, 'K', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
testpos2 = (['R', 'N', 'B', 'Q', None, 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'K', None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
testpos3 = (['R', 'N', 'B', 'Q', None, 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
testpos4 = (['R', 'N', 'B', 'Q', None, 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  None,  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
testpos5 = (['R', 'N', 'B', 'Q', None, 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'K',  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r',  'n',  'b',  'q',  'k',  'b',  'n',  'r'],'w',['K','Q','k','q'],None,0,0)
startBoardnorooks = ([None, 'N', 'B', 'Q', 'K', 'B', 'N', None, 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', None,  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', None,  'n',  'b',  'q',  'k',  'b',  'n',  None],'w',['K','Q','k','q'],None,0,0)

piecetypes = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p']
whitepieces = ['R', 'N', 'B', 'Q', 'K', 'P']
blackpieces = ['r', 'n', 'b', 'q', 'k', 'p']

boardpos = [
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47,
    48, 49, 50, 51, 52, 53, 54, 55,
    56, 57, 58, 59, 60, 61, 62, 63]
    
rankpos = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]]

filepos = [
    [0, 8, 16, 24, 32, 40, 48, 56],
    [1, 9, 17, 25, 33, 41, 49, 57],
    [2, 10, 18, 26, 34, 42, 50, 58],
    [3, 11, 19, 27, 35, 43, 51, 59],
    [4, 12, 20, 28, 36, 44, 52, 60],
    [5, 13, 21, 29, 37, 45, 53, 61],
    [6, 14, 22, 30, 38, 46, 54, 62],
    [7, 15, 23, 31, 39, 47, 55, 63],]

rankdict = {
    0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1,
    8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2,
    16:3, 17:3, 18:3, 19:3, 20:3, 21:3, 22:3, 23:3,
    24:4, 25:4, 26:4, 27:4, 28:4, 29:4, 30:4, 31:4,
    32:5, 33:5, 34:5, 35:5, 36:5, 37:5, 38:5, 39:5,
    40:6, 41:6, 42:6, 43:6, 44:6, 45:6, 46:6, 47:6,
    48:7, 49:7, 50:7, 51:7, 52:7, 53:7, 54:7, 55:7,
    56:8, 57:8, 58:8, 59:8, 60:8, 61:8, 62:8, 63:8}

filedict = { 0:1 , 8:1, 16:1, 24:1, 32:1, 40:1, 48:1, 56:1,
    1:2, 9:2, 17:2, 25:2, 33:2, 41:2, 49:2, 57:2,
    2:3, 10:3, 18:3, 26:3, 34:3, 42:3, 50:3, 58:3,
    3:4, 11:4, 19:4, 27:4, 35:4, 43:4, 51:4, 59:4,
    4:5, 12:5, 20:5, 28:5, 36:5, 44:5, 52:5, 60:5,
    5:6, 13:6, 21:6, 29:6, 37:6, 45:6, 53:6, 61:6,
    6:7, 14:7, 22:7, 30:7, 38:7, 46:7, 54:7, 62:7,
    7:8, 15:8, 23:8, 31:8, 39:8, 47:8, 55:8, 63:8}

whitediagdict = {
    1:1, 8:1,
    40:2, 49:2, 58:2,
    3:3, 10:3, 17:3, 24:3,
    24:4, 33:4, 42:4, 51:4, 60:4,
    5:5, 12:5, 19:5, 26:5, 33:5, 40:5,
    8:6, 17:6, 26:6, 35:6, 44:6, 53:6, 62:6,
    7:7, 14:7, 21:7, 28:7, 35:7, 42:7, 49:7, 56:7,
    1:8, 10:8, 19:8, 28:8, 37:8, 46:8, 55:8,
    23:9, 30:9, 37:9, 44:9, 51:9, 58:9,
    3:10, 12:10, 21:10, 30:10, 39:10,
    39:11, 46:11, 53:11, 60:11,
    5:12, 14:12, 23:12,
    55:13, 62:13}

blackdiagdict = {
    48:1, 57:1,
    2:2, 9:2, 16:2,
    32:3, 41:3, 50:3, 59:3,
    4:4, 11:4, 18:4, 25:4, 32:4,
    16:5, 25:5, 34:5, 43:5, 52:5, 61:5,
    6:6, 13:6, 20:6, 27:6, 34:6, 41:6, 48:6,
    0:7, 9:7, 18:7, 27:7, 36:7, 45:7, 54:7, 63:7,
    15:8, 22:8, 29:8, 36:8, 43:8, 50:8, 57:8,
    2:9, 11:9, 20:9, 29:9, 38:9, 47:9,
    31:10, 38:10, 45:10, 52:10, 59:10,
    4:11, 13:11, 22:11, 31:11,
    47:12, 54:12, 61:12,
    6:13, 15:13}

alldiagdict = [whitediagdict, blackdiagdict]

whitediagpos = [
    [1, 8],
    [40, 49, 58],
    [3, 10, 17, 24],
    [24, 33, 42, 51, 60],
    [5, 12, 19, 26, 33, 40],
    [8, 17, 26, 35, 44, 53, 62],
    [7, 14, 21, 28, 35, 42, 49, 56],
    [1, 10, 19, 28, 37, 46, 55],
    [23, 30, 37, 44, 51, 58],
    [3, 12, 21, 30, 39],
    [39, 46, 53, 60],
    [5, 14, 23],
    [55, 62]]

blackdiagpos = [
    [48, 57],
    [2, 9, 16],
    [32, 41, 50, 59],
    [4, 11, 18, 25, 32],
    [16, 25, 34, 43, 52, 61],
    [6, 13, 20, 27, 34, 41, 48],
    [0, 9, 18, 27, 36, 45, 54, 63],
    [15, 22, 29, 36, 43, 50, 57],
    [2, 11, 20, 29, 38, 47],
    [31, 38, 45, 52, 59],
    [4, 13, 22, 31],
    [47, 54, 61],
    [6, 15]]

centraldict = {0:4, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4,
    8:4, 9:3, 10:3, 11:3, 12:3, 13:3, 14:3, 15:4,
    16:4, 17:3, 18:2, 19:2, 20:2, 21:2, 22:3, 23:4,
    24:4, 25:3, 26:2, 27:1, 28:1, 29:2, 30:3, 31:4,
    32:4, 33:3, 34:2, 35:1, 36:1, 37:2, 38:3, 39:4,
    40:4, 41:3, 42:2, 43:2, 44:2, 45:2, 46:3, 47:4,
    48:4, 49:3, 50:3, 51:3, 52:3, 53:3, 54:3, 55:4,
    56:4, 57:4, 58:4, 59:4, 60:4, 61:4, 62:4, 63:4}
