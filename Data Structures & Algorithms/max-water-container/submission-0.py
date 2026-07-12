class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        water_capacity = lambda i, j: (j - i) * min(heights[j], heights[i])
        max_water_capacity = 0

        while left < right:
            max_water_capacity = max(max_water_capacity, water_capacity(left, right))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water_capacity

        