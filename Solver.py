import copy

# Constants
WALL_V = "|"
WALL_H = "-"
STEP   = "O"
PATH   = "X"

class Solver:

    maze        = []
    path        = []
    maze_exit   = []

    def __init__(self, maze, maze_exit):
        self.maze       = maze
        self.maze_exit  = maze_exit

    def solve(self, cur_step, steps_taken):
        paths = 0
        # Check if finished
        if self.is_solved(cur_step):
            steps_taken.append(cur_step)
            self.path = steps_taken
            return True
        else:
            # Count paths
            paths = self.count_paths(cur_step)
        # Dead end
        if paths == 0:
            return None
        # Single Path
        elif paths == 1:
            next_steps = copy.deepcopy(steps_taken)
            next_steps.append(cur_step)
            # North
            if self.maze[cur_step[0]-1][cur_step[1]] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                new_move = self.solve([cur_step[0]-1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            # East
            elif self.maze[cur_step[0]][cur_step[1]+1] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                new_move = self.solve([cur_step[0], cur_step[1]+1], next_steps)
                if new_move is not None:
                    return new_move
            # West
            elif self.maze[cur_step[0]][cur_step[1]-1] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                new_move = self.solve([cur_step[0], cur_step[1]-1], next_steps)
                if new_move is not None:
                    return new_move
            # South
            elif self.maze[cur_step[0]+1][cur_step[1]] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                new_move = self.solve([cur_step[0]+1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            else:
                return None
        # Multiple Paths
        elif paths > 1:
            # North
            if self.maze[cur_step[0]-1][cur_step[1]] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                next_steps = copy.deepcopy(steps_taken)
                next_steps.append(cur_step)
                new_move = self.solve([cur_step[0]-1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            # East
            if self.maze[cur_step[0]][cur_step[1]+1] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                next_steps = copy.deepcopy(steps_taken)
                next_steps.append(cur_step)
                new_move = self.solve([cur_step[0], cur_step[1]+1], next_steps)
                if new_move is not None:
                    return new_move
            # West
            if self.maze[cur_step[0]][cur_step[1]-1] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                next_steps = copy.deepcopy(steps_taken)
                next_steps.append(cur_step)
                new_move = self.solve([cur_step[0], cur_step[1]-1], next_steps)
                if new_move is not None:
                    return new_move
            # South
            if self.maze[cur_step[0]+1][cur_step[1]] == STEP and not self.traveled_to([cur_step[0],cur_step[1]], steps_taken):
                next_steps = copy.deepcopy(steps_taken)
                next_steps.append(cur_step)
                new_move = self.solve([cur_step[0]+1, cur_step[1]], next_steps)
                if new_move is not None:
                    return new_move
            else:
                return None

    def count_paths(self, cur_step):
        path_count = 0
         # North
        if self.maze[cur_step[0]-1][cur_step[1]] == STEP:
            path_count += 1
        # East
        if self.maze[cur_step[0]][cur_step[1]+1] == STEP:
            path_count += 1
        # South
        if self.maze[cur_step[0]+1][cur_step[1]] == STEP:
            path_count += 1
        # West
        if self.maze[cur_step[0]][cur_step[1]-1] == STEP:
            path_count += 1
        return path_count

    def traveled_to(self, cur_step, steps_taken):
        if len(steps_taken) != 0:
            if cur_step in steps_taken:
                return True
        return False

    def is_solved(self, cur_step):
        if cur_step[0] == self.maze_exit[0] and cur_step[1] == self.maze_exit[1]:
            return True
        return False
