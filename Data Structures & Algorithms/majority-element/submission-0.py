class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, count in counts.items():
            if count > (len(nums) // 2):
                return num
        return -1
            
        