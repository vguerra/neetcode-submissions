class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding pivot index 
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
        cut = l

        print(f"cut found at pos {cut}")

        if target < nums[cut]:
            return -1
        elif target <= nums[-1]:
            l = cut
            r = len(nums) - 1
        else:
            l = 0
            r = cut
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
        

# t = 1
# 0  1  2  3  4  5
# l     m        r
# 3  4  5  6  1  2

