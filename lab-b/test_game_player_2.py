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


def expand_tree(black_pos, white_pos, rows_num, cols_num, rows_of_pieces, root_turn, cutoff_depth, eval_func): 
    root = Node(black_pos, white_pos, root_turn)
    tree_stack = list()

    legal_moves = move_gen(black_pos, white_pos, root_turn, rows_num, cols_num)
    
    '''
    # randomly pick some moves: 
    try:
        legal_moves = random.sample(legal_moves, (cols_num*rows_of_pieces)//2)
    except ValueError: #there are only a few pieces left
        pass
    '''

    for move in legal_moves:
        child_black_pos, child_white_pos = transition_function(black_pos, white_pos, move)
        child = Node(child_black_pos, child_white_pos, root_turn, root, 1)

        tree_stack.append(child)
        root.list_children.append(child)
    
    while tree_stack != []: #cut off time
        cur_node = tree_stack.pop()

        cur_black_pos = cur_node.black_pos
        cur_white_pos = cur_node.white_pos

        if cur_node.level == cutoff_depth: # current node is a leaf
            cur_node.util_est = eval_func(cur_black_pos, cur_white_pos, root_turn) 
            continue

        child_turn = abs(cur_node.turn - 1)
        child_level = cur_node.level + 1
        
        legal_moves = move_gen(cur_black_pos, cur_white_pos, cur_node.turn, rows_num, cols_num)
        for move in legal_moves:
            child_black_pos, child_white_pos = transition_function(cur_black_pos, cur_white_pos, move)
            child = Node(child_black_pos, child_white_pos, child_turn, cur_node, child_level)

            cur_node.list_children.append(child)

            if terminal_test(child_black_pos, child_white_pos, rows_num, cols_num, child_turn):
                child.util_est = eval_func(child_black_pos, child_white_pos, root_turn)  
                continue # stop expanding this branch further

            tree_stack.append(child)

    return root


def minimax(root, maxmin_turn):
    if root.list_children != []: #if leaves not reached
        if maxmin_turn%2 == 0:
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
    
    play_game([evasive, conqueror], 8, 8, 2)