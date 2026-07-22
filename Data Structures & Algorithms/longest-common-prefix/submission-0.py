class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        for tpl in zip(*strs):
            if len(set(tpl)) != 1:
                break
            count += 1 
        return "" if count == 0 else strs[0][:count]
        