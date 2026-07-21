class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n

        m = height[0]
        for i in range(1, n):
            prefix_max[i] = m
            m = max(m, height[i])
        
        m = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = m
            m = max(m, height[i])

        total = 0
        for i in range(n):
            w = min(prefix_max[i], suffix_max[i]) - height[i]
            total += max(w, 0)
        return total