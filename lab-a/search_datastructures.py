from state_representation import DynamicState

class Node:
	def __init__(self, state, parent = None, action = None, path_cost = 0, priority = 0):
		self.state = state
		self.parent = parent 
		self.action = action
		self.path_cost = path_cost
		self.priority = priority

	def __eq__(self, other):
		return self.state == other.get_state()
    
	def __hash__(self):
		return hash(self.state)

	def __lt__(self, other):
		return self.priority < other.get_priority()

	def get_state(self):
		return self.state

	def get_parent(self):
		return self.parent  

	def get_action(self):
		return self.action

	def get_path_cost(self):
		return self.path_cost

	def get_priority(self):
		return self.priority    

##################################################

class SearchTree:
	def __init__(self):
		self.expanded_states = set() #use set for better lookup performance 
		self.frontier = []

	def get_expanded_states(self):
		return self.expanded_states

	def get_frontier(self):
		return self.frontier 

	def add_to_frontier(self, node):
		self.frontier.append(node)

	def add_to_expanded_states(self, state):
		self.expanded_states.add(state)
        
from collections import deque

class BfSearchTree(SearchTree): #the frontier is a FIFO Queue 
	def __init__(self):
		super().__init__()
		self.frontier = deque(self.frontier) #use deque object for better pop() performance 

	def deque_frontier(self):
		return self.frontier.popleft()

class DfSearchTree(SearchTree): #the frontier is a Stack
	def __init__(self):
		super().__init__()

	def pop_frontier(self):
		return self.frontier.pop()

from heapq import heappush, heappop, heapify

class InformedSearchTree(SearchTree): #the frontier is a Min Heap 
	def __init__(self):
		super().__init__()

	def add_to_frontier(self, node): #method overriding 
		heappush(self.frontier, node)

	def pop_frontier_min(self):
		return heappop(self.frontier)
    
#########################################################

#the following helper functions only work for single-prize mazes:

def single_heuristic(current_state, prize_loc):
	current_loc = current_state.get_mouse_loc()
	return abs(prize_loc[1] - current_loc[1]) + abs(prize_loc[0] - current_loc[0]) #manhattan distance  

def get_visited_squares(goal_node):
	visited_squares = [goal_node.get_state().get_mouse_loc()]
	parent_node = goal_node.get_parent()

	while parent_node is not None: 
		visited_squares.append(parent_node.get_state().get_mouse_loc())
		parent_node = parent_node.get_parent()
		
	return visited_squares

def print_sin_solution(maze, goal_node):
	visited_squares = get_visited_squares(goal_node)

	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == 1:
				print("%", end = '')

			else:
				if [i, j] in visited_squares:
					print('#', end = '')
				else:
					print(' ', end = '')
		print()


if __name__ == '__main__': 
	s1 = DynamicState([1,1], [[5,5], [3,7]])
	s2 = DynamicState([1,2], [[5,5], [3,7]])
	s3 = DynamicState([2,1], [[5,5], [3,7]])

	n1 = Node(s1) #root
	n2 = Node(s2, n1, 'E', 1, 0)
	n3 = Node(s3, n1, 'S', 1, 1)

	df_tree = DfSearchTree()
	df_tree.add_to_expanded_states(n1)
	df_tree.add_to_frontier(n2)
	df_tree.add_to_frontier(n3)

	df_tree.pop_frontier()