class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            if nums[m] < nums[r] and nums[l] > nums[m]:
                r = m
            if nums[l] <= nums[m] < nums[r]:
                r = m
        return nums[l]

# Reflection
# We use binary search: at every iteration,
# we check wheather :
# mid < left -> switch point is at left side
# mid > right -> swith point is at right side
# 0 1 2 3
# l m   r 
# 4 5 6 7
#       