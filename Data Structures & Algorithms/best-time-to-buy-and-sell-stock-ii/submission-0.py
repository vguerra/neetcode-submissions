class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gains = 0
        for p1, p2 in zip(prices, prices[1:]):
            if p2 > p1:
                gains += p2 - p1
        return gains
