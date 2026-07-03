class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hash_set:
                seq_len = 1
                n = num
                while n + 1 in hash_set:
                    seq_len += 1
                    n += 1 
                longest = max(longest, seq_len)
        return longest
        