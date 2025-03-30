# https://leetcode.com/problems/fibonacci-number/description/

# visualize recursion problems using a decision tree

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: # base case
            return 0
        elif n == 1: # base case
            return 1
        return self.fib(n - 1) + self.fib(n - 2) # recursive case