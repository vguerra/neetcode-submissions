class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0
        for num in nums:
            currentCount += num
            maxCount = max(maxCount, currentCount)
            if num == 0:
                currentCount = 0
        
        return max(currentCount, maxCount)
        