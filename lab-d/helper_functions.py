import numpy as np

class Node():
	def __init__(self, bias, value):
		self.bias = bias
        self.value = value
        # self.nodes_weights = {Node: weight} # the nodes that input values to this node


##########################################################		


def sigmoid(x):
	return 1/(1 - np.exp(-x))


if __name__ == '__main__':
	print(sigmoid(10))
    print(sigmoid(1))
    print(sigmoid(0))
    print(sigmoid(-10))
    print(sigmoid(-10))