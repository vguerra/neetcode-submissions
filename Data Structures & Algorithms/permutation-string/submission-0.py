class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base = ord('a')
        def signature(s: str) -> list:
            sign = [0] * 26
            for c in s:
                sign[c2i(c)] += 1
            return sign
        
        def c2i(c: s) -> int:
            return ord(c) - base

        counts_target = signature(s1)
        left = 0
        right = len(s1) - 1
        counts_window = signature(s2[:right])

        while right < len(s2):
            counts_window[c2i(s2[right])] += 1
            right += 1
            if counts_target == counts_window:
                return True
            
            counts_window[c2i(s2[left])] -= 1
            left += 1
        return False
