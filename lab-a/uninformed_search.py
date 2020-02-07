from state_representation import FullState, DynamicState, transition_model
from search_datastructures import Node, BfSearchTree, DfSearchTree, print_solution


def df_expand(parent_node, search_tree, maze):
	for action in ['N', 'E', 'S', 'W']:
		child_state = transition_model(maze, parent_node.get_state(), action)
		child_node = Node(child_state, parent_node, action, parent_node.get_path_cost() + 1) 

		if child_node not in search_tree.get_expanded_nodes():
			search_tree.add_to_frontier(child_node)


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

	 	df_tree.add_to_expanded_nodes(node_to_exp)
	 	df_expand(node_to_exp, df_tree, maze)
 	
	try:
		print_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(df_tree.get_expanded_nodes()))


#########################################################


from collections import deque


def bf_expand(parent_node, search_tree, states_frontier, maze):
	for action in ['N', 'E', 'S', 'W']:
		child_state = transition_model(maze, parent_node.get_state(), action)
		child_node = Node(child_state, parent_node, action, parent_node.get_path_cost() + 1) 

		if (child_node not in search_tree.get_expanded_nodes()) and (child_state not in states_frontier):
			search_tree.add_to_frontier(child_node)
			states_frontier.add(child_state)    

    
def single_bfs(inputFile):
	full_state = FullState(inputFile)
	maze = full_state.get_maze()
	dynamic_state_1 = DynamicState(full_state.get_mouse_loc(), full_state.get_cheese_loc())
	root_node = Node(dynamic_state_1)

	bf_tree = BfSearchTree()
	bf_tree.add_to_frontier(root_node)

	states_frontier = {root_node.get_state()} 
	# a set of all the states in the frontier
	# more explanation    

	while bf_tree.get_frontier() != deque(): 
	 	node_to_exp = bf_tree.deque_frontier() #node to expand
	 	states_frontier.remove(node_to_exp.get_state())
        
	 	if node_to_exp.get_state().goal_test():
	 		goal_node = node_to_exp
	 		break 

	 	bf_tree.add_to_expanded_nodes(node_to_exp)
	 	bf_expand(node_to_exp, bf_tree, states_frontier, maze) 
 	
	try:
		print_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(bf_tree.get_expanded_nodes()))


if __name__ == '__main__':
	single_dfs('1prize-medium.txt')
	single_bfs('1prize-open.txt')