class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        i = 0
        for i in range(0, len(prices)-1):
            i += 0
            if prices[i+1] >= prices[i] :
                sum += prices[i+1] - prices[i]
        return sum