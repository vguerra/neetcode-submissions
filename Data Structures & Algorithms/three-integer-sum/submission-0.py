class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            target = -nums[i]

            left = i + 1
            right = n - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < n - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1

        return ans

        