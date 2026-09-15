class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        ans = []
        cap = len(nums) // 3
        for num, count in counts.items():
            if count > cap:
                ans.append(num)
        return ans     