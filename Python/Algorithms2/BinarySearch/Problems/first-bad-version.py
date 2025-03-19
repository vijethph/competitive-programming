# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            res = isBadVersion(mid)

            if res is True:
                right = mid
            else:
                left = mid + 1
        
        return left