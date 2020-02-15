### How to run:
To solve a maze, from the command line, run ```python3 main.py``` and follow the instructions.

#### Other details:
* ```goal_test()``` is a method of the class ```DynamicState```. To call it: ```state1.goal_test()```

* Given the file name of the maze, ```single_dfs()``` solves single-prize mazes using Depth-first Search. To call it: ```single_dfs('1prize-open.txt')```
  
* Similarly, we have:

    ```single_bfs('1prize-open.txt')``` >> Breadth-first Search 
    
    ```single_gbfs('1prize-open.txt')``` >> Greedy Best-first Search 
    
    ```single_astar('1prize-open.txt')``` >> A* search

* To solve mazes with multiple prizes, call ```multi_astar()```. For example: ```multi_astar('multiprize-tiny.txt')```