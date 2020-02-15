from state_representation import FullState, DynamicState, transition_model
from search_datastructures import Node, InformedSearchTree, single_heuristic
from collections import deque


def get_visited_prizes(goal_node):
	visited_prizes = deque()
	child_node = goal_node
	parent_node = goal_node.get_parent()

	while parent_node is not None:
		if child_node.get_state().get_cheese_loc() != parent_node.get_state().get_cheese_loc(): #a prize was collected
			visited_prizes.appendleft(child_node.get_state().get_mouse_loc())
			
		child_node = parent_node
		parent_node = parent_node.get_parent()
		
	return visited_prizes


def print_multiprize_sol(maze, goal_node):
	visited_prizes = get_visited_prizes(goal_node)
	order_list = [n for n in range(10)] + [chr(c) for c in range(ord('a'), ord('z')+1)]

	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == 1:
				print("%", end = '')
			else:
				if [i, j] in visited_prizes: 
					print(order_list[visited_prizes.index([i, j])], end = '')
				else:
					print(' ', end = '')
		print()


def multi_heuristic(current_state): #return the manhattan distance to the furthest prize
	try:
		cheese_loc = current_state.get_cheese_loc()
		return max([single_heuristic(current_state, c) for c in cheese_loc]) # + len(cheese_loc) 
	except ValueError: #cheese_loc is empty, i.e. goal reached! 
		return 0


def multi_astar_expand(parent_node, search_tree, maze):
	for action in ['N', 'E', 'S', 'W']:
		child_state = transition_model(maze, parent_node.get_state(), action)

		if child_state in search_tree.get_expanded_states():
			continue 
		
		child_path_cost = parent_node.get_path_cost() + 1
		child_priority = child_path_cost + multi_heuristic(child_state) 
		child_node = Node(child_state, parent_node, action, child_path_cost, child_priority)

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

	 	# because there are duplicates in the frontier, 
	 	# we need to check if node_to_exp is already in expanded_states to avoid expanding the same node twice:
	 	if node_to_exp.get_state() in astar_tree.get_expanded_states():
	 		continue

	 	astar_tree.add_to_expanded_states(node_to_exp.get_state())
	 	multi_astar_expand(node_to_exp, astar_tree, maze)

	try:
		print_multiprize_sol(maze, goal_node)
		print("The path cost is: ", goal_node.get_path_cost())
	except NameError: #goal_node is not defined
		print('Goal not reached')

	print("The number of nodes expanded is: ", len(astar_tree.get_expanded_states()))


if __name__ == '__main__':
	multi_astar('multiprize-micro1.txt') 
	multi_astar('multiprize-tiny.txt')
	#multi_astar('multiprize-small.txt')