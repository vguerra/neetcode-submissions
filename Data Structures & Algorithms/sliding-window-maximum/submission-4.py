class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        n = len(nums)
        curr_max = -10**1000

        ans = []

        while r < n:
            ans.append(max(nums[l:r+1]))
            r += 1
            l += 1

        return ans            
        