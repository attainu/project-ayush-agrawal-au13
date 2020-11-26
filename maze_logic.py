class maze_logic:
    
    # this function checks if x,y is valid index for square matrix
    def isSafe(self,maze, x, y, N):

        if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
            return True

        return False

    # this function returns the output either matrix or -1
    def solveMaze(self,maze, N):

        sol = [[0 for j in range(N)] for i in range(N)]

        if not self.solveMazeUtil(maze, 0, 0, sol, N):
            return "-1"
        return sol

    # this function solves the maze problem using backtracking
    def solveMazeUtil(self,maze, x, y, sol, N):

        if x == N - 1 and y == N - 1 and maze[x][y] == 1:
            sol[x][y] = 1
            return True

        if self.isSafe(maze, x, y, N):
            sol[x][y] = 1

            if self.solveMazeUtil(maze, x + 1, y, sol, N):
                return True

            if self.solveMazeUtil(maze, x, y + 1, sol, N):
                return True

            sol[x][y] = 0
            return False
