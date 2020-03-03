'''
Dong Cao, Kate Nguyen
CS365 Lab B
heuristic_functions.py
'''

import random
import copy

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
        if len(white_pos) == 0 or (len(black_pos) > 0 and max(black_pos)[0] == rows_num - 1):
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")
        return len(white_pos) - len(black_pos) + (rows_num - 1 - min(white_pos)[0]) + random.random()
    else:
        if len(black_pos) == 0 or (len(white_pos) > 0 and min(white_pos)[0] == 0):
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")
        return len(black_pos) - len(white_pos) + max(black_pos)[0] + random.random()

def guardian(black_pos, white_pos, turn, rows_num):
    if turn == 0:
        if len(white_pos) == 0 or (len(black_pos) > 0 and max(black_pos)[0] == rows_num - 1):
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")
        return len(white_pos) - len(black_pos) - max(black_pos)[0] + random.random()
    else:
        if len(black_pos) == 0 or (len(white_pos) > 0 and min(white_pos)[0] == 0):
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")
        return len(black_pos) - len(white_pos) - (rows_num - 1 - min(white_pos)[0]) + random.random()

def comprehensive(black_pos, white_pos, turn, rows_num):
    if turn == 0:
        if len(white_pos) == 0 or (len(black_pos) > 0 and max(black_pos)[0] == rows_num - 1):
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")
        return len(white_pos) - len(black_pos) + (rows_num - 1 - min(white_pos)[0]) - max(black_pos)[0] + random.random()
    else:
        if len(black_pos) == 0 or (len(white_pos) > 0 and min(white_pos)[0] == 0):
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")
        return len(black_pos) - len(white_pos) + max(black_pos)[0] - (rows_num - 1 - min(white_pos)[0]) + random.random()

def adaptive(black_pos, white_pos, turn, rows_num):
    if turn == 0:
        if len(white_pos) == 0 or (len(black_pos) > 0 and max(black_pos)[0] == rows_num - 1):
            return float("-inf")
        if min(white_pos)[0] == 0 or len(black_pos) == 0:
            return float("inf")

        top_opp_set = list(black_pos)
        top_opp_set.sort()
        top_opp_set = top_opp_set[:2]

        if min(top_opp_set)[0] >= rows_num//2:
            return len(white_pos) - len(black_pos) - 2*max(black_pos)[0] + random.random()

        last_row_count = sum(map(lambda piece: piece[0]== rows_num - 1, white_pos))

        if max(black_pos)[0] != rows_num - 2:
            return len(white_pos) - len(black_pos) + 1.5*(rows_num - 1 - min(white_pos)[0]) - 1.5*max(black_pos)[0] + last_row_count + random.random()

        return len(white_pos) - len(black_pos) + (rows_num - 1 - min(white_pos)[0]) - 2*max(black_pos)[0] + random.random()
    else:
        if len(black_pos) == 0 or (len(white_pos) > 0 and min(white_pos)[0] == 0):
            return float("-inf")
        if max(black_pos)[0] == rows_num - 1 or len(white_pos) == 0:
            return float("inf")

        top_opp_set = list(white_pos)
        top_opp_set.sort()
        top_opp_set = top_opp_set[:2]

        if max(top_opp_set)[0] <= rows_num//2:
            return len(black_pos) - len(white_pos) - 2*(rows_num - 1 - min(white_pos)[0]) + random.random()

        last_row_count = sum(map(lambda piece: piece[0]== 0, black_pos))

        if min(white_pos)[0] != 1:
            return len(black_pos) - len(white_pos) + 1.5*max(black_pos)[0] - 1.5*(rows_num - 1 - min(white_pos)[0]) + last_row_count + random.random()

        return len(black_pos) - len(white_pos) + max(black_pos)[0] - 2*(rows_num - 1 - min(white_pos)[0]) + random.random()
