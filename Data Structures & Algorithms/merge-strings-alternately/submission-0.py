class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for l, r in zip(word1, word2):
            ans.extend([l, r])
        if len(word1) > len(word2):
            ans.extend(word1[len(word2):])
        else:
            ans.extend(word2[len(word1):])
        return "".join(ans)
        