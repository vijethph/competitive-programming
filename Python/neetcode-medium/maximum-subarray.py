# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0: # if the current sum is less than 0, then no need to extend subarray sliding window further; reset it
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub