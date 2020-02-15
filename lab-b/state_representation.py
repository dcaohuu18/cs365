'''
Dong Cao, Kate Nguyen
Lab B
state_representation.py
'''


# display_state()
# transition_function() 
# terminal_test()


import copy

def display_state(rows_num, cols_num, black_set, white_set):
	for i in range(rows_num):
		for j in range(cols_num):
			if (i, j) in black_set:
				print('X', end = '')
			elif (i, j) in white_set:
				print('O', end = '')
			else:
				print('.', end = '')
		print()

def transition_function(black_set, white_set, move):
	new_black_set = copy.deepcopy(black_set)
	new_white_set = copy.deepcopy(white_set)
	
	if move[0] in new_black_set:
		new_black_set.remove(move[0])
		new_black_set.add(move[1])
		new_white_set.discard(move[1])

	else:
		new_white_set.remove(move[0])
		new_white_set.add(move[1])
		new_black_set.discard(move[1])

	return new_black_set, new_white_set

def terminal_test(black_set, white_set, rows_num, cols_num, turn):
	if turn == 0: #white's turn
		if len(white_set) < cols_num:
			for item in white_set:
				if item[0] == 0:
					return True 
			return False 

		else:
			for i in range(cols_num):
				if (0, i) in white_set:
					return True
			return False 

	else: #black's turn
		if len(black_set) < cols_num:
			for item in black_set:
				if item[0] == rows_num - 1:
					return True 
			return False 

		else:
			for i in range(cols_num):
				if (rows_num-1, i) in black_set:
					return True
			return False 

# abs(turn - 1)

if __name__ == '__main__':
	black_set = {(3,0), (0,1), (0,2), (1,3)}
	white_set = {(4,1), (4,2), (3,3)}
	rows_num = 5
	cols_num = 5
	display_state(rows_num, cols_num, black_set, white_set)
	new_black_set, new_white_set = transition_function(black_set, white_set, ((3,0), (4,0)))
	print()
	display_state(rows_num, cols_num, new_black_set, new_white_set)
	print(terminal_test(new_black_set, new_white_set, rows_num, cols_num, 1))

