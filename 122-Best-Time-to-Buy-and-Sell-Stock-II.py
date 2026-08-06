class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0 
        l, r = 0, 1
        while r < len(prices):
            dif = prices[r] - prices[l]
            if dif > 0:
                sum += dif
            l += 1
            r += 1
        return sum