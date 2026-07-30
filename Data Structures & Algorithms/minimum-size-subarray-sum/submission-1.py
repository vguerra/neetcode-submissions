class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        window_sum = 0
        min_length = n + 1

        while r < n:
            window_sum += nums[r]
            while window_sum >= target:
                min_length = min(min_length, r - l + 1)
                window_sum -= nums[l]
                l += 1

            r += 1


        return min_length if min_length != n + 1 else 0


        