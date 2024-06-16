# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text) # or float("inf")
        for ch in balloon:
            res = min(res, countText[ch] // balloon[ch])
        
        return res