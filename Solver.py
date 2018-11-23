import copy
from Maze import Maze

class Solver:

    maze        = []
    path        = []
    maze_exit   = []

    def __init__(self, maze, maze_exit):
        self.maze       = maze
        self.maze_exit  = maze_exit

    def solve(self, cur_step, steps_taken):
        # Count paths
        paths = self.count_paths(cur_step)
        # Check if finished
        if self.is_solved(cur_step):
            self.path = steps_taken
            return True
        # Dead end
        elif paths == 0:
            return None
        # Single Path
        elif paths == 1:
            next_steps = copy.deepcopy(steps_taken)
            next_steps.append(cur_step)
            # North
            if self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0], cur_step[1]-1], next_steps)
                if new_move is not None:
                    return new_move
            # East
            elif self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0]+1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            # West
            elif self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0]-1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            # South
            elif self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0]+1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            else:
                return None
        # Multiple Paths
        elif paths > 1:
            next_steps = copy.deepcopy(steps_taken)
            next_steps.append(cur_step)
            # North
            if self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0], cur_step[1]-1], next_steps)
                if new_move is not None:
                    return new_move
            # East
            if self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0]+1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            # West
            if self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0]-1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            # South
            if self.maze[cur_step[0]][cur_step[1]-1] == Maze.STEP and not self.traveled_to([cur_step[0],cur_step[1]]):
                new_move = self.solve([cur_step[0]+1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            else:
                return None

        return False

    def count_paths(self, cur_step):
        return False

    def traveled_to(self, cur_step, steps_taken):
        if len(steps_taken) != 0:
            if cur_step in steps_taken:
                return True
        return False

    def is_solved(self, cur_step):
        if cur_step[0] == self.maze_exit[0] and cur_step[1] == self.maze_exit[1]:
            return True
        return False
