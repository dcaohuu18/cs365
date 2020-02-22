'''
Dong Cao, Kate Nguyen
CS365 Lab B
state_representation.py
'''

from state_representation import Node, initial_state, move_gen, display_state, transition_function, terminal_test 
from heuristic_functions import evasive, conqueror 
from collections import deque
import copy

def expand_tree(black_pos, white_pos, rows_num, cols_num, root_turn, cutoff_depth):
    # cutoff_depth = 3
    cur_depth = 0
    root = Node(black_pos, white_pos, root_turn)
    
    tree_q = deque()
    tree_q.append(root)
    # cur_node = root
    
    while True: 
        cur_node = tree_q.popleft()
        cur_black_pos = cur_node.black_pos
        cur_white_pos = cur_node.white_pos
        #cur_depth = cur_node.level # bug here: the first leaf will still get expanded
        
        if cur_node.level == cutoff_depth:
            tree_q.append(cur_node)
            break

        child_turn = abs(cur_node.turn - 1)
        child_level = cur_node.level + 1
        
        legal_moves = move_gen(cur_black_pos, cur_white_pos, cur_node.turn, cols_num)
        for move in legal_moves:
            child_black_pos, child_white_pos = transition_function(cur_black_pos, cur_white_pos, move)
            child = Node(child_black_pos, child_white_pos, child_turn, cur_node, child_level)

            if terminal_test(child_black_pos, child_white_pos, rows_num, cols_num, child_turn):
                return deque([child])

            tree_q.append(child)
            cur_node.list_children.append(child)    

    print("Len of tree_q:", len(tree_q))

    return tree_q # set(tree_q) > bug!


def make_minimax_move(black_pos, white_pos, turn, rows_num, cols_num, eval_func, cutoff_depth):
    leaves = expand_tree(black_pos, white_pos, rows_num, cols_num, turn, cutoff_depth)
    #expand_tree() returns the leaves of the search tree

    print("len of leaves:", len(leaves)) 
    
    parents_set = set()

    for leaf in leaves: #calculate the utility of all the leaves 
        leaf.util_est = eval_func(leaf.black_pos, leaf.white_pos, leaf.turn)
        parents_set.add(leaf.parent)

    for level in range(cutoff_depth-1, 0, -1):
        grandparents_set = set()
        
        for parent_node in parents_set:
            if level%2 == 0: #Max's turn
                parent_node.util_est = max(parent_node.list_children)
            
            elif level%2 == 1: #Min's turn
                parent_node.util_est = min(parent_node.list_children)

            grandparents_set.add(parent_node.parent)
        
        parents_set = copy.deepcopy(grandparents_set)

    root = parents_set.pop()

    best_next_node_board = max(root.list_children)
    
    return best_next_node_board.black_pos, best_next_node_board.white_pos   


def play_game(heuristic_functions, rows_num, cols_num, rows_of_pieces):
    turn = 0 #white goes first 

    cutoff_depth = 3 #should be changed based on the sizes of the board

    black_pos, white_pos = initial_state(rows_num, cols_num, rows_of_pieces) 

    display_state(rows_num, cols_num, black_pos, white_pos) #initial state 

    while True:
        eval_func_used = heuristic_functions[turn] #whether it's white's or black's 

        black_pos, white_pos = make_minimax_move(black_pos, white_pos, turn, rows_num, cols_num, eval_func_used, cutoff_depth)

        display_state(rows_num, cols_num, black_pos, white_pos) 

        if terminal_test(black_pos, white_pos, rows_num, cols_num, turn):
            break

        turn = abs(turn - 1) #switch turn (0 -> 1; 1 -> 0)  


if __name__ == '__main__':
    play_game([evasive, evasive], 5, 5, 1)