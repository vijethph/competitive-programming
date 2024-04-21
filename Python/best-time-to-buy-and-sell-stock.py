# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # left - buy, right - sell
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]: # profitable
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right # as prices[right] is much less
            right += 1
        
        return max_profit