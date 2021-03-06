from state_representation import FullState, DynamicState, transition_model
from search_datastructures import Node, InformedSearchTree, print_sin_solution, single_heuristic


def greedy_expand(parent_node, search_tree, maze, prize_loc):
	for action in ['N', 'E', 'S', 'W']:
		child_state = transition_model(maze, parent_node.get_state(), action)

		if child_state in search_tree.get_expanded_states(): #if it's already expanded
			continue

		child_priority = single_heuristic(child_state, prize_loc)
		child_node = Node(child_state, parent_node, action, parent_node.get_path_cost() + 1, child_priority) 

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
	 	
	 	if node_to_exp.get_state().goal_test(): #goal achieved
	 		goal_node = node_to_exp
	 		break

	 	if node_to_exp.get_state() in gbf_tree.get_expanded_states(): 
	 		continue 

	 	gbf_tree.add_to_expanded_states(node_to_exp.get_state())
	 	greedy_expand(node_to_exp, gbf_tree, maze, prize_loc)
 	
	try:
		print_sin_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(gbf_tree.get_expanded_states()))

if __name__ == '__main__':
	single_gbfs('1prize-open.txt')