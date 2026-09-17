class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0

        while l <= r:
            p1 = people[l]
            p2 = people[r]
            t = p1 + p2

            if t <= limit:
                boats += 1
                l += 1
            elif p2 <= limit:
                boats += 1
            r -= 1
        
        return boats
