'''
Dong Cao, Kate Nguyen
CS365 Lab B
heuristic_functions.py
'''

import random


def evasive(black_pos, white_pos, turn, rows_num):
    if turn == 0:
    	return len(white_pos) + random.random()
    return len(black_pos) + random.random()

def conqueror(black_pos, white_pos, turn, rows_num):
    if turn == 0:
    	return 0 - len(black_pos) + random.random()
    return 0 - len(white_pos) + random.random()

def pioneer(black_pos, white_pos, turn, rows_num):
    if turn == 0:
        if len(white_pos) == 0:
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")
        return len(white_pos) - len(black_pos) + (rows_num - 1 - min(white_pos)[0]) + random.random()
    else:
        if len(black_pos) == 0:
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")
        return len(black_pos) - len(white_pos) + max(black_pos)[0] + random.random()

def guardian(black_pos, white_pos, turn, rows_num):
    if turn == 0:
        if len(white_pos) == 0:
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")
        return len(white_pos) - len(black_pos) - max(black_pos)[0] + random.random()
    else:
        if len(black_pos) == 0:
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")
        return len(black_pos) - len(white_pos) - (rows_num - 1 - min(white_pos)[0]) + random.random()

def offensive_defensive(black_pos, white_pos, turn, rows_num):
    if turn == 0:
        if len(white_pos) == 0:
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")
        return len(white_pos) - len(black_pos) + (rows_num - 1 - min(white_pos)[0]) - max(black_pos)[0] + random.random()
    else:
        if len(black_pos) == 0:
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")
        return len(black_pos) - len(white_pos) + max(black_pos)[0] - (rows_num - 1 - min(white_pos)[0]) + random.random()