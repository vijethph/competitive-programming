# https://leetcode.com/problems/count-sub-islands/description/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()

        def dfs(row, col):
            if (row < 0 or col < 0 or row == ROWS or col == COLS or
                grid2[row][col] == 0 or (row, col) in visit):
                return True
            
            visit.add((row, col))
            res = True
            if grid1[row][col] == 0:
                res = False
            
            res = dfs(row - 1, col) and res
            res = dfs(row + 1, col) and res
            res = dfs(row, col - 1) and res
            res = dfs(row, col + 1) and res
            return res
        
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid2[row][col] and (row, col) not in visit and dfs(row, col):
                    count += 1
        
        return count