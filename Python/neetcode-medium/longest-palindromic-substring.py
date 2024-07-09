# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # consider each character to be center of palindrome, expand both sides and check
        res = ""
        res_len = 0

        for idx in range(len(s)):
            # odd length
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1

            # even length
            left, right = idx, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1
        
        return res