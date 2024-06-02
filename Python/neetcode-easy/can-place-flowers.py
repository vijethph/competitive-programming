# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]
        
        for i in range(1, len(flowers) - 1): # skip first and last
            if flowers[i-1] == 0 and flowers[i] == 0 and flowers[i+1] == 0:
                flowers[i] = 1
                n -= 1
        return n <= 0

        # alternative solution:
        empty = 0 if flowerbed[0] else 1
        for flower in flowerbed:
            if flower:
                n -= int((empty - 1) / 2) # int division, round toward zero
                empty = 0
            else:
                empty += 1
        
        n -= (empty) // 2
        return n <= 0