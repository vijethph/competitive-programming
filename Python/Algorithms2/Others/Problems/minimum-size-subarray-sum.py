# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        res = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(right - left + 1, res)
                total -= nums[left]
                left += 1
            
        return 0 if res == float("inf") else res
