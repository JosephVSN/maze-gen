import copy
import random
from Solver import Solver
# Constants
WALL_V = "|"
WALL_H = "-"
STEP   = "O"
PATH   = "X"


class Maze:

    dim           = 0
    maze_unsolved = []
    maze_solved   = []
    maze_exit     = []
    start         = []
    is_valid      = False

    def __init__(self, dim):
        # Initialize maze
        self.dim = dim
        self.create_maze()
        # Re-create until we get a valid maze
        self.is_valid = self.solve()
        while not self.is_valid:
            self.maze_unsolved = []
            self.maze_exit = []
            self.maze_start = []
            self.create_maze()
            self.is_valid = self.solve()

    def create_maze(self):
        # Seed random
        random.seed()
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
            if self.maze_unsolved[self.dim][i] == STEP and not exit_added:
                walls_bottom[i] = STEP
                self.maze_exit = [self.dim+1, i]
                exit_added = True
        self.maze_unsolved.append(walls_bottom)


    def solve(self):
        starts = self.find_possible_starts()
        if len(self.maze_exit) == 0 or len(starts) == 0:
            return
        s = Solver(self.maze_unsolved, self.maze_exit)
        for start in starts:
            if s.solve(start, []):
                self.generate_solution(s.path)
                return True

    def find_possible_starts(self):
        starts_pos = []
        try:
            for i in range(1, self.dim+1):
                if self.maze_unsolved[1][i] == STEP:
                    starts_pos.append([1, i])
        except:
            raise RuntimeError("Map was not initiliazed before call to solve.")
        return starts_pos

    def print_maze(self, solved):
        cur_maze = self.maze_unsolved
        if solved:
            cur_maze = self.maze_solved
        for i in range(0, self.dim+2):
            for j in range(0, self.dim+2):
                print(cur_maze[i][j] + " ", end = '')
            print()

    def generate_solution(self, path):
        # Copy unsolved maze to solved maze
        self.maze_solved = copy.deepcopy(self.maze_unsolved)
        for step in path:
            self.maze_solved[step[0]][step[1]] = PATH