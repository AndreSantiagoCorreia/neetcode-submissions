class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS
        """
        max_area = 0
        queue = deque()
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (0, -1) ,(-1, 0) ,(1, 0)]

        for row in range(m):
            for col in range(n):
                # if it's a 0, skip and find next "land"
                # if it's a 1, BFS through it's neighbors to find more land and compute total area
                if grid[row][col] == 1:
                    queue.append((row, col))
                    grid[row][col] = 0
                    curr_area = 1

                    while queue:
                        curr_row, curr_col = queue.popleft()
                        
                        for move in moves:
                            new_row = curr_row + move[0]
                            new_col = curr_col + move[1]
                            # if in bounds and is a land, add to the queue (it's part of curr_island)
                            if new_row >= 0 and new_col >= 0 and new_row < m and new_col < n and grid[new_row][new_col] == 1:
                                curr_area += 1
                                queue.append((new_row, new_col))
                                grid[new_row][new_col] = 0

                    max_area = max(max_area, curr_area)
        

        return max_area