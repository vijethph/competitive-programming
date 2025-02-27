# https://leetcode.com/problems/min-stack/description/

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = [] # this is a tracker that keeps a history of all the minimum of all the values so far

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]