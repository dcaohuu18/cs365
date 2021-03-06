'''
Dong Cao, Kate Nguyen
CS365 Lab B
state_representation.py
'''


import copy
from collections import deque


class Node:
    def __init__(self, black_pos, white_pos, turn, level = 0):
        self.black_pos = black_pos
        self.white_pos = white_pos
        self.list_children = [] 
        self.turn = turn
        self.level = level
        self.util_est = None

    def __lt__(self, other):
        return self.util_est < other.util_est

    '''
    def __hash__(self):
        return hash(frozenset(self.black_pos.union(self.white_pos)))

    def __eq__(self, other):
        return self.black_pos == other.black_pos and self.white_pos == other.white_pos
    '''


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
    moves = deque()
    
    if turn == 0: ###white
        for pos in white_pos:
            cur_row = pos[0]
            cur_col = pos[1]

            if ((cur_row - 1, cur_col - 1) not in white_pos) and (cur_col - 1 >= 0): 
                moves.appendleft((pos, (cur_row - 1, cur_col - 1))) #move up right (from white's perspective)
                # (possible) captures will get expanded first
                # this move ordering may help with alpha-beta pruning 
                
            if ((cur_row - 1, cur_col + 1) not in white_pos) and (cur_col + 1 <= cols_num - 1):  
                moves.appendleft((pos, (cur_row - 1, cur_col + 1))) #move up left (from white's perspective)

            if ((cur_row - 1, cur_col) not in white_pos) and ((cur_row - 1, cur_col) not in black_pos):
                moves.append((pos, (cur_row - 1, cur_col))) #move up
    
    else:       ###black
        for pos in black_pos:
            cur_row = pos[0]
            cur_col = pos[1]

            if ((cur_row + 1, cur_col - 1) not in black_pos) and (cur_col - 1 >= 0):
                moves.appendleft((pos, (cur_row + 1, cur_col - 1)))
                
            if ((cur_row + 1, cur_col + 1) not in black_pos) and (cur_col + 1 <= cols_num - 1):
                moves.appendleft((pos, (cur_row + 1, cur_col + 1)))

            if ((cur_row + 1, cur_col) not in black_pos) and ((cur_row + 1, cur_col) not in white_pos):
                moves.append((pos, (cur_row + 1, cur_col))) #move up

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


def short_terminal_test(black_pos, white_pos, rows_num, turn, move): # only check if the given move leads to the terminal_state
    if len(black_pos) == 0 or len(white_pos) == 0:
        return True 

    if turn == 0: #white's turn
        return move[1][0] == 0
    
    return move[1][0] == (rows_num - 1) 


def terminal_test(black_pos, white_pos, rows_num, cols_num, turn):
    if len(black_pos) == 0 or len(white_pos) == 0:
        return True

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


if __name__ == '__main__':
    rows_num = 4
    cols_num = 4
    rows_of_pieces = 2

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces)
    display_state(rows_num, cols_num, black_pos, white_pos)
    
    new_black_pos, new_white_pos = transition_function(black_pos, white_pos, ((1,0), (2,0)))
    display_state(rows_num, cols_num, new_black_pos, new_white_pos)

    new_black_pos, new_white_pos = transition_function(new_black_pos, new_white_pos, ((3,1), (2,0)))
    display_state(rows_num, cols_num, new_black_pos, new_white_pos)

    print(terminal_test(new_black_pos, new_white_pos, rows_num, cols_num, 1))

