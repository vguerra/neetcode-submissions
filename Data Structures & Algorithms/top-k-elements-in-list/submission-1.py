class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)
        for num, count in freq.items():
            buckets[count].append(num)
        
        ans = []
        idx = len(nums) - 1
        while len(ans) < k:
            while buckets[idx] is None:
                idx -= 1
            ans.extend(buckets[idx])
            idx -= 1
        return ans[:k]

        
        