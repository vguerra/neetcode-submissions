class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_swap = -1
        n = len(nums)
        l = 0
        r = len(nums) - 1

        while l < n and r >= 0 and l <= r:
            if nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if l == n:
            return n 
        if r < 0:
            return 0
        return l


# [1 0 0 0] 1
        