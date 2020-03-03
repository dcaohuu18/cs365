'''
Dong Cao, Kate Nguyen
CS365 Lab B
main.py
'''

from alpha_beta_player import play_game as ab_player
from basic_minimax_player import play_game as minimax_player
from heuristic_functions import evasive, conqueror, pioneer, guardian, comprehensive, adaptive

def main():
    player_algorithm = input("Choose one of the following algorithms: alpha-beta, minimax\nEnter your input here: ")
    print()
    
    if player_algorithm not in ["alpha-beta", "minimax"]:
        raise ValueError("Wrong algorithm name. Please enter again.\n")

    white_function, black_function = input("Choose players: evasive, conqueror, pioneer, guardian, comprehensive, adaptive\nEnter <white player> <space> <black_player>\nEnter your input here: ").split()
    print()

    function_dict = {"evasive":evasive, "conqueror":conqueror, "pioneer":pioneer, "guardian":guardian, "comprehensive":comprehensive, "adaptive":adaptive}

    if white_function not in function_dict or black_function not in function_dict:
        raise ValueError("Wrong function name. Please enter again.\n")

    rows_num, cols_num, rows_of_pieces= input("Choose a board size.\nEnter <number of rows> <space> <number of columns> <space> <rows of pieces>\nEnter your input here: ").split()
    print()
    
    if type(eval(rows_num)) != int or type(eval(cols_num)) != int or type(eval(rows_of_pieces)) != int:
        raise ValueError("These numbers should be integers. Please enter again.\n")

    if player_algorithm == "alpha-beta":
        ab_player([function_dict[white_function],function_dict[black_function]], int(rows_num), int(cols_num), int(rows_of_pieces))

    elif player_algorithm == "minimax":
        minimax_player([function_dict[white_function],function_dict[black_function]], int(rows_num), int(cols_num), int(rows_of_pieces))

    print("White (O): ", white_function)
    print("Black (X): ", black_function)
    
if __name__ == '__main__':
    main()
