class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        right = 0
        n = len(s)

        freq = defaultdict(int)

        while right < n:
            freq[s[right]] += 1
            while (right - left + 1 - max(freq.values())) > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
