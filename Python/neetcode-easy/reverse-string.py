# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # O(n)
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

        # alternative solution
        stack = []

        for ch in s:
            stack.append(ch)
        
        i = 0

        while stack:
            s[i] = stack.pop()
            i += 1

        # another alternative solution
        def reverse(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)