class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def do_reverse(low: int, high: int):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        n = len(nums)
        k = k % n
        if k == 0:
            return

        nums.reverse()
        do_reverse(0, k - 1)
        do_reverse(k, n - 1)

        return
