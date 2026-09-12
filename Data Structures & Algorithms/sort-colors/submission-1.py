class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        k = 0
        for color in [0, 1, 2]:
            for _ in range(freq[color]):
                nums[k] = color
                k += 1
        