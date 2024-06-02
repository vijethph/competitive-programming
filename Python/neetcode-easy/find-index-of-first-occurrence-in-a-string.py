# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

        # alternative solution
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
            
            # alternative:
            # if haystack[i: i + len(needle)] == needle:
            #     return i
        
        return -1