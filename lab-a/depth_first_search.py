from state_representation import FullState, DynamicState
from search_datastructures import Node, DfSearchTree, expand_node, print_solution

def single_dfs(inputFile):
	full_state = FullState(inputFile)
	maze = full_state.get_maze()
	dynamic_state_1 = DynamicState(full_state.get_mouse_loc(), full_state.get_cheese_loc())
	root_node = Node(dynamic_state_1)

	df_tree = DfSearchTree()
	df_tree.add_to_frontier(root_node)

	while df_tree.get_frontier() != []:
	 	node_to_exp = df_tree.pop_frontier() #node to expand
	 	
	 	if node_to_exp.get_state().goal_test():
	 		goal_node = node_to_exp
	 		break 

	 	expand_node(node_to_exp, df_tree, maze)
 	
	try:
		print_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(df_tree.get_expanded_nodes()))

if __name__ == '__main__':
	single_dfs('1prize-medium.txt')