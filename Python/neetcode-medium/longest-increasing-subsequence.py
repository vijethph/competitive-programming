# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # start at end and compute increasing subsequence
        LIS = [1] * len(nums) # consider the element itself

        for i in range(len(nums) -1, -1, -1): # reverse
            for j in range(i+1, len(nums)): # look forward
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

