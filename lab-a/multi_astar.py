from state_representation import FullState, DynamicState, transition_model
from search_datastructures import Node, InformedSearchTree, print_solution
from greedy_bf_search import single_heuristic

'''
def print_solution(maze, goal_node):
	print()
'''

def multi_heuristic(current_state): #return the mahattan distance to the farthest prize
	try:
	    return max([single_heuristic(current_state, c) for c in current_state.get_cheese_loc()])
	except IndexError: #cheese_loc is empty, i.e. goal reached! 
		return 0

def multi_astar_expand(parent_node, search_tree, maze):
	for action in ['N', 'E', 'S', 'W']:
		child_state = transition_model(maze, parent_node.get_state(), action)
		child_path_cost = parent_node.get_path_cost() + 1
		child_priority = child_path_cost + multi_heuristic(child_state) 
		
		child_node = Node(child_state, parent_node, action, child_path_cost, child_priority) 

		if child_node not in search_tree.get_expanded_nodes():
			search_tree.add_to_frontier(child_node)

def multi_astar(inputFile):
	full_state = FullState(inputFile)
	maze = full_state.get_maze()
	dynamic_state_1 = DynamicState(full_state.get_mouse_loc(), full_state.get_cheese_loc()) 

	root_node = Node(dynamic_state_1)
	astar_tree = InformedSearchTree()
	astar_tree.add_to_frontier(root_node)

	while astar_tree.get_frontier() != []:
	 	node_to_exp = astar_tree.pop_frontier_min() #node to expand
	 	
	 	if node_to_exp.get_state().goal_test():
	 		goal_node = node_to_exp
	 		break

	 	astar_tree.add_to_expanded_nodes(node_to_exp)
	 	multi_astar_expand(node_to_exp, astar_tree, maze)
 	
	try:
		print_solution(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(astar_tree.get_expanded_nodes()))

if __name__ == '__main__':
	multi_astar('multiprize-tiny.txt')