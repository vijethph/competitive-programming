# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast==1

    def squared(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result