import copy
import random

# Constants
WALL_V = "|"
WALL_H = "-"
STEP   = "O"
PATH   = "X"


class Maze:

    dim           = 0
    maze_unsolved = []
    maze_solved   = []
    start         = []
    is_valid      = False

    def __init__(self, dim):
        # Initialize maze
        self.dim = dim
        self.create_maze()
        # Check if we created a valid maze
        self.is_valid = self.solve()

    def create_maze(self):
        # Create top and bottom walls
        walls_temp = []
        for i in range(0, self.dim+2):
            walls_temp.append(WALL_H)
        # Top walls
        self.maze_unsolved.append(walls_temp)
        # Create actual maze, index 
        for i in range(1, self.dim+1):
            temp_inner = [WALL_V]
            for j in range(1, self.dim+1):
                wall_choice = WALL_V
                # TODO - Maybe just make a static wall character instead of doing Vertical and Horizontal..
                if temp_inner[j-1] is not STEP or j == self.dim:
                    wall_choice = WALL_H
                temp_inner.append(random.choice([STEP, wall_choice]))
            temp_inner.append(WALL_V)
            self.maze_unsolved.append(temp_inner)

        # Bottom wall
        exit_added = False
        walls_bottom = copy.deepcopy(walls_temp)
        for i in range(1, self.dim+1):
            if self.maze_unsolved[-2][i] == STEP and not exit_added:
                print('Added exit')
                walls_bottom[i] = STEP
                exit_added = True
        if not exit_added:
            print("Bad maze")
        self.maze_unsolved.append(walls_bottom)


    def solve(self):
        return False

    def create_path(self):
        return False

    def print_maze(self, solved):
        cur_maze = self.maze_unsolved
        if solved:
            cur_maze = self.maze_solved
        for i in range(0, self.dim+2):
            for j in range(0, self.dim+2):
                print(cur_maze[i][j] + " ", end = '')
            print()
