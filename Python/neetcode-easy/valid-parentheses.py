# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        things = {
            '{':'}',
            '(':')',
            '[':']'
        }

        std = []

        for index,value in enumerate(s):
            if value in things:
                std.append(value)
            elif value in things.values():
                if len(std) > 0:
                    chr = std.pop()
                else:
                    return False
                    
                if things[chr] != value:
                    return False
                else:
                    continue
        if len(std) == 0:
            return True
        else:
            return False

        # alternate solution:
        # stack = []
        # closeToOpen = {
        #     '}':'{',
        #     ')':'(',
        #     ']':'['
        # }

        # for ch in s:
        #     if ch in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[ch]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(ch)
        
        # return True if not stack else False


# Optimized Version:
# class Solution:
#     def isValid(self, s: str) -> bool:
#         things = {
#             '{':'}',
#             '(':')',
#             '[':']'
#         }

#         std = []

#         for index,value in enumerate(s):
#             if value in things:
#                 std.append(value)
#             elif len(std) == 0 or things[std.pop()] != value:
#                 return False
#         return len(std) == 0