# https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest

            res += 1
        return res