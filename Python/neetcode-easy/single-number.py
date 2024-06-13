# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor of two numbers (which are same), is equal to zero
        res = 0

        for n in nums:
            res = n ^ res
        
        return res