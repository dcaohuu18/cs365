import random

def evasive(black_pos, white_pos, turn):       ## takes self state (black_pos or white_pos set) as arg
    if turn == 0:
    	return len(white_pos) + random.random()
    return len(black_pos) + random.random()

def conqueror(black_pos, white_pos, turn):     ## takes opponent's set as arg
    if turn == 0:
    	return 0 - len(black_pos) + random.random()
    return 0 - len(white_pos) + random.random()
