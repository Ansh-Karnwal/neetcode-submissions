class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, n in enumerate(prices):
            j = i + 1
            if i < len(prices):
                while j < len(prices):
                    max_profit = max(max_profit, prices[j] - n)
                    j += 1
        return max_profit
