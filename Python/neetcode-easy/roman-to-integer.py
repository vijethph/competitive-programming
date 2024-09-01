# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        doublepairs = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }

        skip = 0

        for i in range(0,len(s)):
            if skip == 1:
                skip = 0
                continue
            
            subd = s[i:i+2]
            sing = s[i]

            if subd in doublepairs:
                total = total + doublepairs[subd]
                skip = 1
            elif sing in values:
                total = total + values[sing]

        return total
            
            

# Optimized Version:

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         total = 0
#         values = {
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000
#         }

#         s = s.replace('IV','IIII').replace('IX','VIIII')
#         s = s.replace('XL', 'XXXX').replace('XC','LXXXX')
#         s = s.replace('CD','CCCC').replace('CM','DCCCC')

#         for ch in s:
#             total+= values[ch]
        
#         return total
            
            