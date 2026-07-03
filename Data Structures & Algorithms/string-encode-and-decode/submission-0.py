class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(string)}#{string}" for string in strs])


    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0

        ans = []
        while end < len(s):
            while end < len(s) and s[end] != '#':
                end += 1
            l = int(s[start:end])
            ans.append(s[end + 1: end + l + 1])
            start = end + l + 1
            end = start
        return ans
        