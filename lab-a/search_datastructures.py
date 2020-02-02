class Node:
	def __init__(self, state, parent = None, action = None, path_cost = 0, priority = 0):
		self.state = state
		self.parent = parent 
		self.action = action
		self.path_cost = path_cost
		self.priority = priority

	def __lt__(self, other):
		return self.priority < other.get_priority()

	def __str__(self): #for debugging only!
		return str(self.priority) 

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


class SearchTree:
	def __init__(self):
		self.expanded_nodes = []
		self.frontier = []

	def get_expanded_nodes(self):
		return self.expanded_nodes

	def get_frontier(self):
		return self.frontier 

	def add_to_frontier(self, node):
		self.frontier.append(node)

	def add_to_expanded_nodes(self, node):
		self.expanded_nodes.append(node)

	def print_frontier(self): #for debugging only!
		print([str(n) for n in self.frontier])

class BfSearchTree(SearchTree): #the frontier is a FIFO Queue 
	def __init__(self):
		super().__init__()

	def deque_frontier(self):
		return self.frontier.pop(0)

class DfSearchTree(SearchTree): #the frontier is a Stack
	def __init__(self):
		super().__init__()

	def pop_frontier(self):
		return self.frontier.pop()

class InformedSearchTree(SearchTree): #the frontier is a Priority Queue 
	def __init__(self):
		super().__init__()

	def pop_frontier_min(self):
		min_priority_node = min(self.frontier)
		self.frontier.remove(min_priority_node)
		return min_priority_node

if __name__ == '__main__':
	from state_representation import DynamicState 
	
	s1 = DynamicState([1,1], [[5,5], [3,7]])
	s2 = DynamicState([1,2], [[5,5], [3,7]])
	s3 = DynamicState([2,1], [[5,5], [3,7]])

	n1 = Node(s1) #root
	n2 = Node(s2, n1, 'E', 1, 0)
	n3 = Node(s3, n1, 'S', 1, 1)

	df_tree = DfSearchTree()
	df_tree.add_to_expanded_nodes(n1)
	df_tree.add_to_frontier(n2)
	df_tree.add_to_frontier(n3)
	df_tree.print_frontier()

	print(df_tree.pop_frontier())
	df_tree.print_frontier()

	#https://ai.stackexchange.com/questions/6426/what-is-the-difference-between-tree-search-and-graph-search



		
