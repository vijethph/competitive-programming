# https://leetcode.com/problems/maximum-number-of-removable-characters/description/

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(s, subseq):
            i1, i2 = 0, 0

            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue

                i1 += 1
                i2 += 1
            return i2 == len(subseq)
        
        removed = set()
        res = 0
        left, right = 0, len(removable) - 1

        while left <= right:
            mid = (left + right) // 2

            removed = set(removable[:mid + 1])
            if isSubseq(s, p):
                res = max(res, mid + 1)
                left = mid + 1
            else:
                right = mid - 1
        
        return res