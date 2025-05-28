# https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "*":
                stack and stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)