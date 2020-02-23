'''
Dong Cao, Kate Nguyen
CS365 Lab B
state_representation.py
'''


import copy


class Node:
    def __init__(self, black_pos, white_pos, turn, parent = None, level = 0):
        self.black_pos = black_pos
        self.white_pos = white_pos
        self.list_children = []
        self.parent = parent 
        self.turn = turn
        self.level = level
        self.util_est = None

    def __lt__(self, other):
        return self.util_est < other.util_est

    def __hash__(self):
        return hash(frozenset(self.black_pos.union(self.white_pos)))

    def __eq__(self, other):
        return self.black_pos == other.black_pos and self.white_pos == other.white_pos


############################################################################


def initial_state(rows_num, cols_num, rows_of_pieces): ### number of rows of pieces in EACH side
    black_pos = set()
    white_pos = set()
    
    for i in range(rows_of_pieces):
        for j in range(cols_num):
            black_pos.add((i,j))

    for i in range(rows_num - 1, rows_num - rows_of_pieces - 1, -1):
        for j in range(cols_num):
            white_pos.add((i,j))

    return black_pos, white_pos


def move_gen(black_pos, white_pos, turn, rows_num, cols_num):
    moves = set()
    
    if turn == 0: ###white
        for pos in white_pos:
            cur_row = pos[0]
            cur_col = pos[1]

            if cur_row - 1 >= 0:
                if ((cur_row - 1, cur_col) not in white_pos) and ((cur_row - 1, cur_col) not in black_pos):
                    moves.add((pos, (cur_row - 1, cur_col))) #move up
                
                if ((cur_row - 1, cur_col - 1) not in white_pos) and (cur_col - 1 >= 0): 
                    moves.add((pos, (cur_row - 1, cur_col - 1))) #move up right (from white's perspective)
                
                if ((cur_row - 1, cur_col + 1) not in white_pos) and (cur_col + 1 <= cols_num - 1):  
                    moves.add((pos, (cur_row - 1, cur_col + 1))) #move up left (from white's perspective)
    
    else:       ###black
        for pos in black_pos:
            cur_row = pos[0]
            cur_col = pos[1]
            
            if cur_row + 1 <= rows_num - 1:
                if ((cur_row + 1, cur_col) not in black_pos) and ((cur_row + 1, cur_col) not in white_pos):
                    moves.add((pos, (cur_row + 1, cur_col))) #move up
                
                if ((cur_row + 1, cur_col - 1) not in black_pos) and (cur_col - 1 >= 0):
                    moves.add((pos, (cur_row + 1, cur_col - 1)))
                
                if ((cur_row + 1, cur_col + 1) not in black_pos) and (cur_col + 1 <= cols_num - 1):
                    moves.add((pos, (cur_row + 1, cur_col + 1)))

    return moves


def display_state(rows_num, cols_num, black_pos, white_pos):
    for i in range(rows_num):
        for j in range(cols_num):
            if (i, j) in black_pos:
                print('X', end = '')
            elif (i, j) in white_pos:
                print('O', end = '')
            else:
                print('.', end = '')
        print()

    print()


def transition_function(black_pos, white_pos, move):
    new_black_pos = copy.deepcopy(black_pos)
    new_white_pos = copy.deepcopy(white_pos)
    
    if move[0] in new_black_pos:
        new_black_pos.remove(move[0])
        new_black_pos.add(move[1])
        new_white_pos.discard(move[1])

    else:
        new_white_pos.remove(move[0])
        new_white_pos.add(move[1])
        new_black_pos.discard(move[1])

    return new_black_pos, new_white_pos


def terminal_test(black_pos, white_pos, rows_num, cols_num, turn):
    if turn == 0: #white's turn
        if len(white_pos) < cols_num:
            for item in white_pos:
                if item[0] == 0:
                    return True 
            return False 

        else:
            for i in range(cols_num):
                if (0, i) in white_pos:
                    return True
            return False 

    else: #black's turn
        if len(black_pos) < cols_num:
            for item in black_pos:
                if item[0] == rows_num - 1:
                    return True 
            return False 

        else:
            for i in range(cols_num):
                if (rows_num-1, i) in black_pos:
                    return True
            return False 

# abs(turn - 1)

if __name__ == '__main__':
    rows_num = 5
    cols_num = 5
    rows_of_pieces = 2

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces)
    display_state(rows_num, cols_num, black_set, white_pos)
    
    new_black_pos, new_white_pos = transition_function(black_pos, white_pos, ((1,0), (2,0)))
    display_state(rows_num, cols_num, new_black_pos, new_white_pos)

    new_black_pos, new_white_pos = transition_function(new_black_pos, new_white_pos, ((3,1), (2,0)))
    display_state(rows_num, cols_num, new_black_pos, new_white_pos)

    print(terminal_test(new_black_pos, new_white_pos, rows_num, cols_num, 1))

