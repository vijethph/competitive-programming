# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # look at each cell and run DFS on islands
        # time and size: O(m * n)
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(row, col):
            if (row < 0 or row == ROWS or col < 0 or col == COLS or
                grid[row][col] == 0 or (row, col) in visit):
                return 0
            
            visit.add((row, col))
            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) +
                        dfs(row, col + 1) +
                        dfs(row, col - 1))
        
        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                area = max(area, dfs(row, col))
        
        return area
