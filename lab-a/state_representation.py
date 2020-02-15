import copy

class FullState:
    def __init__(self, inputFile):
        self.maze = []
        self.mouse_loc = [-1, -1]
        self.cheese_loc = [] 
        
        #read the file and construct the state:
        with open(inputFile, 'r') as inputFile:
            lines_list = inputFile.readlines()
            lines_num = len(lines_list)

            for i in range(lines_num): #go through each line/row
                line = lines_list[i]
                self.maze.append([])
                
                for j in range(len(line)): #go through each character/col
                    if line[j] == '%':
                        self.maze[i].append(1) #1 means there's a wall
                    
                    else:
                        if line[j] == '.':
                            self.cheese_loc.append([i, j])
                        
                        elif line[j] == 'P':
                            self.mouse_loc = [i, j]
                        
                        self.maze[i].append(0) #0 means there's no wall
    
    def get_maze(self):
        return self.maze
    
    def get_mouse_loc(self):
        return self.mouse_loc

    def set_mouse_loc(self, new_mouse_loc):
        self.mouse_loc = new_mouse_loc

    def get_cheese_loc(self):
        return self.cheese_loc

    def set_mouse_loc(self, new_cheese_loc):
        self.cheese_loc = new_cheese_loc

    def print_full_state(self): #print out the state for debugging
        for i in range(len(self.maze)):
            row = self.maze[i] 
            for j in range(len(row)):
                if row[j] == 1:
                    print('%', end = "")
                elif [i, j] == self.mouse_loc:
                    print('P', end = "")
                elif [i, j] in self.cheese_loc:
                    print('.', end = "")
                else:
                    print(' ', end = "")
            print()
            

class DynamicState:
    def __init__(self, mouse_loc, cheese_loc):
        self.mouse_loc = mouse_loc
        self.cheese_loc = cheese_loc
        
    def __hash__(self): #is this a good hash method?
        coordinates_list = [e for e in self.mouse_loc]
        for l in self.cheese_loc:
            coordinates_list += [e for e in l]
        return hash(frozenset(coordinates_list))
    
    def get_mouse_loc(self):
        return self.mouse_loc

    def set_mouse_loc(self, new_mouse_loc):
        self.mouse_loc = new_mouse_loc

    def get_cheese_loc(self):
        return self.cheese_loc

    def set_mouse_loc(self, new_cheese_loc):
        self.cheese_loc = new_cheese_loc

    def __eq__(self, other):
        return (self.mouse_loc == other.mouse_loc) and (self.cheese_loc == other.cheese_loc)

    def goal_test(self):
        return self.cheese_loc == [] #check if there's no cheese left


def transition_model(maze, old_state, action):
    new_state = copy.deepcopy(old_state)
    old_mouse_loc = old_state.get_mouse_loc()

    #update mouse_loc:
    if action == 'N' and maze[old_mouse_loc[0] - 1][old_mouse_loc[1]] == 0:
        new_state.mouse_loc[0] -= 1 #move up

    elif action == 'E' and maze[old_mouse_loc[0]][old_mouse_loc[1] + 1] == 0: 
        new_state.mouse_loc[1] += 1 #move right

    elif action == 'S' and maze[old_mouse_loc[0] + 1][old_mouse_loc[1]] == 0: 
        new_state.mouse_loc[0] += 1 #move down

    elif action == 'W' and maze[old_mouse_loc[0]][old_mouse_loc[1] - 1] == 0: 
        new_state.mouse_loc[1] -= 1 #move left
        
    #update cheese_loc:
    try:
        new_state.cheese_loc.remove(new_state.get_mouse_loc())
    except ValueError: #not in list
        pass

    return new_state

if __name__ == '__main__':
    full_state = FullState("1prize-medium.txt")
    full_state.print_full_state()
    
    first_dynamic_state = DynamicState(full_state.get_mouse_loc(), full_state.get_cheese_loc())    
    print(first_dynamic_state.get_mouse_loc())

    next_dynamic_state = transition_model(full_state.get_maze(), first_dynamic_state, 'E')   
    print(next_dynamic_state.get_mouse_loc())    
    print(next_dynamic_state.goal_test())
    
    full_state.set_mouse_loc(next_dynamic_state.get_mouse_loc())
    full_state.print_full_state()