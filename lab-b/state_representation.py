'''
Dong Cao, Kate Nguyen
CS365 Lab B
state_representation.py
'''


import copy


class Node:
    def __init__(self, black_pos, white_pos, turn, depth):
        self.black_pos = black_pos
        self.white_pos = white_pos
        self.list_children = []
        self.turn = turn
        self.util_est = None
        self.depth = depth


def initial_state(num_row, num_col, rows_of_pieces): ### number of rows of pieces in EACH side
    black_pos = set()
    white_pos = set()
    for i in range(rows_of_pieces):
        for j in range(num_col):
            black_pos.add((i,j))

    for i in range(num_row - 1, num_row - rows_of_pieces - 1, -1):
        for j in range(num_col):
            white_pos.add((i,j))

    return black_pos, white_pos, num_row, num_col, rows_of_pieces


def move_gen(black_pos, white_pos, turn, num_col):
    moves = set()
    if turn == 0: ###white
        cur_set = copy.deepcopy(white_pos)
        for pos in cur_set:
            cur_row = pos[0]
            cur_col = pos[1]
            moves.add((pos, (cur_row - 1, cur_col)))
            if cur_col - 1 >= 0:
                moves.add((pos, (cur_row - 1, cur_col - 1)))
            if cur_col + 1 <= num_col:
                moves.add((pos, (cur_row - 1, cur_col + 1)))
    else:       ###black
        cur_set = copy.deepcopy(black_pos)
        for pos in cur_set:
            cur_row = pos[0]
            cur_col = pos[1]
            moves.add((pos, (cur_row + 1, cur_col)))
            if cur_col - 1 >= 0:
                moves.add((pos, (cur_row + 1, cur_col - 1)))
            if cur_col + 1 <= num_col:
                moves.add((pos, (cur_row + 1, cur_col + 1)))

    return moves


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
	black_set, white_set, rows_num, cols_num, rows_of_pieces = initial_state(5, 5, 2)
	display_state(rows_num, cols_num, black_set, white_set)
	
	new_black_set, new_white_set = transition_function(black_set, white_set, ((1,0), (2,0)))
	display_state(rows_num, cols_num, new_black_set, new_white_set)

	new_black_set, new_white_set = transition_function(new_black_set, new_white_set, ((3,1), (2,0)))
	display_state(rows_num, cols_num, new_black_set, new_white_set)

	print(terminal_test(new_black_set, new_white_set, rows_num, cols_num, 1))

