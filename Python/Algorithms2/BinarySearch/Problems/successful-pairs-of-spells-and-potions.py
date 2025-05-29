# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O(nlogm + mlogm)
        # sort potions and binary search

        potions.sort()
        res = []

        for s in spells:
            left, right = 0, len(potions) - 1
            idx = len(potions)

            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                    idx = mid
                else:
                    left = mid + 1
            
            res.append(len(potions) - idx)
        
        return res