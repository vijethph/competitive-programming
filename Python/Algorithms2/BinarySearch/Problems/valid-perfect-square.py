# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # O(logn)
        
        left, right = 1, num 
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True 
        return False