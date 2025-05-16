# https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for left in range(len(s) - 9):
            cur = s[left:left + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)

        return list(res)