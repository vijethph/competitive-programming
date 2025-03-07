# https://leetcode.com/problems/remove-k-digits/description/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # monotonic stack - should be either increasing or decreasing order only
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()

            if not stack and c == "0":
                continue
                
            stack.append(c)
        
        stack = stack[:len(stack) - k] # remove the last k digits
        res =  "".join(stack).lstrip("0") # remove leading zeroes
    
        return res if res else "0"
