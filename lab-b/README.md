### How to run:
From the command line, run ```python3 main.py``` and follow the instructions.

### What each file does:
* ```state_representation.py``` includes the class ```Node``` and helper functions to construct and modify board states like:
    * ```initial_state(rows_num, cols_num, rows_of_pieces)``` returns the initial board state (two sets of black positions and white positions: ```black_pos``` and ```white_pos```) given the numbers of rows, columns, and rows of pieces
    * ```move_gen(black_pos, white_pos, turn, rows_num, cols_num)``` returns all legal moves at a turn 
    * ```display_state(rows_num, cols_num, black_pos, white_pos)``` prints out the board state 
    * ```transition_function(black_pos, white_pos, move)``` returns the new state resulted from the given move
    * ```terminal_test(black_pos, white_pos, rows_num, cols_num, turn)``` checks if a board state is a terminal state
    * ```short_terminal_test(black_pos, white_pos, rows_num, turn, move)``` only checks if the given move leads to a terminal state 
* ```basic_minimax_player.py``` implements minimax search and has two agents play against each other, each using the specified heuristic functions (see ```play_game()``` below). For a (8x8, 2) board, it can think 3 steps ahead. In other words, the search tree is three-layer deep (not including the root).   
* ```alpha_beta_player.py``` applies alpha-beta pruning and can think 4 steps ahead.
* ```heuristic_functions.py``` includes heuristic functions or utility functions that evaluate how favorable a board state is to a player. It has the following functions:
    * ```evasive(black_pos, white_pos, turn, rows_num)```
    * ```conqueror(black_pos, white_pos, turn, rows_num)```
    * ```pioneer(black_pos, white_pos, turn, rows_num)```
    * ```guardian(black_pos, white_pos, turn, rows_num)```
    * ```comprehensive(black_pos, white_pos, turn, rows_num)```
    * ```adaptive(black_pos, white_pos, turn, rows_num)```

#### Other details:
* ```play_game()``` takes the following arguments:
    * ```heuristic_functions```: a two-element list of the heuristic functions used by the two players. The first element of the list is the function used by white; the second is the one used by black
    * ```rows_num```: the board's number of rows
    * ```cols_num```: the board's number of columns
    * ```rows_of_pieces```: the board's number of rows of pieces    
 ```play_game()``` firsts creates an initial board state by calling ```initial_state()```. It then uses minimax search to determine which move to take for each player, displays the new board state resulted from the move, and keeps repeating the process until a terminal state is reached. An example call is ```play_game([evasive, guardian], 8, 8, 2)```.
