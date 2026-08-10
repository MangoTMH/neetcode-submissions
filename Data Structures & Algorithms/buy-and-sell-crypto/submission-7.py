class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highestP = 0

        for sell in prices:
            lowest = min(lowest, sell)
            highestP = max(highestP, sell - lowest)

        return highestP