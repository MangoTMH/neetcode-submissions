class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestP = 0

        for i in range(len(prices)-1):
            r = i + 1
            buy = prices[i]
            while r < len(prices):
                profit = prices[r] - buy
                print("profit=", profit)
                if profit > highestP:
                    highestP = profit    
                r += 1

        return highestP