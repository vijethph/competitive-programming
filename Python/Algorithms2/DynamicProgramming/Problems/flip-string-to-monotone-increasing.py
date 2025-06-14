# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        cntone = 0
        for c in s:
            if c == "1":
                cntone += 1
            else:
                res = min(res + 1, cntone)
        
        return res