# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
                res = mid
            else:
                return mid
        
        return res
