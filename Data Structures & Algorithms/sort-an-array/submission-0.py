class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l: int, r:int):
            if r - l > 0:
                m = l + (r - l) // 2
                mergeSort(l, m)
                mergeSort(m + 1, r)
                merge(l, m , r)


        def merge(l: int, m: int, r: int) -> List[int]:
            left_part = nums[l:m + 1]
            right_part = nums[m + 1:r + 1]

            l_i = 0
            r_i = 0

            for k_i in range(l, r + 1):
                if l_i >= len(left_part):
                    nums[k_i] = right_part[r_i]
                    r_i += 1
                elif r_i >= len(right_part):
                    nums[k_i] = left_part[l_i]
                    l_i += 1
                elif left_part[l_i] < right_part[r_i]:
                    nums[k_i] = left_part[l_i]
                    l_i += 1
                else:
                    nums[k_i] = right_part[r_i]
                    r_i += 1
        
        mergeSort(0, len(nums) - 1)
        return nums
        
# l = 2
# m = 2
# r = 3

# l_i = 2
# r_i = 3