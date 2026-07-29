class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        n = len(nums)
        in_window = set()

        while r < n:
            if nums[r] in in_window:
                return True
            in_window.add(nums[r])
            while len(in_window) > k:
                in_window.discard(nums[l])
                l += 1
            r += 1

        return False
        