# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # O(k logn)
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k > 0:
            k -= 1
            ele = -heapq.heappop(gifts)
            rs = floor(sqrt(ele))
            heapq.heappush(gifts, -rs)

        return -sum(gifts)