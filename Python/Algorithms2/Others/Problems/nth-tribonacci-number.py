# https://leetcode.com/problems/fibonacci-number/description/

from functools import cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def tribonachi(n):
            # base cases
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            # recursive case
            return tribonachi(n - 3) + tribonachi(n - 2) + tribonachi(n - 1)
        
        return tribonachi(n)