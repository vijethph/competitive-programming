# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # O(sqrt(n))
        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
        
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