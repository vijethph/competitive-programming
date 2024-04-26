# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up dynamic programming approach
        one, two = 1, 1 # takes 1 step at the top, and 2 steps from previous step

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one