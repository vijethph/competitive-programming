# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for num in nums:
            total = total + num
            result.append(total)
        return result