'''
Dong Cao, Kate Nguyen
CS365 Lab B
basic_minimax_player.py
'''


from state_representation import Node, initial_state, move_gen, display_state, transition_function, terminal_test, short_terminal_test
from heuristic_functions import evasive, conqueror, pioneer, guardian, offensive_defensive  
from collections import deque
import copy


def expand_tree(black_pos, white_pos, rows_num, cols_num, real_turn, cutoff_depth, eval_func): 
    root = Node(black_pos, white_pos, abs(real_turn-1))
    tree_stack = [root]

    while tree_stack != []: #cut off time
        cur_node = tree_stack.pop()

        cur_black_pos = cur_node.black_pos
        cur_white_pos = cur_node.white_pos

        if cur_node.level == cutoff_depth: # current node is a leaf
            cur_node.util_est = eval_func(cur_black_pos, cur_white_pos, real_turn, rows_num) 
            continue

        child_turn = abs(cur_node.turn - 1)
        child_level = cur_node.level + 1
        
        legal_moves = move_gen(cur_black_pos, cur_white_pos, child_turn, rows_num, cols_num)
        
        for move in legal_moves:
            child_black_pos, child_white_pos = transition_function(cur_black_pos, cur_white_pos, move)
            child = Node(child_black_pos, child_white_pos, child_turn, child_level)

            cur_node.list_children.append(child)

            if short_terminal_test(child_black_pos, child_white_pos, rows_num, child_turn, move):
                child.util_est = eval_func(child_black_pos, child_white_pos, real_turn, rows_num)
                continue # stop expanding this branch further

            tree_stack.append(child)

    return root


def minimax(root):
    if root.list_children != []: # if leaves not reached
        if root.level%2 == 0: # max's turn
            root.util_est = max([minimax(child) for child in root.list_children])
        else:
            root.util_est = min([minimax(child) for child in root.list_children])
    
    return root.util_est


def play_game(heuristic_functions, rows_num, cols_num, rows_of_pieces):
    turn = 0 #white goes first 

    cutoff_depth = 3  #should be changed based on the sizes of the board

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces) 

    display_state(rows_num, cols_num, black_pos, white_pos) #initial state 

    while True:
        eval_func_used = heuristic_functions[turn] #whether it's white's or black's

        root = expand_tree(black_pos, white_pos, rows_num, cols_num, turn, cutoff_depth, eval_func_used) 

        for child in root.list_children:
            minimax(child) # calculate the util_est for all the root's children

        best_next_board_node = max(root.list_children)
        black_pos, white_pos = best_next_board_node.black_pos, best_next_board_node.white_pos

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
    play_game([conqueror, conqueror], 8, 8, 2)