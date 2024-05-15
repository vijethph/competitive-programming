# https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # need to use a max heap
        # time complexity: n logn where logn is to retrieve max element from heap every time
        # but python supports only min heaps - use it by converting all numbers to negative values
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])