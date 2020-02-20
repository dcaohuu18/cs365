'''
Dong Cao, Kate Nguyen
CS365 Lab B
state_representation.py
'''

from state_representation import Node, initial_state, move_gen, display_state, transition_function, terminal_test 
from heuristic_functions import evasive, conqueror 
from collections import deque

def expand_tree(black_pos, white_pos, rows_num, cols_num, turn, cutoff_depth):
    # cutoff_depth = 3
    cur_depth = 0
    root = Node(black_pos, white_pos, turn)
    tree_q = deque()
    tree_q.append(root)
    # cur_node = root
    while cur_depth <= cutoff_depth:
        cur_node = tree_q.popleft()
        moves = move_gen(black_pos, white_pos, turn, cols_num)

        for move in moves:
            new_black_set, new_white_set = transition_function(black_pos, white_pos, move)
            new_node = Node(new_black_set, new_white_set, turn, cur_node)

            if terminal_test(black_pos, white_pos, rows_num, cols_num, turn) == True:
                return new_node

            tree_q.append(new_node)
            cur_node.list_children.append(new_node)

        cur_depth += 1
        turn = abs(turn - 1)

    print("Len of tree_q:", len(tree_q))

    return set(tree_q) #bug!


def make_minimax_move(black_set, white_set, turn, rows_num, cols_num, eval_func, cutoff_depth):
    leaves = expand_tree(black_set, white_set, rows_num, cols_num, turn, cutoff_depth)

    print("len of leaves:", len(leaves)) 
     

    #expand_tree() returns the leaves of the search tree 
    
    parents_set = set()

    for leaf in leaves: #calculate the utility of all the leaves 
        leaf.util_est = eval_func(leaf.black_pos, leaf.white_pos, leaf.turn)
        parents_set.add(leaf.parent)
        print(leaf.util_est)

    for level in range(cutoff_depth-1, 0, -1):
        for parent_node in parents_set:
            if level%2 == 0: #Max's turn
                parent_node.util_est = max(parent_node.list_children)
            
            elif level%2 == 1: #Min's turn
                parent_node.util_est = min(parent_node.list_children)

            parents_set.add(parent_node.parent)

        parents_set = set()

    root = parents_set.pop()

    best_next_node_board = max(root.list_children)
    
    black_set, white_set = best_next_node_board.black_set, best_next_node_board.white_set   


def play_game(heuristic_functions, rows_num, cols_num, rows_of_pieces):
    turn = 0 #white goes first 

    black_set, white_set = initial_state(rows_num, cols_num, rows_of_pieces)

    cutoff_depth = 3 #should be changed based on the sizes of the board 

    while True:
        turn = abs(turn - 1) #switch turn (0 -> 1; 1 -> 0)

        eval_func_used = heuristic_functions[turn] #whether it's white's or black's 

        make_minimax_move(black_set, white_set, turn, rows_num, cols_num, eval_func_used, cutoff_depth)

        display_state(rows_num, cols_num, black_set, white_set) 

        if terminal_test(black_set, white_set, rows_num, cols_num, turn):
            terminal_state = True
            break  

if __name__ == '__main__':
    play_game([evasive, evasive], 5, 5, 1)