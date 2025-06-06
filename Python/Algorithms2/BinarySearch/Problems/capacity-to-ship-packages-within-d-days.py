# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res