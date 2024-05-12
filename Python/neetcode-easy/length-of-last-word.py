# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

        # alternative solution
        # i, length = len(s) - 1, 0

        # while s[i] == " ":
        #     i-= 1
        # while i >= 0 and s[i] != " ":
        #     length += 1
        # return length