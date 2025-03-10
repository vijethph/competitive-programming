# https://leetcode.com/problems/daily-temperatures/description

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack with monotonic decreasing order
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        
        return res