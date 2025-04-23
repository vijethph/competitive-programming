# https://leetcode.com/problems/unique-paths-ii/description/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # time: O(N*M), space: O(N) 
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N-1] = 1

        for row in reversed(range(M)):
            for col in reversed(range(N)):
                if grid[row][col]:
                    dp[col] = 0
                elif col + 1 < N:
                    dp[col] = dp[col] + dp[col + 1]
        
        return dp[0]
