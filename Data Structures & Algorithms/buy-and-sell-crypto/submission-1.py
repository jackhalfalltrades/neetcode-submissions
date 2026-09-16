class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        cp = prices[0]
        for price in prices:
            if price < cp:
                cp = price
            else:
                mp = max(mp, price - cp)
        return mp