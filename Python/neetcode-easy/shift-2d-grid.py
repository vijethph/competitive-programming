# https://leetcode.com/problems/shift-2d-grid/description/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        return [nums[i:i+col] for i in range(0, len(nums), col)]