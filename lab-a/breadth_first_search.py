from state_representation import FullState, DynamicState
from search_datastructures import Node, BfSearchTree, expand_node, print_solution

def single_bfs(inputFile): #Should I put this along with dfs into one file called uninformed_search.py
	full_state = FullState(inputFile)
	maze = full_state.get_maze()
	dynamic_state_1 = DynamicState(full_state.get_mouse_loc(), full_state.get_cheese_loc())
	root_node = Node(dynamic_state_1)

	bf_tree = BfSearchTree()
	bf_tree.add_to_frontier(root_node)

	while bf_tree.get_frontier() != []:
	 	node_to_exp = bf_tree.deque_frontier() #node to expand
	 	
	 	if node_to_exp.get_state().goal_test():
	 		goal_node = node_to_exp
	 		break 

	 	expand_node(node_to_exp, bf_tree, maze)
 	
	try:
		print_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(bf_tree.get_expanded_nodes()))

if __name__ == '__main__':
	single_bfs('1prize-tiny.txt')