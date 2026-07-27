class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)

        window_chars = set()
        longest = 0

        while left < n and right < n:
            if s[right] not in window_chars:
                window_chars.add(s[right])
                longest = max(longest, len(window_chars))
            else:
                while s[right] in window_chars:
                    window_chars.discard(s[left])
                    left += 1
                window_chars.add(s[right])
            right += 1
                
        return longest

        