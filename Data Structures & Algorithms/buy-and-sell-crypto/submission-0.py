class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        i = 0 
        j = 1
        max_gain = 0
        while i < len(prices) and j < len(prices):
            if prices[j] <= prices[i]:
                i += 1
                j = i + 1
            else:
                max_gain = max(max_gain, prices[j] - prices[i])
                j += 1

        return max_gain

        