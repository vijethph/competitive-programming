# https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:]) if i+1 < len(nums) else 0
            if leftsum == rightsum:
                return i
        return -1