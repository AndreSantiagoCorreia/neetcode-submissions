class Solution:
    def isUnvisitedLandWithinBounds(self, row, col, m, n, grid):
        return row >= 0 and col >= 0 and row < m and col < n and self.isNewIsland(row, col, grid)
    
    def isNewIsland(self, row, col, grid):
        return grid[row][col] == "1"

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: BFS
        Iterate through the graph until we reach a "1" AND it's non-visited
        - Once we reach a "1", start BFS
        - Keep track of visited nodes, so we don't visit twice
        - Only add neighbors to the queue if they are "1"s
        """
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        m, n = len(grid), len(grid[0])
        res = 0

        for row in range(m):
            for col in range(n):
                curr = grid[row][col]

                if self.isNewIsland(row, col, grid):
                    # increment the result (one island found)
                    res += 1
                    grid[row][col] = "0"
                    queue.append((row,col))

                    # find neighbors and mark as visited so we do not count this same island
                    while queue:
                        curr_row, curr_col = queue.popleft()
                        
                        for move in moves:
                            if self.isUnvisitedLandWithinBounds(curr_row + move[0], curr_col + move[1], m, n, grid):
                                queue.append((curr_row + move[0], curr_col + move[1]))
                                grid[curr_row + move[0]][curr_col + move[1]] = "0"

        return res



