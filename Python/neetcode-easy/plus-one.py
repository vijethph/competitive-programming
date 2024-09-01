# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = map(str, digits)
        temp = ''.join(temp)
        temp = int(temp)
        temp = temp + 1
        return map(int, str(temp))