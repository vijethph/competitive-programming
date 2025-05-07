# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""
        for char, count in stack:
            res += (char * count)
        
        return res