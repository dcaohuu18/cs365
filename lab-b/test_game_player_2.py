'''
Dong Cao, Kate Nguyen
CS365 Lab B
state_representation.py
'''


from state_representation import Node, initial_state, move_gen, display_state, transition_function, terminal_test
from heuristic_functions import evasive, conqueror 
from collections import deque
import copy
import random


def expand_tree(black_pos, white_pos, rows_num, cols_num, rows_of_pieces, real_turn, cutoff_depth, eval_func): 
    root = Node(black_pos, white_pos, abs(real_turn-1))
    tree_stack = [root]

    while tree_stack != []: #cut off time
        cur_node = tree_stack.pop()

        cur_black_pos = cur_node.black_pos
        cur_white_pos = cur_node.white_pos

        if cur_node.level == cutoff_depth: # current node is a leaf
            cur_node.util_est = eval_func(cur_black_pos, cur_white_pos, real_turn) 
            continue

        child_turn = abs(cur_node.turn - 1)
        child_level = cur_node.level + 1
        
        legal_moves = move_gen(cur_black_pos, cur_white_pos, child_turn, rows_num, cols_num)

        '''
        if cur_node.level <= 0:
        # randomly pick some moves: 
            try:
                legal_moves = random.sample(legal_moves, (cols_num*rows_of_pieces)//2)
            except ValueError: #there are only a few pieces left
                pass
        '''
        
        for move in legal_moves:
            child_black_pos, child_white_pos = transition_function(cur_black_pos, cur_white_pos, move)
            child = Node(child_black_pos, child_white_pos, child_turn, cur_node, child_level)

            cur_node.list_children.append(child)

            if terminal_test(child_black_pos, child_white_pos, rows_num, cols_num, child_turn):
                child.util_est = eval_func(child_black_pos, child_white_pos, real_turn)  
                continue # stop expanding this branch further

            if len(child_black_pos) == 0 or len(child_white_pos) == 0:
                child.util_est = eval_func(child_black_pos, child_white_pos, real_turn)  
                continue # stop expanding this branch further

            tree_stack.append(child)

    return root


def minimax(root, maxmin_turn):
    if root.list_children != []: # if leaves not reached
        if maxmin_turn%2 == 0: # max's turn
            root.util_est = max([minimax(child, abs(maxmin_turn - 1)) for child in root.list_children])
        else:
            root.util_est = min([minimax(child, abs(maxmin_turn - 1)) for child in root.list_children])
    
    return root.util_est


def play_game(heuristic_functions, rows_num, cols_num, rows_of_pieces):
    turn = 0 #white goes first 

    cutoff_depth = 3 #should be changed based on the sizes of the board

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces) 

    display_state(rows_num, cols_num, black_pos, white_pos) #initial state 

    while True:
        eval_func_used = heuristic_functions[turn] #whether it's white's or black's

        root = expand_tree(black_pos, white_pos, rows_num, cols_num, rows_of_pieces, turn, cutoff_depth, eval_func_used) 

        for child in root.list_children:
            minimax(child, 1) # calculate the util_est for all the root's children

        try:
            best_next_board_node = max(root.list_children)
            black_pos, white_pos = best_next_board_node.black_pos, best_next_board_node.white_pos
        except ValueError: #one player is left with no piece to play
            pass

        display_state(rows_num, cols_num, black_pos, white_pos)

        if terminal_test(black_pos, white_pos, rows_num, cols_num, turn):
            break

        turn = abs(turn - 1) #switch turn (0 -> 1; 1 -> 0)  


if __name__ == '__main__':
    '''
    rows_num = 4
    cols_num = 4
    rows_of_pieces = 2

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces)
    root = expand_tree(black_pos, white_pos, rows_num, cols_num, rows_of_pieces, 0, 3, evasive)
    
    print(minimax(root, 0))
    '''
    play_game([conqueror, conqueror], 5, 5, 2) 

    # bug when there's only 1 piece left and it's the turn of the player with less pieces (1) >> fixed!