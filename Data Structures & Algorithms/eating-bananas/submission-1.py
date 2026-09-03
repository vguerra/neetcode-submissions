class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_to_eat_at_rate(k: int) -> int:
            return sum([math.ceil(bananas / k) for bananas in piles])
        
        # upper value of k is max(piles)
        # lower bound value is 1
        l = 1
        u = max(piles)

        while l <= u:
            rate = l + (u - l) // 2
            hours_to_eat = hours_to_eat_at_rate(rate)
            
            if hours_to_eat <= h:
                u = rate - 1
            else:
                l = rate + 1        

        return l
        