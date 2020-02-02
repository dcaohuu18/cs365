from state_representation import FullState, DynamicState, transition_model
from search_datastructures import Node, InformedSearchTree, expand_node, print_solution

def single_heuristic(current_state, prize_loc):
	current_loc = current_state.get_mouse_loc()
	return abs(prize_loc[1] - current_loc[1]) + abs(prize_loc[0] - current_loc[0]) #manhattan distance 

def greedy_expand(parent_node, search_tree, maze, prize_loc):
	search_tree.add_to_expanded_nodes(parent_node)

	for action in ['N', 'E', 'S', 'W']:
		child_state = transition_model(maze, parent_node.get_state(), action)
		child_priority = single_heuristic(child_state, prize_loc)
		child_node = Node(child_state, parent_node, action, parent_node.get_path_cost() + 1, child_priority) 

		if child_node not in search_tree.get_expanded_nodes():
			search_tree.add_to_frontier(child_node)

def single_gbfs(inputFile):
	full_state = FullState(inputFile)
	maze = full_state.get_maze()
	dynamic_state_1 = DynamicState(full_state.get_mouse_loc(), full_state.get_cheese_loc())
	prize_loc = dynamic_state_1.get_cheese_loc()[0] #single prize 

	root_node = Node(dynamic_state_1)
	gbf_tree = InformedSearchTree()
	gbf_tree.add_to_frontier(root_node)

	while gbf_tree.get_frontier() != []:
	 	node_to_exp = gbf_tree.pop_frontier_min() #node to expand
	 	
	 	if node_to_exp.get_state().goal_test():
	 		goal_node = node_to_exp
	 		break 

	 	greedy_expand(node_to_exp, gbf_tree, maze, prize_loc)
 	
	try:
		print_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(gbf_tree.get_expanded_nodes()))

if __name__ == '__main__':
	single_gbfs('1prize-open.txt')