'''
Dong Cao, Kate Nguyen
CS365 Lab B
alpha_beta_player.py
'''


from state_representation import initial_state, move_gen, display_state, transition_function, terminal_test, short_terminal_test
from heuristic_functions import evasive, conqueror, pioneer, guardian, comprehensive
import copy


class ABNode:
    def __init__(self, black_pos, white_pos, turn, parent = None, level = 0):
        self.black_pos = black_pos
        self.white_pos = white_pos
        self.list_children = [] 
        self.turn = turn
        self.parent = parent
        self.level = level
        self.util_est = None
        self.alpha = float('inf')
        self.beta = float('-inf')


def alpha_beta_search(parent, rows_num, cols_num, real_turn, cutoff_depth, eval_func): 
    # prune and apply minimax as we expand
    # use recursion to expand

    pa_black_pos = parent.black_pos
    pa_white_pos = parent.white_pos

    if parent.level == cutoff_depth:
        return eval_func(pa_black_pos, pa_white_pos, real_turn, rows_num)
        # stop expanding this branch further

    maxmin_turn = parent.level%2

    if maxmin_turn == 0: # MAX's turn
        parent.util_est = float('-inf')
    else: # MIN's turn
        parent.util_est = float('inf')


    child_turn = abs(parent.turn - 1)
    child_level = parent.level + 1

    legal_moves = move_gen(pa_black_pos, pa_white_pos, child_turn, rows_num, cols_num)

    for move in legal_moves:
        child_black_pos, child_white_pos = transition_function(pa_black_pos, pa_white_pos, move)
        child = ABNode(child_black_pos, child_white_pos, child_turn, parent, child_level) 

        if short_terminal_test(child_black_pos, child_white_pos, rows_num, child_turn, move):
            child.util_est = eval_func(child_black_pos, child_white_pos, real_turn, rows_num)
            # stop expanding this branch further
        else:
            child.util_est = alpha_beta_search(child, rows_num, cols_num, real_turn, cutoff_depth, eval_func)
        
        parent.list_children.append(child) # do we need to do this, except at the top level? 

        if maxmin_turn == 0: # MAX's turn
            parent.util_est = max(parent.util_est, child.util_est)
            parent.beta = max(parent.beta, child.util_est)
            
            try:
                if parent.beta >= parent.parent.alpha: 
                    return parent.util_est
            except AttributeError: # root reached!
                pass

        else:
            parent.util_est = min(parent.util_est, child.util_est)
            parent.alpha = min(parent.alpha, child.util_est)
            if parent.alpha <= parent.parent.beta:
                return parent.util_est

    return parent.util_est


def play_game(heuristic_functions, rows_num, cols_num, rows_of_pieces):
    turn = 0 #white goes first 

    cutoff_depth = 4  #should be changed based on the sizes of the board

    init_black_pos, init_white_pos = initial_state(rows_num, cols_num, rows_of_pieces)
    
    black_pos = copy.deepcopy(init_black_pos)
    white_pos = copy.deepcopy(init_white_pos) 

    display_state(rows_num, cols_num, black_pos, white_pos) #initial state 

    moves_taken = 0

    while True:
        eval_func_used = heuristic_functions[turn] #whether it's white's or black's

        root = ABNode(black_pos, white_pos, abs(turn-1))

        highest_util = alpha_beta_search(root, rows_num, cols_num, turn, cutoff_depth, eval_func_used) 

        for child in root.list_children: 
            if child.util_est == highest_util:
                black_pos, white_pos = child.black_pos, child.white_pos
                break 

        display_state(rows_num, cols_num, black_pos, white_pos)

        moves_taken += 1

        if terminal_test(black_pos, white_pos, rows_num, cols_num, turn):
            break

        turn = abs(turn - 1) #switch turn (0 -> 1; 1 -> 0)

    print('Number of moves taken: ', moves_taken)
    print('Pieces captured by white: ', len(init_black_pos) - len(black_pos))
    print('Pieces captured by black: ', len(init_white_pos) - len(white_pos))  


if __name__ == '__main__':
    '''
    rows_num = 4
    cols_num = 4
    rows_of_pieces = 2

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces)
    root = ABNode(black_pos, white_pos, 0)

    print(alpha_beta_search(root, rows_num, cols_num, 0, 5, conqueror))
    '''
    play_game([evasive, pioneer], 8, 8, 2)
