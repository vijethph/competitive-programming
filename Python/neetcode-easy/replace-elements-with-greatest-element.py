# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initially max = -1
        # reverse iteration

        oldMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(oldMax, arr[i])
            arr[i] = oldMax
            oldMax = newMax 
        
        return arr
        
