class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = m - 1, len(nums2) - 1

        for i in range(len(nums1) - 1, -1, -1):
            if i1 < 0 or (i2 >= 0 and nums2[i2] >= nums1[i1]):
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
        
