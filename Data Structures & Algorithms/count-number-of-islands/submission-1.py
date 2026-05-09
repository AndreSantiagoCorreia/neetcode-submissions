class Solution:
    def isUnvisitedLandWithinBounds(self, row, col, m, n, grid, visited):
        return row >= 0 and col >= 0 and row < m and col < n and self.isNewIsland(row, col, grid, visited)
    
    def isNewIsland(self, row, col, grid, visited):
        return grid[row][col] == "1" and (row,col) not in visited

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
        visited = set()
        m, n = len(grid), len(grid[0])
        res = 0

        for row in range(m):
            for col in range(n):
                curr = grid[row][col]

                if self.isNewIsland(row, col, grid, visited):
                    # increment the result (one island found)
                    res += 1
                    visited.add((row, col))
                    queue.append((row,col))

                    # find neighbors and mark as visited so we do not count this same island
                    while queue:
                        curr_row, curr_col = queue.popleft()
                        
                        for move in moves:
                            if self.isUnvisitedLandWithinBounds(curr_row + move[0], curr_col + move[1], m, n, grid, visited):
                                queue.append((curr_row + move[0], curr_col + move[1]))
                                visited.add((curr_row + move[0], curr_col + move[1]))

        return res



