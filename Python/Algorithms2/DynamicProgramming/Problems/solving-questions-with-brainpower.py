# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # time: O(N)
        # space: O(N)

        dp = {}

        for i in range(len(questions) - 1, -1 , -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + 1 + questions[i][1], 0),
                dp.get(i + 1, 0)
            )
        
        return dp[0]
