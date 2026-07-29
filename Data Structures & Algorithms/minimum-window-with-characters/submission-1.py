class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        n = len(s)
        shortest = ""
        found = False

        t_counts = Counter(t)
        s_counts = Counter()

        while r < n:
            s_counts[s[r]] += 1
            while l <= r and all(s_counts[char] >= count for char, count in t_counts.items()):
                # print(f"{s[l:r + 1]} contains {t}")                        
                if not shortest:
                    shortest = s[l:r + 1]
                else:
                    shortest = s[l:r + 1] if (r - l  + 1 < len(shortest)) else shortest
                s_counts[s[l]] -= 1
                l += 1

            r += 1

        return shortest
