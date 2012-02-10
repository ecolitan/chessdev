import re

emptyBoard = [[[None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None]],
               'w', [False,False,False,False],None,0,0]

startBoard = [[['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
               ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
               [None,  None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
               ['r',  'n',  'b',  'q',  'k',  'b',  'n',  'r']],
               'w',[True,True,True,True],None,0,0]

testpos1 = [[['R', None, 'B', 'Q', 'R', None, 'K', None],
            ['P', 'P', 'B', None, None, 'P', 'P', None],
            [None, None, 'P', None, None, 'N', 'N', 'P'],
            [None, None, 'p', None, 'P', None, None, None],
            [None, 'p', 'n', 'P', 'p', None, None, None],
            ['p', None, None, 'p', None, 'n', None, None],
            [None, None, 'q', None, 'b', 'p', 'p', 'p'],
            ['r', None, 'b', None, 'r', None, 'k', None]],
            'w', [False,False,False,False],None,6,15]
            
piecetypes = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p']
whitepieces = ['R', 'N', 'B', 'Q', 'K', 'P']
blackpieces = ['r', 'n', 'b', 'q', 'k', 'p']
whitepromotions = ['R', 'N', 'B', 'Q']
blackpromotions = ['r', 'n', 'b', 'q']

boardpos = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
            (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
            (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]


testpos2=[[['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'], ['P', 'P', None, 'P', 'P', 'P', 'P', 'P'], [None, None, None, None, None, None, None, None], [None, None, 'P', None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']], 'b', [True, True, True, True], None, 0, 0]

# http://home.hccnet.nl/h.g.muller/engine-intf.html#8
valid_commands = ['xboard',
                'protover',                 # 'protover N',
                'accepted',
                'rejected',
                'new',
                'quit',
                'force',
                'go',
                'level',                    # 'level MPS BASE INC',
                'st',                       # 'st TIME',
                'sd',                       # 'sd DEPTH',
                'variant',                  # 'variant VARNAME',
                'random',
                'playother',
                'nps',                      # 'nps NODE_RATE',
                'time',                     # 'time N',
                'otim',                     # 'otim N',
                'usermove',                 # 'usermove MOVE',
                '?',
                'ping',
                'draw',
                'result',                   # 'result RESULT {COMMENT}',
                'setboard',                 # 'setboard FEN',
                'edit',
                'hint',
                'bk',
                'undo',
                'remove',
                'hard',
                'easy',
                'post',
                'nopost',
                'analyze',
                'name',                     # 'name X',
                'rating',
                'ics',                      # 'ics HOSTNAME',
                'computer',
                'pause',
                'resume',
                'memory',                   # 'memory N',
                'cores',                    # 'cores N',
                'egtpath',                  # 'egtpath TYPE PATH',
                'option',                   # 'option NAME[=VALUE]',
                ]

valid_move_input = r"""([abcdefgh][1-8]){2}([qrbn])?"""
valid_move_input_obj = re.compile(valid_move_input)














