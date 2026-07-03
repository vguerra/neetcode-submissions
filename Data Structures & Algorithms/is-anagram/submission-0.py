class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = Counter(s)
        print(counts_s)
        for c_t in t:
            counts_s[c_t] -= 1
        print(counts_s)
        return all(v == 0 for v in counts_s.values())